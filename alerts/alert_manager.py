import csv
import os

from rich.console import Console
from rich.panel import Panel
from rich.table import Table


class AlertManager:

    def __init__(self):

        self.console = Console()

        self.log_file = (
            "logs/alert_logs.csv"
        )

        self.initialize_logs()

    def initialize_logs(self):

        os.makedirs(
            "logs",
            exist_ok=True
        )

        if not os.path.exists(
            self.log_file
        ):

            with open(
                self.log_file,
                "w",
                newline=""
            ) as file:

                writer = csv.writer(
                    file
                )

                writer.writerow(
                    [
                        "timestamp",
                        "stock",
                        "events",
                        "confidence",
                        "risk_level",
                        "recommendation"
                    ]
                )

    def get_alert_color(
        self,
        confidence
    ):

        colors = {
            "HIGH": "red",
            "MEDIUM": "yellow",
            "LOW": "cyan"
        }

        return colors.get(
            confidence,
            "white"
        )

    def display_alert(
        self,
        alert_data
    ):

        color = (
            self.get_alert_color(
                alert_data[
                    "confidence"
                ]
            )
        )

        table = Table(
            show_header=False
        )

        table.add_row(
            "Stock",
            alert_data["stock"]
        )

        table.add_row(
            "Time",
            str(
                alert_data[
                    "timestamp"
                ]
            )
        )

        table.add_row(
            "Events",
            ", ".join(
                alert_data[
                    "events"
                ]
            )
        )

        table.add_row(
            "Confidence",
            alert_data[
                "confidence"
            ]
        )

        table.add_row(
            "Risk",
            alert_data[
                "risk_level"
            ]
        )

        table.add_row(
            "Recommendation",
            alert_data[
                "recommendation"
            ]
        )

        panel = Panel(
            table,
            title=(
                f"{alert_data['confidence']} "
                f"CONFIDENCE ALERT"
            ),
            border_style=color
        )

        self.console.print(
            panel
        )

    def log_alert(
        self,
        alert_data
    ):

        with open(
            self.log_file,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(
                file
            )

            writer.writerow(
                [
                    alert_data[
                        "timestamp"
                    ],
                    alert_data[
                        "stock"
                    ],
                    ", ".join(
                        alert_data[
                            "events"
                        ]
                    ),
                    alert_data[
                        "confidence"
                    ],
                    alert_data[
                        "risk_level"
                    ],
                    alert_data[
                        "recommendation"
                    ]
                ]
            )

    def process_alert(
        self,
        alert_data
    ):

        self.log_alert(
            alert_data
        )
        
        if(alert_data["confidence"] == "LOW"): return
                
        self.display_alert(
            alert_data
        )
