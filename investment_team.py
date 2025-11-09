"""
AI Investment Agent Team
=========================

A multi-agent system for comprehensive investment analysis using Agno framework.

Team Structure:
- Researcher: Fetches latest market data and news via Yfinance
- Analyst: Interprets data and drafts insights
- Advisor: Suggests portfolio moves and strategies
- Reporter: Compiles comprehensive investment report

Usage:
    python investment_team.py "Analyze AAPL, GOOGL, and MSFT"
    python investment_team.py "What's the market outlook for tech stocks?"
"""

import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agents.researcher import create_researcher_agent
from agents.analyst import create_analyst_agent
from agents.advisor import create_advisor_agent
from agents.reporter import create_reporter_agent

# Load environment variables
load_dotenv()


def create_investment_team() -> Team:
    """
    Create and configure the Investment Agent Team.

    Returns:
        Configured Team instance with all four agents.
    """
    # Create all agents
    researcher = create_researcher_agent()
    analyst = create_analyst_agent()
    advisor = create_advisor_agent()
    reporter = create_reporter_agent()

    # Create the team with coordinate mode for collaborative work
    investment_team = Team(
        name="AI Investment Analysis Team",
        members=[researcher, analyst, advisor, reporter],
        mode="coordinate",  # Agents work together in a coordinated fashion
        model=OpenAIChat(id="gpt-4"),
        instructions=[
            "You are leading a team of investment professionals to provide comprehensive market analysis and recommendations.",
            "",
            "Team workflow:",
            "1. The Market Researcher gathers all relevant market data, stock information, and news",
            "2. The Market Analyst interprets the data and identifies trends, patterns, and insights",
            "3. The Investment Advisor formulates specific recommendations based on the analysis",
            "4. The Investment Reporter compiles everything into a comprehensive report",
            "",
            "Ensure thorough coverage of:",
            "- Current market conditions and sentiment",
            "- Specific stocks or sectors mentioned in the query",
            "- Relevant news and developments",
            "- Technical and fundamental analysis",
            "- Risk assessment",
            "- Actionable recommendations",
            "",
            "The final output should be a well-structured report with:",
            "- Executive Summary",
            "- Market Outlook",
            "- Key Assets Analysis",
            "- Investment Recommendations",
            "",
            "Coordinate the team to work efficiently and produce high-quality investment insights.",
        ],
        show_tool_calls=True,
        markdown=True,
    )

    return investment_team


def analyze_investment(query: str, stream: bool = True) -> str:
    """
    Run investment analysis on a given query.

    Args:
        query: Investment analysis request (e.g., "Analyze AAPL and MSFT")
        stream: Whether to stream the response (default: True)

    Returns:
        Analysis result as a string
    """
    team = create_investment_team()

    print(f"\n{'='*80}")
    print(f"AI INVESTMENT ANALYSIS TEAM")
    print(f"{'='*80}")
    print(f"Query: {query}")
    print(f"{'='*80}\n")

    # Run the team analysis
    if stream:
        team.print_response(query, stream=True)
        return ""
    else:
        response = team.run(query)
        return response.content


def main():
    """Main entry point for the investment team."""
    import sys

    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please set your API key in a .env file or environment variable.")
        print("Example: export OPENAI_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Get query from command line or use default
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        # Default query for demonstration
        query = "Analyze the current market outlook and provide recommendations for AAPL, MSFT, and NVDA"

    # Run the analysis
    analyze_investment(query, stream=True)


if __name__ == "__main__":
    main()
