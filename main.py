# main.py

from ingestion.data_loader import (
    MarketDataLoader
)

from processing.indicators import (
    IndicatorEngine
)

from config.thresholds import (
    MONITORED_STOCKS
)

loader = MarketDataLoader()

indicator_engine = (
    IndicatorEngine()
)

for stock in MONITORED_STOCKS:

    data = loader.fetch_stock_data(stock)

    if not data.empty:

        enriched_data = (
            indicator_engine
            .enrich_market_data(
                data
            )
        )

        loader.save_to_csv(
            enriched_data,
            stock
        )

        print(
            f"\nEnriched data for {stock}\n"
        )

        print(
            enriched_data[
                [
                    "timestamp",
                    "close",
                    "ma_short",
                    "ma_long",
                    "price_change_percent",
                    "volatility",
                    "volume_ratio"
                ]
            ].tail()
        )