import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

class MarketCharts:

    def plot_market_analysis(
        self,
        stock_name,
        df,
        detected_events
    ):

        fig, axes = plt.subplots(
            3,
            1,
            figsize=(16, 10),
            sharex=True
        )

        fig.suptitle(
            f"{stock_name} Market Analysis",
            fontsize=16
        )

        # -------------------------
        # PRICE + MOVING AVERAGES
        # -------------------------

        axes[0].plot(
            df["timestamp"],
            df["close"],
            label="Close Price"
        )

        axes[0].plot(
            df["timestamp"],
            df["ma_short"],
            label="MA5"
        )

        axes[0].plot(
            df["timestamp"],
            df["ma_long"],
            label="MA20"
        )

        event_times = []

        event_prices = []

        for event in detected_events:

            event_times.append(
                event["timestamp"]
            )

            matched_row = df[
                df["timestamp"]
                ==
                event["timestamp"]
            ]

            if not matched_row.empty:

                event_prices.append(
                    matched_row[
                        "close"
                    ].values[0]
                )

        axes[0].scatter(
            event_times,
            event_prices,
            marker="^",
            s=100,
            label="Detected Event"
        )

        axes[0].set_title(
            "Price & Trend Analysis"
        )

        axes[0].legend()

        # -------------------------
        # VOLATILITY
        # -------------------------

        axes[1].plot(
            df["timestamp"],
            df["volatility"]
        )

        axes[1].set_title(
            "Volatility Analysis"
        )

        # -------------------------
        # VOLUME RATIO
        # -------------------------

        axes[2].plot(
            df["timestamp"],
            df["volume_ratio"]
        )

        axes[2].axhline(
            y=2,
            linestyle="--"
        )

        axes[2].set_title(
            "Volume Spike Detection"
        )

        plt.tight_layout()

        plt.show()