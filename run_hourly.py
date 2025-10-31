import os
import sys
import time
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv


def sleep_until_next_hour():
    now = datetime.now()
    next_hour = (now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1))
    sleep_secs = (next_hour - now).total_seconds()
    time.sleep(max(1, int(sleep_secs)))


def main():
    # Ensure .env is loaded from repo root
    repo_dir = Path(__file__).parent
    load_dotenv(repo_dir / ".env")

    # Force today-only, include weekends for Upbit
    os.environ.setdefault("USE_TODAY", "true")
    os.environ.setdefault("ONLY_TODAY", "true")
    os.environ.setdefault("INCLUDE_WEEKENDS", "true")
    # Default bar to 60 minutes if not specified
    os.environ.setdefault("UPBIT_BAR_MINUTES", "60")

    py = sys.executable
    script = str(repo_dir / "main.py")

    print("[runner] Hourly runner started. Using 60min bars. Press Ctrl+C to stop.")

    try:
        while True:
            start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[runner] Starting cycle at {start}")
            try:
                subprocess.run([py, script], check=False)
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"[runner] Error running main.py: {e}")

            print("[runner] Sleeping until next hour ...")
            sleep_until_next_hour()
    except KeyboardInterrupt:
        print("[runner] Stopped by user.")


if __name__ == "__main__":
    main()

