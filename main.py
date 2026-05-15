from ingestion.data_loader import (
    MarketDataLoader
)

from processing.indicators import (
    IndicatorEngine
)

from detection.event_detector import (
    EventDetector
)

from config.thresholds import (
    MONITORED_STOCKS
)

loader = MarketDataLoader()

indicator_engine = (
    IndicatorEngine()
)

event_detector = (
    EventDetector()
)

for stock in MONITORED_STOCKS:

    print(
        f"\nProcessing {stock}"
    )

    data = loader.fetch_stock_data(
        stock
    )

    if data.empty:
        continue

    enriched_data = (
        indicator_engine
        .enrich_market_data(
            data
        )
    )

    for _, row in (
        enriched_data.iterrows()
    ):

        event = (
            event_detector
            .detect_market_events(
                row,
                stock
            )
        )

        if event:

            print(
                "\nALERT DETECTED"
            )

            print(
                f"Stock: "
                f"{event['stock']}"
            )

            print(
                f"Time: "
                f"{event['timestamp']}"
            )

            print(
                f"Events: "
                f"{event['events']}"
            )

            print(
                "-" * 50
            )