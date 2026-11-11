def stock_portfolio_tracker():
    stock_prices = {
        "GOOGL": 200,
        "APPL": 190,
        "HP": 150,
        "GITH": 140,
        "TESL": 250,
        "MERCD": 200,
        "YOUTB": 200,
    }

    portfolio = {}
    total_investment = 0
    print("--- Stock Portfolio Tracker---")
    print("Available stocks and prices:", stock_prices)

    while True:
        stock = input("\nEnter stock symbol (e.g., HP) or 'done' to finish: ").strip().upper()

        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found in the price list, please pick from the available stocks.")
            continue
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Please enter a valid whole number for qunatity.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print("\n--- Summary ---")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            total_investment += value
            print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")
        print(f"\nTotal portfolio Investment value: ${total_investment}")

        save_choice = input("\nwould you like to save this summary to a . txt file? (y/n): ").strip().lower()
        if save_choice == 'y':
            with open("portfolio_summary.txt", "w") as f:
                f.write("--- Portfolio Summary ---\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
                f.write(f"\nTotal Investment Value: ${total_investment}\n")
            print("Summary successfully saved to 'portfolio_summary.txt'!")

if __name__ == "__main__":
    stock_portfolio_tracker()
                