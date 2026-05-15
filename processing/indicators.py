import pandas as pd

from config.thresholds import (
    THRESHOLDS
)


class IndicatorEngine:

    def __init__(self):

        self.short_window = (
            THRESHOLDS[
                "SHORT_MOVING_AVERAGE"
            ]
        )

        self.long_window = (
            THRESHOLDS[
                "LONG_MOVING_AVERAGE"
            ]
        )

    def calculate_moving_averages(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        df["ma_short"] = (
            df["close"]
            .rolling(
                window=self.short_window
            )
            .mean()
        )

        df["ma_long"] = (
            df["close"]
            .rolling(
                window=self.long_window
            )
            .mean()
        )

        return df

    def calculate_price_change(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        df["price_change_percent"] = (
            df["close"]
            .pct_change()
            * 100
        )

        return df

    def calculate_volatility(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        df["volatility"] = (
            df["close"]
            .rolling(window=10)
            .std()
        )

        return df

    def calculate_volume_metrics(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        df["avg_volume"] = (
            df["volume"]
            .rolling(window=10)
            .mean()
        )

        df["volume_ratio"] = (
            df["volume"]
            / df["avg_volume"]
        )

        return df

    def enrich_market_data(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        df = self.calculate_moving_averages(df)

        df = self.calculate_price_change(df)

        df = self.calculate_volatility(df)

        df = self.calculate_volume_metrics(df)

        df.dropna(inplace=True)

        return df