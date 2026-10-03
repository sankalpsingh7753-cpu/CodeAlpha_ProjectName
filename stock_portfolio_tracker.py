# =====================================================
#  STOCK PORTFOLIO TRACKER
# =====================================================

# 1. Dictionary of stocks: key = stock symbol, value = price (in rupees)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

# 2. Show the program title and the available stocks
print("=================================")
print("     STOCK PORTFOLIO TRACKER")
print("=================================")
print()
print("Available Stocks:")
for symbol in stock_prices:
    print(symbol, "- ₹" + str(stock_prices[symbol]))
print()

# 3. Initialize variables
total_investment = 0   # keeps the running total of the whole portfolio
portfolio = []         # list of dictionaries, one dictionary per stock entered
add_more = "yes"       # controls the main loop

# 4. Main loop: keep asking for stocks until the user says "no"
while add_more == "yes":

    # 5. Ask for a stock symbol until a valid one is entered
    stock = input("Enter stock symbol: ").upper().strip()   # aapl -> AAPL

    if stock in stock_prices:
        price = stock_prices[stock]   # get the price from the dictionary

        # 6. Ask for quantity until a valid positive number is entered
        quantity = 0
        while quantity <= 0:
            try:
                quantity = int(input("Enter quantity: "))   # text -> whole number
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
            except ValueError:
                # runs if the user types something like "abc"
                print("Please enter a valid number.")
                quantity = 0

        # 7. Calculate the investment value
        investment = price * quantity
        print()
        print(stock, "Investment = ₹" + str(price), "×", quantity, "= ₹" + str(investment))

        # 8. Add to the total and store this stock in the portfolio list
        total_investment += investment
        portfolio.append({
            "stock": stock,
            "price": price,
            "quantity": quantity,
            "investment": investment
        })

        # 9. Ask whether to add another stock (repeat until answer is yes/no)
        print()
        add_more = input("Do you want to add another stock? (yes/no): ").lower().strip()
        while add_more != "yes" and add_more != "no":
            print("Please type yes or no.")
            add_more = input("Do you want to add another stock? (yes/no): ").lower().strip()
        print()

    else:
        # Invalid stock: show a message and the loop asks again
        print("Stock not found in the available stock list.")
        print("Please enter another stock.")
        print()

# 10. Display the final portfolio summary
print("=================================")
print("       PORTFOLIO SUMMARY")
print("=================================")
print()

if len(portfolio) == 0:
    print("No stocks were added.")
else:
    print(f"{'Stock':<12}{'Price':<10}{'Quantity':<12}{'Value'}")
    for item in portfolio:
        print(f"{item['stock']:<12}{'₹' + str(item['price']):<10}"
              f"{item['quantity']:<12}{'₹' + str(item['investment'])}")

print()
print("---------------------------------")
print("Total Investment: ₹" + str(total_investment))
print("---------------------------------")
print()

# 11. OPTIONAL FEATURE: save the portfolio to a text file
if len(portfolio) > 0:
    save = input("Do you want to save the portfolio to a file? (yes/no): ").lower().strip()

    if save == "yes":
        # "w" = write mode (creates the file, or replaces it if it exists)
        # encoding="utf-8" makes sure the ₹ symbol is saved correctly
        with open("portfolio.txt", "w", encoding="utf-8") as file:
            file.write("STOCK PORTFOLIO\n\n")
            for item in portfolio:
                file.write(item["stock"] + "\n")
                file.write("Price: ₹" + str(item["price"]) + "\n")
                file.write("Quantity: " + str(item["quantity"]) + "\n")
                file.write("Investment: ₹" + str(item["investment"]) + "\n\n")
            file.write("Total Investment: ₹" + str(total_investment) + "\n")

        print()
        print("Portfolio saved successfully to portfolio.txt")

print()
print("Thank you for using Stock Portfolio Tracker!")
