# AI Investment Agent Team

A sophisticated multi-agent system for comprehensive investment analysis using the Agno framework and real-time market data from Yahoo Finance.

## Overview

This project implements a team of four AI agents that work together to provide detailed investment analysis and recommendations:

1. **Researcher Agent** - Fetches latest market data and news via Yfinance
2. **Analyst Agent** - Interprets data and drafts analytical insights
3. **Advisor Agent** - Suggests specific portfolio moves and strategies
4. **Reporter Agent** - Compiles comprehensive investment reports

## Features

- 🔍 **Real-time Market Data**: Fetches current stock prices, indices, and market information
- 📰 **Latest News**: Retrieves recent news articles for stocks and market sentiment
- 📊 **Technical Analysis**: Analyzes price trends, volatility, and performance metrics
- 💡 **Investment Insights**: Provides data-driven insights and trend analysis
- 🎯 **Actionable Recommendations**: Suggests specific buy/sell/hold actions with rationale
- 📝 **Professional Reports**: Generates comprehensive reports with Market Outlook, Key Assets, and Recommendations

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd cc-web-demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Usage

### Basic Usage

Run the investment team with a query:

```bash
python investment_team.py "Analyze AAPL, GOOGL, and MSFT"
```

### Example Queries

```bash
# Analyze specific stocks
python investment_team.py "What's the outlook for NVDA and AMD?"

# Market overview
python investment_team.py "Give me the current market outlook for tech stocks"

# Sector analysis
python investment_team.py "Analyze the semiconductor sector and recommend top picks"

# Comparative analysis
python investment_team.py "Compare TSLA with traditional automakers"
```

### Programmatic Usage

```python
from investment_team import create_investment_team

# Create the team
team = create_investment_team()

# Run analysis
response = team.run("Analyze AAPL and MSFT stock performance")
print(response.content)
```

## Project Structure

```
cc-web-demo/
├── agents/
│   ├── researcher.py    # Market data collection agent
│   ├── analyst.py       # Data analysis and insights agent
│   ├── advisor.py       # Investment recommendations agent
│   └── reporter.py      # Report compilation agent
├── tools/
│   └── yfinance_tools.py # Custom Yfinance tools and functions
├── investment_team.py    # Main orchestration file
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## Agent Responsibilities

### 1. Researcher Agent
- Fetches current stock prices and market indices
- Retrieves latest news articles
- Gathers historical price data
- Compares multiple stocks
- Provides raw market data to other agents

### 2. Analyst Agent
- Interprets market data and trends
- Identifies patterns and anomalies
- Analyzes technical indicators
- Considers macroeconomic factors
- Provides balanced, objective insights

### 3. Advisor Agent
- Formulates investment recommendations
- Suggests specific portfolio actions (Buy/Sell/Hold)
- Assesses risk levels
- Recommends position sizes
- Considers diversification and risk management

### 4. Reporter Agent
- Compiles comprehensive investment reports
- Structures information into clear sections:
  - Executive Summary
  - Market Outlook
  - Key Assets Analysis
  - Investment Recommendations
- Ensures professional formatting and clarity

## Report Structure

Each analysis generates a comprehensive report with:

### Executive Summary
- Quick overview of key findings and recommendations

### Market Outlook
- Current market conditions
- Major indices performance
- Market sentiment and trends
- Risk factors and opportunities

### Key Assets
- Highlighted stocks/sectors
- Performance metrics
- Recent news and developments
- Technical and fundamental analysis

### Recommendations
- Specific buy/sell/hold actions
- Rationale and supporting data
- Risk assessments
- Time horizons and price targets

## Technologies Used

- **[Agno](https://docs.agno.com)** - Multi-agent framework for Python
- **[Yfinance](https://pypi.org/project/yfinance/)** - Real-time financial data from Yahoo Finance
- **[Anthropic Claude](https://www.anthropic.com/claude)** - Advanced AI model (Claude Sonnet 4.5)
- **Python 3.8+** - Programming language

## Requirements

- Python 3.8 or higher
- Anthropic API key
- Internet connection for real-time market data

## Environment Variables

```bash
# Required
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Optional (if using OpenAI models)
OPENAI_API_KEY=your_openai_api_key_here
```

## Limitations & Disclaimers

⚠️ **Important**: This tool is for informational and educational purposes only.

- Not financial advice - consult a licensed financial advisor
- Past performance doesn't guarantee future results
- Market data may have delays or inaccuracies
- AI-generated analysis may contain errors
- Always do your own research before investing
- Consider your risk tolerance and financial situation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
- Create an issue on GitHub
- Check Agno documentation: https://docs.agno.com
- Review Yfinance documentation: https://pypi.org/project/yfinance/

## Acknowledgments

- Built with [Agno](https://docs.agno.com) framework
- Market data powered by [Yahoo Finance](https://finance.yahoo.com)
- AI models by [Anthropic](https://www.anthropic.com)
