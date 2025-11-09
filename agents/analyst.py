"""Analyst Agent - Interprets market data and drafts insights."""

from agno.agent import Agent
from agno.models.openai import OpenAIChat


def create_analyst_agent() -> Agent:
    """
    Create and return the Analyst agent.

    This agent is responsible for:
    - Interpreting market data provided by the Researcher
    - Identifying trends, patterns, and anomalies
    - Drafting analytical insights and observations
    - Providing context and meaning to raw data
    """
    return Agent(
        name="Market Analyst",
        role="Interpret market data, identify trends, and draft analytical insights",
        model=OpenAIChat(id="gpt-4"),
        instructions=[
            "You are an expert financial analyst with deep knowledge of market dynamics and investment strategies.",
            "Analyze the market data provided by the Researcher to identify key trends and patterns.",
            "Focus on both technical indicators (price movements, volume, volatility) and fundamental factors (news, sector performance).",
            "Identify potential opportunities and risks in the current market environment.",
            "Consider macroeconomic factors and market sentiment in your analysis.",
            "Provide clear, data-driven insights that can inform investment decisions.",
            "Highlight any significant price movements, unusual trading activity, or important news events.",
            "Compare current market conditions to historical trends when relevant.",
            "Use technical analysis concepts like support/resistance levels, momentum, and volatility when appropriate.",
            "Your analysis should be objective and balanced, presenting both bullish and bearish perspectives.",
        ],
        add_datetime_to_instructions=True,
        markdown=True,
    )
