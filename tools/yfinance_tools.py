"""Custom Yfinance tools for market data and news retrieval."""

import yfinance as yf
from typing import Optional, Dict, List, Any
from datetime import datetime, timedelta


def get_stock_info(ticker: str) -> Dict[str, Any]:
    """
    Get comprehensive stock information for a given ticker.

    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')

    Returns:
        Dictionary containing stock information including current price,
        market cap, PE ratio, 52-week high/low, and more.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "ticker": ticker,
            "company_name": info.get("longName", "N/A"),
            "current_price": info.get("currentPrice", info.get("regularMarketPrice", "N/A")),
            "previous_close": info.get("previousClose", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "forward_pe": info.get("forwardPE", "N/A"),
            "dividend_yield": info.get("dividendYield", "N/A"),
            "52_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
            "52_week_low": info.get("fiftyTwoWeekLow", "N/A"),
            "volume": info.get("volume", "N/A"),
            "avg_volume": info.get("averageVolume", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
        }
    except Exception as e:
        return {"error": f"Failed to fetch data for {ticker}: {str(e)}"}


def get_stock_news(ticker: str, max_news: int = 10) -> List[Dict[str, Any]]:
    """
    Get latest news for a given stock ticker.

    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
        max_news: Maximum number of news articles to return (default: 10)

    Returns:
        List of news articles with title, publisher, link, and publish time.
    """
    try:
        stock = yf.Ticker(ticker)
        news = stock.news

        articles = []
        for article in news[:max_news]:
            articles.append({
                "title": article.get("title", "N/A"),
                "publisher": article.get("publisher", "N/A"),
                "link": article.get("link", "N/A"),
                "publish_time": datetime.fromtimestamp(article.get("providerPublishTime", 0)).strftime("%Y-%m-%d %H:%M:%S") if article.get("providerPublishTime") else "N/A",
                "type": article.get("type", "N/A"),
            })

        return articles
    except Exception as e:
        return [{"error": f"Failed to fetch news for {ticker}: {str(e)}"}]


def get_historical_data(ticker: str, period: str = "1mo", interval: str = "1d") -> Dict[str, Any]:
    """
    Get historical stock price data.

    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
        period: Time period (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', 'max')
        interval: Data interval (e.g., '1m', '5m', '15m', '1h', '1d', '1wk', '1mo')

    Returns:
        Dictionary containing historical price data and statistics.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)

        if hist.empty:
            return {"error": f"No historical data available for {ticker}"}

        return {
            "ticker": ticker,
            "period": period,
            "interval": interval,
            "data_points": len(hist),
            "latest_close": float(hist['Close'].iloc[-1]),
            "period_high": float(hist['High'].max()),
            "period_low": float(hist['Low'].min()),
            "period_avg_volume": float(hist['Volume'].mean()),
            "price_change": float(hist['Close'].iloc[-1] - hist['Close'].iloc[0]),
            "price_change_percent": float(((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100),
            "start_date": hist.index[0].strftime("%Y-%m-%d"),
            "end_date": hist.index[-1].strftime("%Y-%m-%d"),
        }
    except Exception as e:
        return {"error": f"Failed to fetch historical data for {ticker}: {str(e)}"}


def get_market_indices() -> Dict[str, Any]:
    """
    Get current information for major market indices.

    Returns:
        Dictionary containing data for major indices like S&P 500, Dow Jones, NASDAQ, etc.
    """
    indices = {
        "^GSPC": "S&P 500",
        "^DJI": "Dow Jones",
        "^IXIC": "NASDAQ",
        "^RUT": "Russell 2000",
        "^VIX": "VIX (Volatility Index)",
    }

    results = {}
    for ticker, name in indices.items():
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            hist = stock.history(period="5d")

            if not hist.empty:
                results[name] = {
                    "ticker": ticker,
                    "current_price": float(hist['Close'].iloc[-1]),
                    "previous_close": float(hist['Close'].iloc[-2]) if len(hist) > 1 else "N/A",
                    "change": float(hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) if len(hist) > 1 else "N/A",
                    "change_percent": float(((hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100) if len(hist) > 1 else "N/A",
                }
        except Exception as e:
            results[name] = {"error": f"Failed to fetch data: {str(e)}"}

    return results


def compare_stocks(tickers: List[str]) -> Dict[str, Any]:
    """
    Compare multiple stocks side by side.

    Args:
        tickers: List of stock ticker symbols to compare

    Returns:
        Dictionary containing comparison data for all tickers.
    """
    comparison = {}

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            hist = stock.history(period="3mo")

            if not hist.empty:
                comparison[ticker] = {
                    "company_name": info.get("longName", "N/A"),
                    "current_price": info.get("currentPrice", info.get("regularMarketPrice", "N/A")),
                    "market_cap": info.get("marketCap", "N/A"),
                    "pe_ratio": info.get("trailingPE", "N/A"),
                    "3mo_performance": float(((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100),
                    "volatility": float(hist['Close'].pct_change().std() * 100),
                    "sector": info.get("sector", "N/A"),
                }
        except Exception as e:
            comparison[ticker] = {"error": f"Failed to fetch data: {str(e)}"}

    return comparison
