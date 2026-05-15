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

from alerts.alert_manager import (
    AlertManager
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

alert_manager = (
    AlertManager()
)

for stock in MONITORED_STOCKS:

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

            alert_manager.process_alert(
                smart_alert
            )