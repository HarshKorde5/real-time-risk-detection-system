from ingestion.data_loader import (
    MarketDataLoader
)

from processing.indicators import (
    IndicatorEngine
)

from detection.event_detector import (
    EventDetector
)

from intelligence.confidence_engine import (
    ConfidenceEngine
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

confidence_engine = (
    ConfidenceEngine()
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

            smart_alert = (
                confidence_engine
                .enrich_alert(
                    event
                )
            )

            print(
                "\nMARKET ALERT"
            )

            print(
                f"Stock: "
                f"{smart_alert['stock']}"
            )

            print(
                f"Time: "
                f"{smart_alert['timestamp']}"
            )

            print(
                f"Events: "
                f"{smart_alert['events']}"
            )

            print(
                f"Confidence: "
                f"{smart_alert['confidence']}"
            )

            print(
                f"Risk Level: "
                f"{smart_alert['risk_level']}"
            )

            print(
                f"Recommendation: "
                f"{smart_alert['recommendation']}"
            )

            print(
                "-" * 50
            )