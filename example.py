"""
Example usage of the AI Investment Agent Team
"""

import os
from dotenv import load_dotenv
from investment_team import create_investment_team

# Load environment variables
load_dotenv()


def run_example():
    """Run an example investment analysis."""

    # Check for API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  ERROR: ANTHROPIC_API_KEY not found!")
        print("Please create a .env file with your API key:")
        print("  ANTHROPIC_API_KEY=your-api-key-here")
        return

    # Create the investment team
    print("🤖 Creating AI Investment Agent Team...")
    team = create_investment_team()

    # Example queries
    queries = [
        "What's the current market outlook?",
        "Analyze AAPL and MSFT stocks",
        "Give me investment recommendations for tech stocks",
    ]

    # You can change this to any query you want
    query = queries[0]  # Use the first query

    print(f"\n{'='*80}")
    print(f"📊 INVESTMENT ANALYSIS")
    print(f"{'='*80}")
    print(f"Query: {query}")
    print(f"{'='*80}\n")

    # Run the analysis with streaming output
    team.print_response(query, stream=True)

    print(f"\n{'='*80}")
    print(f"✅ Analysis Complete!")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    run_example()
