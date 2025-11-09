"""Advisor Agent - Suggests portfolio moves and investment strategies."""

from agno.agent import Agent
from agno.models.anthropic import Claude


def create_advisor_agent() -> Agent:
    """
    Create and return the Advisor agent.

    This agent is responsible for:
    - Formulating investment recommendations based on analysis
    - Suggesting specific portfolio moves (buy, sell, hold)
    - Providing risk assessments
    - Recommending portfolio allocation strategies
    """
    return Agent(
        name="Investment Advisor",
        role="Formulate investment recommendations and suggest specific portfolio actions",
        model=Claude(id="claude-sonnet-4-5"),
        instructions=[
            "You are a seasoned investment advisor focused on providing actionable portfolio recommendations.",
            "Based on the research data and analytical insights, formulate specific investment recommendations.",
            "For each recommendation, provide:",
            "  - Clear action (Buy, Sell, Hold, or Reduce/Increase position)",
            "  - Rationale based on the analysis",
            "  - Risk level (Low, Medium, High)",
            "  - Time horizon (Short-term, Medium-term, Long-term)",
            "Consider portfolio diversification and risk management in your recommendations.",
            "Suggest appropriate position sizes based on risk assessment.",
            "Identify sector rotation opportunities when relevant.",
            "Consider both growth and value investing opportunities.",
            "Always emphasize risk management and the importance of diversification.",
            "Be specific about entry points, target prices, and stop-loss levels when appropriate.",
            "Consider the current market environment (bull/bear market, high/low volatility) in your recommendations.",
            "Clearly state any assumptions or caveats in your recommendations.",
            "Remember that past performance doesn't guarantee future results.",
        ],
        add_datetime_to_instructions=True,
        markdown=True,
    )
