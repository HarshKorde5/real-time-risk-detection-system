from rich.console import Console

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

from utils.replay_engine import (
    ReplayEngine
)

from config.thresholds import (
    MONITORED_STOCKS
)

console = Console()

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

replay_engine = (
    ReplayEngine(
        replay_speed=0.15
    )
)

console.print(
    "\n[bold green]"
    "================================="
)

console.print(
    "MARKET EVENT DETECTION SYSTEM"
)

console.print(
    "================================="
)

console.print(
    "[cyan]"
    "Mode: Simulated Real-Time"
)

console.print(
    "Monitoring Stocks:"
)

for stock in MONITORED_STOCKS:

    console.print(
        f"• {stock}"
    )

console.print("\n")

for stock in MONITORED_STOCKS:

    console.print(
        f"\n[bold blue]"
        f"Monitoring {stock}"
        f"[/bold blue]"
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

    for row in (
        replay_engine
        .stream_market_data(
            enriched_data
        )
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