import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import mplfinance as mpf

# Display settings

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)

# Paths
root = Path(__file__).parent.parent
processed_dir = root / '2_data' / '2_processed'


# Auto-loader: load ALL CSVs in 2_data/1_raw
def load_all_stocks():
    data_dir = root / '2_data' / '1_raw'
    csv_files = list(data_dir.glob('*.csv'))

    stocks = {}

    for file in csv_files:
        ticker = file.stem  # filename without .csv
        df = pd.read_csv(file)

        df['date'] = pd.to_datetime(df['date'])
        df['Daily_Return'] = df['close'].pct_change() * 100
        df = df.set_index('date')
        df.index.name = None

        stocks[ticker] = df

    return stocks

# Load all stocks

stocks = load_all_stocks()

# Pick a main ticker (AAPL if available)

main_ticker = 'AAPL' if 'AAPL' in stocks else list(stocks.keys())[0]
df_main = stocks[main_ticker]

# Generate a mplfinance chart for EVERY stock

for ticker, df in stocks.items():
    print(f"\nGenerating chart for {ticker}...")

    mpf.plot(
        df,   # or df for full history
        type='line',
        style='binance',
        ylabel='Price ($)',
        savefig=str(processed_dir / f"{ticker}_chart.png")
    )

# Multi-stock comparison (line chart)

plt.figure(figsize=(12, 6))

for ticker, df in stocks.items():
    plt.plot(df.index, df['close'], label=ticker)

plt.legend()
plt.grid(True)
plt.title('FAANG Stock Price Chart 2013-2018')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.show()