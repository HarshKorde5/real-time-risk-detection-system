import time
import pandas as pd


class ReplayEngine:

    def __init__(
        self,
        replay_speed=0.15
    ):

        self.replay_speed = (
            replay_speed
        )

    def stream_market_data(
        self,
        df: pd.DataFrame
    ):

        for _, row in (
            df.iterrows()
        ):

            yield row

            time.sleep(
                self.replay_speed
            )