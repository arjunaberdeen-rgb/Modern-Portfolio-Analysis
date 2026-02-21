# Modern Portfolio Analysis Process

This document outlines the quantitative framework used to analyze the FTSE 100 and select the top 10 stocks for an optimized investment portfolio.

## 1. Data Acquisition & Cleaning
We use historical daily adjusted closing prices. Adjusted prices are critical as they account for dividends and stock splits, providing a true total return.

Source: Yahoo Finance
Universe: FTSE 100 (current constituents)
Timeframe: 2020-01-01 to 2026-01-01

## 2. Statistical Metric Calculation
For each stock, we calculate:

Daily Returns: Percentage change in price.
Expected Annualized Return: The mean daily return multiplied by 252 (trading days).
Annualized Volatility (Risk): The standard deviation of daily returns multiplied by $\sqrt{252}$.

## 3. Risk-Adjusted Performance (Sharpe Ratio)
The core of our selection is the Sharpe Ratio, which measures the excess return per unit of deviation in an investment asset. Sharpe = Rp  -  Rfp , 
   Rp is the portfolio return,  Rf  is the risk-free rate, and p is the volatility.

## 4. Fundamental & Momentum Screening
Beyond raw MPT, we look for:

Maximum Drawdown: Assessing the worst-case historical loss.
Beta: Understanding how the stock moves relative to the FTSE 100 index.

## 5. Portfolio Optimization
Using the Mean-Variance Optimization (Markowitz Model), we identify stocks that offer the best "Efficient Frontier" placement—maximizing return for a given level of risk.

## 6. Final Selection
The top 10 stocks are selected based on the highest Sharpe Ratios, ensuring sector diversification to mitigate idiosyncratic risk.

