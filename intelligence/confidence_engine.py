class ConfidenceEngine:

    def evaluate_confidence(
        self,
        events
    ):

        signal_count = len(events)

        if signal_count >= 3:
            return "HIGH"

        if signal_count == 2:
            return "MEDIUM"

        return "LOW"

    def calculate_risk_level(
        self,
        events
    ):

        if (
            "HIGH_VOLATILITY"
            in events
        ):
            return "HIGH"

        if len(events) >= 3:
            return "MEDIUM"

        return "LOW"

    def generate_recommendation(
        self,
        confidence
    ):

        recommendations = {

            "HIGH":
                "WATCH CLOSELY",

            "MEDIUM":
                "MONITOR",

            "LOW":
                "OBSERVE"
        }

        return recommendations[
            confidence
        ]

    def enrich_alert(
        self,
        event_data
    ):

        confidence = (
            self.evaluate_confidence(
                event_data["events"]
            )
        )

        risk = (
            self.calculate_risk_level(
                event_data["events"]
            )
        )

        recommendation = (
            self
            .generate_recommendation(
                confidence
            )
        )

        event_data[
            "confidence"
        ] = confidence

        event_data[
            "risk_level"
        ] = risk

        event_data[
            "recommendation"
        ] = recommendation

        return event_data