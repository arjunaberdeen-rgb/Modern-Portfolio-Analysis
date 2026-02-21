import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def perform_portfolio_analysis(input_file="ftse100_database.csv", risk_free_rate=0.04):
    """
    Analyzes the FTSE100 data and selects top 10 stocks using MPT principles.
    """
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Please run database.py first.")
        return

    # Load data
    # Note: yfinance multi-index CSV can be tricky to load. 
    # We assume 'Close' or 'Adj Close' is available.
    df = pd.read_csv(input_file, header=[0, 1], index_col=0, parse_dates=True)
    
    # Extract Adjusted Close prices
    adj_close = pd.DataFrame()
    for ticker in df.columns.levels[0]:
        if 'Adj Close' in df[ticker]:
            adj_close[ticker] = df[ticker]['Adj Close']
        elif 'Close' in df[ticker]:
            adj_close[ticker] = df[ticker]['Close']

    # 1. Calculate Daily Returns
    returns = adj_close.pct_change().dropna()

    # 2. Annualized Statistics
    stats = pd.DataFrame()
    stats['Annualized Return'] = returns.mean() * 252
    stats['Annualized Volatility'] = returns.std() * np.sqrt(252)
    
    # 3. Sharpe Ratio (Risk Adjusted Return)
    stats['Sharpe Ratio'] = (stats['Annualized Return'] - risk_free_rate) / stats['Annualized Volatility']
    
    # 4. Filter for stocks with sufficient data (avoiding recently listed or gaps)
    # Require at least 80% data coverage
    stats['Coverage'] = adj_close.count() / len(adj_close)
    stats = stats[stats['Coverage'] > 0.8]

    # 5. Sort by Sharpe Ratio to find top 10
    top_10 = stats.sort_values(by='Sharpe Ratio', ascending=False).head(10)
    
    print("\n--- Portfolio Manager's Top 10 FTSE 100 Recommendations ---")
    print(top_10[['Annualized Return', 'Annualized Volatility', 'Sharpe Ratio']])
    
    # Save recommendations
    top_10.to_csv("top_10_recommendations.csv")
    print("\nRecommendations saved to ML/top_10_recommendations.csv")
    
    # Simple Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(stats['Annualized Volatility'], stats['Annualized Return'], alpha=0.5, label='All FTSE 100')
    plt.scatter(top_10['Annualized Volatility'], top_10['Annualized Return'], color='red', label='Top 10 Picks')
    
    for i, txt in enumerate(top_10.index):
        plt.annotate(txt, (top_10['Annualized Volatility'].iloc[i], top_10['Annualized Return'].iloc[i]))

    plt.title('FTSE 100: Risk vs Return (Efficient Frontier Selection)')
    plt.xlabel('Annualized Volatility (Risk)')
    plt.ylabel('Annualized Return')
    plt.legend()
    plt.grid(True)
    plt.savefig('risk_return_plot.png')
    print("Risk-Return plot saved as risk_return_plot.png")

if __name__ == "__main__":
    perform_portfolio_analysis()
