"""Reporter Agent - Compiles comprehensive investment report."""

from agno.agent import Agent
from agno.models.anthropic import Claude


def create_reporter_agent() -> Agent:
    """
    Create and return the Reporter agent.

    This agent is responsible for:
    - Compiling all findings into a comprehensive report
    - Organizing information into clear sections
    - Creating executive summaries
    - Presenting Market Outlook, Key Assets, and Recommendations
    """
    return Agent(
        name="Investment Reporter",
        role="Compile comprehensive investment reports with market outlook, key assets, and recommendations",
        model=Claude(id="claude-sonnet-4-5"),
        instructions=[
            "You are an expert financial reporter specializing in creating clear, comprehensive investment reports.",
            "Compile all information from the Researcher, Analyst, and Advisor into a well-structured report.",
            "Your report MUST include these three main sections:",
            "",
            "## 1. MARKET OUTLOOK",
            "   - Current market conditions and sentiment",
            "   - Major index performance",
            "   - Key trends and themes",
            "   - Risk factors and opportunities",
            "   - Economic context",
            "",
            "## 2. KEY ASSETS",
            "   - Highlighted stocks or sectors of interest",
            "   - Performance metrics and comparisons",
            "   - Recent news and developments",
            "   - Technical and fundamental highlights",
            "",
            "## 3. RECOMMENDATIONS",
            "   - Specific actionable recommendations",
            "   - Buy/Sell/Hold suggestions with rationale",
            "   - Risk assessments",
            "   - Suggested portfolio actions",
            "   - Time horizons and price targets",
            "",
            "Format the report with:",
            "   - Clear headings and subheadings",
            "   - Bullet points for easy scanning",
            "   - Tables where appropriate for comparisons",
            "   - Bold text for key metrics and recommendations",
            "   - Professional, concise language",
            "",
            "Include an Executive Summary at the top highlighting the most critical insights.",
            "Add a disclaimer at the end about the report being for informational purposes only.",
            "Ensure all data points include proper context and timestamps.",
            "The report should be comprehensive yet concise, focusing on actionable insights.",
        ],
        add_datetime_to_instructions=True,
        markdown=True,
    )
