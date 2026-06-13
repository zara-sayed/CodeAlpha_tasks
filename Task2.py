# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, "- $", price)

num_stocks = int(input("\nHow many different stocks do you want to enter? "))

portfolio_details = []

for i in range(num_stocks):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio_details.append(
            f"{stock_name} - Quantity: {quantity}, Value: ${investment}"
        )

    else:
        print("Stock not found in the price list!")

print("\n===== PORTFOLIO SUMMARY =====")
for item in portfolio_details:
    print(item)

print("\nTotal Investment Value: $", total_investment)

# Save result to a text file
file = open("portfolio_report.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("======================\n")

for item in portfolio_details:
    file.write(item + "\n")

file.write("\nTotal Investment Value: $" + str(total_investment))

file.close()

print("\nPortfolio report saved successfully in 'portfolio_report.txt'")
