"""Researcher Agent - Fetches latest market data and news via Yfinance."""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from tools.yfinance_tools import (
    get_stock_info,
    get_stock_news,
    get_historical_data,
    get_market_indices,
    compare_stocks,
)


def create_researcher_agent() -> Agent:
    """
    Create and return the Researcher agent.

    This agent is responsible for:
    - Fetching current market data for stocks and indices
    - Retrieving latest news for specific stocks
    - Getting historical price data and trends
    - Comparing multiple stocks
    """
    return Agent(
        name="Market Researcher",
        role="Fetch and gather latest market data, stock prices, news, and financial information",
        model=OpenAIChat(id="gpt-4"),
        tools=[
            get_stock_info,
            get_stock_news,
            get_historical_data,
            get_market_indices,
            compare_stocks,
        ],
        instructions=[
            "You are a market research specialist focused on gathering accurate and timely financial data.",
            "Always fetch data for major market indices to understand overall market sentiment.",
            "When researching stocks, gather comprehensive information including price data, news, and historical trends.",
            "Use the compare_stocks function when analyzing multiple stocks to provide comparative insights.",
            "Always include the latest news when researching specific stocks to capture market sentiment.",
            "Organize your findings clearly with proper categorization (market overview, stock analysis, news summary).",
            "Include data timestamps and sources in your research.",
        ],
        add_datetime_to_instructions=True,
        show_tool_calls=True,
        markdown=True,
    )
