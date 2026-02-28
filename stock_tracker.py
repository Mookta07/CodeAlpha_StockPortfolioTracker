# Stock Portfolio Tracker

# Hardcoded stock prices (example)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")

# Ask user number of stocks
n = int(input("Enter number of different stocks you want to add: "))

# Input stock details
for i in range(n):
    stock_name = input("\nEnter stock name (AAPL, TSLA, GOOG, MSFT, AMZN): ").upper()
    
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not available in price list.")

# Calculate total investment
print("\n📊 Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock} - Quantity: {quantity}, Price: ${price}, Investment: ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save result to file? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("Stock Portfolio Summary\n")
    
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} - Quantity: {quantity}, Investment: ${investment}\n")
    
    file.write(f"\nTotal Investment: ${total_investment}")
    file.close()
    
    print("✅ Portfolio saved to portfolio.txt")

print("✅ Program finished.")
