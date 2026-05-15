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

from visualization.charts import (
    MarketCharts
)

from config.thresholds import (
    MONITORED_STOCKS
)

def main():
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

    chart_engine = (
        MarketCharts()
    )

    selected_chart_stock = (
        "TSLA"
    )
    
    total_alerts = 0
    high_alerts = 0
    medium_alerts = 0
    low_alerts = 0

    detected_events = []

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

        stock_events = []

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
                
                total_alerts += 1
                
                if (
                    smart_alert[
                        "confidence"
                    ] == "HIGH"
                ):
                    high_alerts += 1

                elif (
                    smart_alert[
                        "confidence"
                    ] == "MEDIUM"
                ):
                    medium_alerts += 1

                else:
                    low_alerts += 1
                    
                
                alert_manager.process_alert(
                    smart_alert
                )

                stock_events.append(
                    smart_alert
                )

        if stock == selected_chart_stock:

            chart_engine.plot_market_analysis(
                stock,
                enriched_data,
                stock_events
            )
            
    console.print(
        "\n[bold green]"
        "================================="
    )

    console.print(
        "MONITORING SUMMARY"
    )

    console.print(
        "================================="
    )

    console.print(
        f"Stocks Monitored: "
        f"{len(MONITORED_STOCKS)}"
    )

    console.print(
        f"Total Alerts: "
        f"{total_alerts}"
    )

    console.print(
        f"High Confidence: "
        f"{high_alerts}"
    )

    console.print(
        f"Medium Confidence: "
        f"{medium_alerts}"
    )

    console.print(
        f"Low Confidence: "
        f"{low_alerts}"
    )

    console.print(
        "================================="
    )
        
        
        
        
        
if __name__ == "__main__":
    main()