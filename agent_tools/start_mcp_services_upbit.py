#!/usr/bin/env python3
"""
Start MCP services with Upbit trade and price tools.

Reuses ports from env to remain compatible with BaseAgent's default mcp_config keys.
Services:
  - Math: agent_tools/tool_math.py
  - Search: agent_tools/tool_jina_search.py (requires JINA_API_KEY)
  - TradeTools: agent_tools/tool_trade_upbit.py (uses UPBIT_* env)
  - LocalPrices: agent_tools/tool_get_price_upbit.py
"""

import os
import sys
import time
import signal
import subprocess
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


class MCPServiceManager:
    def __init__(self):
        self.services = {}
        self.running = True

        self.ports = {
            'math': int(os.getenv('MATH_HTTP_PORT', '8000')),
            'search': int(os.getenv('SEARCH_HTTP_PORT', '8001')),
            'trade': int(os.getenv('TRADE_HTTP_PORT', '8002')),
            'price': int(os.getenv('GETPRICE_HTTP_PORT', '8003')),
        }

        self.service_configs = {
            'math': {
                'script': 'tool_math.py',
                'name': 'Math',
                'port': self.ports['math'],
            },
            'search': {
                'script': 'tool_jina_search.py',
                'name': 'Search',
                'port': self.ports['search'],
            },
            'trade': {
                'script': 'tool_trade_upbit.py',
                'name': 'TradeTools',
                'port': self.ports['trade'],
            },
            'price': {
                'script': 'tool_get_price_upbit.py',
                'name': 'LocalPrices',
                'port': self.ports['price'],
            },
        }

        self.log_dir = Path('../logs')
        self.log_dir.mkdir(exist_ok=True)

        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

    def signal_handler(self, signum, frame):
        print("\nStopping all services...")
        self.stop_all_services()
        sys.exit(0)

    def start_service(self, service_id, config):
        script_path = config['script']
        service_name = config['name']
        port = config['port']

        if not Path(script_path).exists():
            print(f"Script file not found: {script_path}")
            return False

        try:
            log_file = self.log_dir / f"{service_id}.log"
            f = open(log_file, 'w')
            process = subprocess.Popen(
                [sys.executable, script_path],
                stdout=f,
                stderr=subprocess.STDOUT,
                cwd=os.getcwd()
            )
            self.services[service_id] = {
                'process': process,
                'name': service_name,
                'port': port,
                'log_file': log_file,
                'stdout': f,
            }
            print(f"Started {service_name} (PID: {process.pid}, Port: {port})")
            return True
        except Exception as e:
            print(f"Failed to start {service_name}: {e}")
            return False

    def start_all(self):
        print("Starting MCP services (Upbit mode)...")
        for sid, cfg in self.service_configs.items():
            self.start_service(sid, cfg)

        time.sleep(2)
        print("Services running:")
        for sid, svc in self.services.items():
            print(f" - {svc['name']}: http://localhost:{svc['port']}  (log: {svc['log_file']})")

        print("Press Ctrl+C to stop.")
        self.keepalive()

    def keepalive(self):
        try:
            while self.running:
                time.sleep(1)
                for sid, svc in list(self.services.items()):
                    if svc['process'].poll() is not None:
                        print(f"{svc['name']} exited.")
                        self.running = False
                        break
        except KeyboardInterrupt:
            pass
        finally:
            self.stop_all_services()

    def stop_all_services(self):
        for sid, svc in self.services.items():
            try:
                svc['process'].terminate()
                svc['process'].wait(timeout=5)
            except Exception:
                pass
            try:
                svc['stdout'].close()
            except Exception:
                pass
        self.services.clear()


if __name__ == '__main__':
    manager = MCPServiceManager()
    manager.start_all()

