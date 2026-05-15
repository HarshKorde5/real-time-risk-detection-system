import yfinance as yf
import pandas as pd
from rich.console import Console

console = Console()


class MarketDataLoader:

    def __init__(self):
        self.console = console

    def fetch_stock_data(
        self,
        ticker: str,
        period: str = "5d",
        interval: str = "5m"
    ) -> pd.DataFrame:

        try:
            self.console.print(
                f"[cyan]Fetching data for {ticker}...[/cyan]"
            )

            stock = yf.Ticker(ticker)

            df = stock.history(
                period=period,
                interval=interval
            )

            if df.empty:
                raise ValueError(
                    f"No data found for {ticker}"
                )

            df.reset_index(inplace=True)

            df = self.clean_market_data(df)

            self.console.print(
                f"[green]Fetched {len(df)} records "
                f"for {ticker}[/green]"
            )

            return df

        except Exception as e:
            self.console.print(
                f"[red]Error fetching {ticker}: {e}[/red]"
            )

            return pd.DataFrame()

    def clean_market_data(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        required_columns = [
            "Datetime",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]

        df = df[required_columns]

        df.dropna(inplace=True)

        df.rename(
            columns={
                "Datetime": "timestamp",
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume"
            },
            inplace=True
        )

        return df

    def save_to_csv(
        self,
        df: pd.DataFrame,
        ticker: str
    ):

        filename = (
            f"data/{ticker.replace('.', '_')}.csv"
        )

        df.to_csv(filename, index=False)

        self.console.print(
            f"[yellow]Saved to {filename}[/yellow]"
        )