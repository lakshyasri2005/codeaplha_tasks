# Stock Portfolio Tracker Application

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

portfolio = {}

while True:
    print("\n===== STOCK PORTFOLIO TRACKER =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Calculate Total Investment")
    print("4. Save Portfolio")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stock = input("Enter Stock Name: ").upper()

        if stock in stock_prices:
            quantity = int(input("Enter Quantity: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
            print("Stock added successfully!")
        else:
            print("Stock not available.")

    elif choice == "2":
        if len(portfolio) == 0:
            print("Portfolio is empty.")
        else:
            print("\nYour Portfolio:")
            for stock, quantity in portfolio.items():
                print(stock, "- Quantity:", quantity,
                      "- Price:", stock_prices[stock])

    elif choice == "3":
        total = 0
        for stock, quantity in portfolio.items():
            total += stock_prices[stock] * quantity
        print("Total Investment Value =", total)

    elif choice == "4":
        file = open("portfolio.txt", "w")
        for stock, quantity in portfolio.items():
            file.write(f"{stock} : {quantity}\n")
        total = sum(stock_prices[s] * q for s, q in portfolio.items())
        file.write(f"\nTotal Investment Value = {total}")
        file.close()
        print("Portfolio saved successfully.")

    elif choice == "5":
        print("Thank you for using Stock Portfolio Tracker!")
        break
    else:
        print("Invalid choice! Please try again.")
