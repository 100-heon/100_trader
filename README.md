<div align="center">

# 🤖 AI-Trader Bench
### *Let AI Show Its Power in Financial Markets*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


**A revolutionary AI stock trading agent system that lets multiple large language models compete autonomously in the NASDAQ 100 stock pool!**

## 🏆 Current Championship Leaderboard

<div align="center">

### 🥇 **Last Update: 2025/10/22**

| 🏆 Rank | 🤖 AI Model | 📈 Total Earnings | 
|---------|-------------|----------------|
| **🥇 1st** | **DeepSeek** | 🚀 +9.03% | 
| 🥈 2nd | Claude-3.7 | 📊 +2.34% | 
| 🥉 3rd | GPT-5 | 📊 +1.22% | 

### 📊 **Live Performance Dashboard**
![rank](assets/rank.png)

*Daily tracking of AI models' performance in NASDAQ 100*

</div>


[🚀 Quick Start](#-quick-start) • [📈 Performance Analysis](#-performance-analysis) • [🛠️ Configuration Guide](#-configuration-guide) • [中文文档](README_CN.md)

</div>

---

## 🌟 Project Introduction

> **Imagine: 5 different AI models, each with unique investment strategies, competing autonomously in the same market, seeing who can make the most profit in NASDAQ 100!**

### 🎯 Core Features

- **🤖 Fully Autonomous Decision-Making**: AI agents make 100% autonomous analysis, decisions, and execution with zero human intervention
- **🛠️ Pure Tool-Driven**: Based on MCP toolchain, AI completes all trading operations through tool calls
- **🏆 Multi-Model Arena**: Run GPT, Claude, Qwen and other AI models for trading
- **📊 Real-time Performance Tracking**: Complete trading records, position changes and profit analysis
- **🔍 Intelligent Information Retrieval**: Integrated Jina search for latest market news and financial reports
- **⚡ MCP Toolchain**: Modular tool system based on Model Context Protocol
- **🔌 Pluggable Strategies**: Support for third-party strategies and custom AI agent integration
- **⏰ Replay Design**: Support for replaying any time period with automatic future information filtering

## 🚀 Project Overview

AI-Trader Bench is an innovative AI trading agent system that allows multiple large language models to compete in real stock trading environments. Each AI agent has:

### 🎮 Trading Environment
- **💰 Initial Capital**: $10,000 USD
- **📈 Trading Targets**: NASDAQ 100 component stocks (100 top tech stocks)
- **⏰ Trading Hours**: Weekday trading with historical replay support
- **📊 Data Sources**: Alpha Vantage API + Jina AI search
- **🔄 Time Control**: Support for historical replay of any time period and future information filtering

### 🧠 AI Agent Capabilities
- **📰 Intelligent Information Retrieval**: Automatically search market news, analyst reports, and autonomously filter information
- **💡 Pure AI Decision-Making**: Based on multi-dimensional analysis, AI makes buy/sell decisions completely autonomously
- **📝 Automatic Recording**: System automatically records detailed logs and position changes for each trade
- **🔄 Continuous Learning**: AI autonomously adjusts strategies based on market feedback

### 🏁 Competition Rules
Each AI model runs completely independently, using the same:
- **💰 Initial Capital**: $10,000 USD starting capital
- **📊 Market Data**: Same price data and information sources
- **⏰ Trading Hours**: Same trading time windows
- **📈 Evaluation Criteria**: Unified performance evaluation metrics
- **🛠️ Tool Set**: Same MCP toolchain

**🎯 Goal: See which AI model can achieve the highest investment return under complete autonomy!**

### 🚫 Zero Human Intervention
- ❌ **No Preset Strategies**: No preset trading strategies or rules provided
- ❌ **No Human Guidance**: AI relies completely on its own reasoning abilities for decisions
- ❌ **No Manual Intervention**: No human intervention allowed during trading process
- ✅ **Pure Tool-Driven**: AI completes all operations through tool calls
- ✅ **Autonomous Learning**: AI autonomously adjusts behavior based on market feedback

## ⏰ Replay Design

One of the core features of AI-Trader Bench is the **fully replayable** trading environment, ensuring that AI agent performance on historical data is scientific and reproducible.

### 🔄 Time Control Mechanism

#### 📅 Flexible Time Settings
```json
{
  "date_range": {
    "init_date": "2025-01-01",  // Any start date
    "end_date": "2025-01-31"    // Any end date
  }
}
```

#### 🛡️ Future Information Filtering
- **📊 Price Data**: Only provides price information for current date and earlier
- **📰 News Search**: Automatically filters news and announcements from future dates
- **📈 Financial Reports**: Only includes published financial data
- **🔍 Market Analysis**: Limited to information available at specified time points

### 🎯 Replay Advantages

#### 🔬 Scientific Research
- **📊 Market Efficiency Research**: Test AI performance under different market conditions
- **🧠 Cognitive Bias Analysis**: Study temporal consistency of AI decisions
- **📈 Risk Model Validation**: Verify effectiveness of risk management strategies

#### 🎯 Competition Fairness
- **🏆 Fair Competition**: All AI models use the same historical information
- **📊 Objective Evaluation**: Performance comparison based on same dataset
- **🔍 Transparency**: Completely reproducible experimental results

## 📁 Project Architecture

```
AI-Trader Bench/
├── 🤖 Core System
│   ├── main.py    # 🎯 Main program entry
│   ├── agent/base_agent/          # 🧠 AI agent core
│   └── configs/                   # ⚙️ Configuration files
│
├── 🛠️ MCP Toolchain
│   ├── agent_tools/
│   │   ├── tool_trade.py          # 💰 Trade execution
│   │   ├── tool_get_price_local.py # 📊 Price queries
│   │   ├── tool_jina_search.py   # 🔍 Information search
│   │   └── tool_math.py           # 🧮 Mathematical calculations
│   └── tools/                     # 🔧 Auxiliary tools
│
├── 📊 Data System
│   ├── data/
│   │   ├── daily_prices_*.json    # 📈 Stock price data
│   │   ├── merged.jsonl           # 🔄 Unified data format
│   │   └── agent_data/            # 📝 AI trading records
│   └── calculate_performance.py   # 📈 Performance analysis
│
├── 🎨 Frontend Interface
│   └── frontend/                  # 🌐 Web dashboard
│
└── 📋 Configuration & Documentation
    ├── configs/                   # ⚙️ System configuration
    ├── prompts/                   # 💬 AI prompts
    └── calc_perf.sh              # 🚀 Performance calculation script
```

### 🔧 Core Components Details

#### 🎯 Main Program (`main.py`)
- **Multi-Model Concurrency**: Run multiple AI models simultaneously for trading
- **Configuration Management**: Support for JSON configuration files and environment variables
- **Date Management**: Flexible trading calendar and date range settings
- **Error Handling**: Comprehensive exception handling and retry mechanisms

#### 🛠️ MCP Toolchain
| Tool | Function | API |
|------|----------|-----|
| **Trading Tool** | Buy/sell stocks, position management | `buy()`, `sell()` |
| **Price Tool** | Real-time and historical price queries | `get_price_local()` |
| **Search Tool** | Market information search | `get_information()` |
| **Math Tool** | Financial calculations and analysis | Basic mathematical operations |

#### 📊 Data System
- **📈 Price Data**: Complete OHLCV data for NASDAQ 100 component stocks
- **📝 Trading Records**: Detailed trading history for each AI model
- **📊 Performance Metrics**: Sharpe ratio, maximum drawdown, annualized returns, etc.
- **🔄 Data Synchronization**: Automated data acquisition and update mechanisms

## 🚀 Quick Start

### 📋 Prerequisites

- **Python 3.8+** 
- **API Keys**: OpenAI, Alpha Vantage, Jina AI

### ⚡ One-Click Installation

```bash
# 1. Clone project
git clone https://github.com/HKUDS/AI-Trader.git
cd AI-Trader

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env
# Edit .env file and fill in your API keys
```

### 🔑 Environment Configuration

Create `.env` file and configure the following variables:

```bash
# 🤖 AI Model API Configuration
OPENAI_API_BASE=https://your-openai-proxy.com/v1
OPENAI_API_KEY=your_openai_key

# 📊 Data Source Configuration
ALPHAADVANTAGE_API_KEY=your_alpha_vantage_key
JINA_API_KEY=your_jina_api_key

# ⚙️ System Configuration
RUNTIME_ENV_PATH=./runtime_env.json # Recommended to use absolute path

# 🌐 Service Port Configuration
MATH_HTTP_PORT=8000
SEARCH_HTTP_PORT=8001
TRADE_HTTP_PORT=8002
GETPRICE_HTTP_PORT=8003
# 🧠 AI Agent Configuration
AGENT_MAX_STEP=30             # Maximum reasoning steps
```

### 📦 Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# Or manually install core dependencies
pip install langchain langchain-openai langchain-mcp-adapters fastmcp python-dotenv requests numpy pandas
```

## 🎮 Running Guide

### 📊 Step 1: Data Preparation (`./fresh_data.sh`)

```bash
# 📈 Get NASDAQ 100 stock data
cd data
python get_daily_price.py

# 🔄 Merge data into unified format
python merge_jsonl.py
```

### 🛠️ Step 2: Start MCP Services

```bash
cd ./agent_tools
python start_mcp_services.py
```

### 🚀 Step 3: Start AI Arena

```bash
# 🎯 Run main program - let AIs start trading!
python main.py

# 🎯 Or use custom configuration
python main.py configs/my_config.json
```

### ⏰ Time Settings Example

#### 📅 Create Custom Time Configuration
```json
{
  "agent_type": "BaseAgent",
  "date_range": {
    "init_date": "2024-01-01",  // Backtest start date
    "end_date": "2024-03-31"     // Backtest end date
  },
  "models": [
    {
      "name": "claude-3.7-sonnet",
      "basemodel": "anthropic/claude-3.7-sonnet",
      "signature": "claude-3.7-sonnet",
      "enabled": true
    }
  ]
}
```

### 📈 Start Web Interface

```bash
cd docs
python3 -m http.server 8000
# Visit http://localhost:8000
```

## 📈 Performance Analysis

### 🏆 Competition Rules

| Rule Item | Setting | Description |
|-----------|---------|-------------|
| **💰 Initial Capital** | $10,000 | Starting capital for each AI model |
| **📈 Trading Targets** | NASDAQ 100 | 100 top tech stocks |
| **⏰ Trading Hours** | Weekdays | Monday to Friday |
| **💲 Price Benchmark** | Opening Price | Trade using daily opening price |
| **📝 Recording Method** | JSONL Format | Complete trading history records |

## ⚙️ Configuration Guide

### 📋 Configuration File Structure

```json
{
  "agent_type": "BaseAgent",
  "date_range": {
    "init_date": "2025-01-01",
    "end_date": "2025-01-31"
  },
  "models": [
    {
      "name": "claude-3.7-sonnet",
      "basemodel": "anthropic/claude-3.7-sonnet",
      "signature": "claude-3.7-sonnet",
      "enabled": true
    }
  ],
  "agent_config": {
    "max_steps": 30,
    "max_retries": 3,
    "base_delay": 1.0,
    "initial_cash": 10000.0
  },
  "log_config": {
    "log_path": "./data/agent_data"
  }
}
```

### 🔧 Configuration Parameters

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `agent_type` | AI agent type | "BaseAgent" |
| `max_steps` | Maximum reasoning steps | 30 |
| `max_retries` | Maximum retry attempts | 3 |
| `base_delay` | Operation delay (seconds) | 1.0 |
| `initial_cash` | Initial capital | $10,000 |

### 📊 Data Format

#### 💰 Position Records (position.jsonl)
```json
{
  "date": "2025-01-20",
  "id": 1,
  "this_action": {
    "action": "buy",
    "symbol": "AAPL", 
    "amount": 10
  },
  "positions": {
    "AAPL": 10,
    "MSFT": 0,
    "CASH": 9737.6
  }
}
```

#### 📈 Price Data (merged.jsonl)
```json
{
  "Meta Data": {
    "2. Symbol": "AAPL",
    "3. Last Refreshed": "2025-01-20"
  },
  "Time Series (Daily)": {
    "2025-01-20": {
      "1. buy price": "255.8850",
      "2. high": "264.3750", 
      "3. low": "255.6300",
      "4. sell price": "262.2400",
      "5. volume": "90483029"
    }
  }
}
```

### 📁 File Structure

```
data/agent_data/
├── claude-3.7-sonnet/
│   ├── position/
│   │   └── position.jsonl      # 📝 Position records
│   └── log/
│       └── 2025-01-20/
│           └── log.jsonl       # 📊 Trading logs
├── gpt-4o/
│   └── ...
└── qwen3-max/
    └── ...
```

## 🔌 Third-Party Strategy Integration

AI-Trader Bench adopts a modular design, supporting easy integration of third-party strategies and custom AI agents.

### 🛠️ Integration Methods

#### 1. Custom AI Agent
```python
# Create new AI agent class
class CustomAgent(BaseAgent):
    def __init__(self, model_name, **kwargs):
        super().__init__(model_name, **kwargs)
        # Add custom logic
```

#### 2. Register New Agent
```python
# Register in main.py
AGENT_REGISTRY = {
    "BaseAgent": {
        "module": "agent.base_agent.base_agent",
        "class": "BaseAgent"
    },
    "CustomAgent": {  # New addition
        "module": "agent.custom.custom_agent",
        "class": "CustomAgent"
    },
}
```

#### 3. Configuration File Settings
```json
{
  "agent_type": "CustomAgent",
  "models": [
    {
      "name": "your-custom-model",
      "basemodel": "your/model/path",
      "signature": "custom-signature",
      "enabled": true
    }
  ]
}
```

### 🔧 Extending Toolchain

#### Adding Custom Tools
```python
# Create new MCP tool
@mcp.tools()
class CustomTool:
    def __init__(self):
        self.name = "custom_tool"
    
    def execute(self, params):
        # Implement custom tool logic
        return result
```

## 🚀 Roadmap

### 🌟 Future Plans
- [ ] **🇨🇳 A-Share Support** - Extend to Chinese stock market
- [ ] **📊 Post-Market Statistics** - Automatic profit analysis
- [ ] **🔌 Strategy Marketplace** - Add third-party strategy sharing platform
- [ ] **🎨 Cool Frontend Interface** - Modern web dashboard
- [ ] **₿ Cryptocurrency** - Support digital currency trading
- [ ] **📈 More Strategies** - Technical analysis, quantitative strategies
- [ ] **⏰ Advanced Replay** - Support minute-level time precision and real-time replay
- [ ] **🔍 Smart Filtering** - More precise future information detection and filtering

## 🤝 Contributing Guide

We welcome contributions of all kinds! Especially AI trading strategies and agent implementations.

### 🧠 AI Strategy Contributions
- **🎯 Trading Strategies**: Contribute your AI trading strategy implementations
- **🤖 Custom Agents**: Implement new AI agent types
- **📊 Analysis Tools**: Add new market analysis tools
- **🔍 Data Sources**: Integrate new data sources and APIs

### 🐛 Issue Reporting
- Use GitHub Issues to report bugs
- Provide detailed reproduction steps
- Include system environment information

### 💡 Feature Suggestions
- Propose new feature ideas in Issues
- Describe use cases in detail
- Discuss implementation approaches

### 🔧 Code Contributions
1. Fork the project
2. Create a feature branch
3. Implement your strategy or feature
4. Add test cases
5. Create a Pull Request

### 📚 Documentation Improvements
- Improve README documentation
- Add code comments
- Write usage tutorials
- Contribute strategy documentation

### 🏆 Strategy Sharing
- **📈 Technical Analysis Strategies**: AI strategies based on technical indicators
- **📊 Quantitative Strategies**: Multi-factor models and quantitative analysis
- **🔍 Fundamental Strategies**: Analysis strategies based on financial data
- **🌐 Macro Strategies**: Strategies based on macroeconomic data

## 📞 Support & Community

- **💬 Discussions**: [GitHub Discussions](https://github.com/HKUDS/AI-Trader/discussions)
- **🐛 Issues**: [GitHub Issues](https://github.com/HKUDS/AI-Trader/issues)
- **📧 Contact**: your-email@example.com

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgments

Thanks to the following open source projects and services:
- [LangChain](https://github.com/langchain-ai/langchain) - AI application development framework
- [MCP](https://github.com/modelcontextprotocol) - Model Context Protocol
- [Alpha Vantage](https://www.alphavantage.co/) - Financial data API
- [Jina AI](https://jina.ai/) - Information search service

---

<div align="center">

**🌟 If this project helps you, please give us a Star!**

[![GitHub stars](https://img.shields.io/github/stars/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)
[![GitHub forks](https://img.shields.io/github/forks/HKUDS/AI-Trader?style=social)](https://github.com/HKUDS/AI-Trader)

**🤖 Let AI show its power in financial markets with complete autonomous decision-making!**  
**🛠️ Pure tool-driven, zero human intervention, a true AI trading arena!** 🚀

</div>
