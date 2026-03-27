# FAANG Stock Price Analyzer

Python tool for analyzing and visualizing FAANG stock performance (2013-2018).

## Overview

Automatically loads multiple stock CSV files, calculates daily returns, and generates professional financial charts using mplfinance.

## Features

- Automated CSV loading for multiple stocks
- Daily percentage return calculations
- Individual candlestick charts for each stock
- Multi-stock price comparison overlay
- Organized output directory with saved charts

## Tech Stack

- Python 3.x
- pandas - data manipulation
- matplotlib - visualization foundation
- mplfinance - financial charting

## Installation
```bash
pip install pandas matplotlib mplfinance
```

## Usage
```bash
python 1_src/main.py
```

Charts are automatically saved to `2_data/2_processed/`

## Project Structure
```
stock-price-analyzer/
├── 1_src/
│   └── main.py
├── 2_data/
│   ├── 1_raw/          # CSV files (AAPL, AMZN, FB, GOOGL, NFLX)
│   └── 2_processed/    # Generated charts
└── README.md
```

## Data

Historical daily stock prices (Open, High, Low, Close, Volume) from 2013-2018.

## Key Insights

- Amazon showed 400%+ growth over the period
- Google and Amazon significantly outperformed other FAANG stocks
- All stocks showed strong upward trends from 2016-2018

## Future Enhancements

- Volatility analysis and risk metrics
- Portfolio return calculations
- Interactive dashboards with Plotly
- Correlation analysis between stocks
