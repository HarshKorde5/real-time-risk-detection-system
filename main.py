def main():
    from ingestion.data_loader import (
        MarketDataLoader
    )

    from config.thresholds import (
        MONITORED_STOCKS
    )

    loader = MarketDataLoader()

    for stock in MONITORED_STOCKS:

        data = loader.fetch_stock_data(stock)

        if not data.empty:

            loader.save_to_csv(
                data,
                stock
            )

            print("\n")
            print(data.head())
            print("\n")
        
if __name__ == "__main__":
    main()