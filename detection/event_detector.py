import pandas as pd

from config.thresholds import (
    THRESHOLDS
)


class EventDetector:

    def __init__(self):

        self.price_threshold = (
            THRESHOLDS[
                "PRICE_SPIKE_PERCENT"
            ]
        )

        self.volume_multiplier = (
            THRESHOLDS[
                "VOLUME_SPIKE_MULTIPLIER"
            ]
        )

        self.volatility_threshold = (
            THRESHOLDS[
                "VOLATILITY_THRESHOLD"
            ]
        )

    def detect_price_spike(
        self,
        row
    ):

        return abs(
            row[
                "price_change_percent"
            ]
        ) > self.price_threshold

    def detect_volume_spike(
        self,
        row
    ):

        return (
            row["volume_ratio"]
            > self.volume_multiplier
        )

    def detect_trend_reversal(
        self,
        row
    ):

        return (
            row["ma_short"]
            > row["ma_long"]
        )

    def detect_high_volatility(
        self,
        row
    ):

        return (
            row["volatility"]
            > self.volatility_threshold
        )

    def detect_market_events(
        self,
        row: pd.Series,
        stock: str
    ):

        detected_events = []

        if self.detect_price_spike(
            row
        ):
            detected_events.append(
                "PRICE_BREAKOUT"
            )

        if self.detect_volume_spike(
            row
        ):
            detected_events.append(
                "VOLUME_SPIKE"
            )

        if self.detect_trend_reversal(
            row
        ):
            detected_events.append(
                "TREND_REVERSAL"
            )

        if self.detect_high_volatility(
            row
        ):
            detected_events.append(
                "HIGH_VOLATILITY"
            )

        if not detected_events:
            return None

        return {
            "stock": stock,
            "timestamp": row[
                "timestamp"
            ],
            "events": detected_events
        }