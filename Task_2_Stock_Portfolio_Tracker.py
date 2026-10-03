HEADER = "Stock : Quantity : Total Price"

Stock_Prices = {
    "NVDA": 234.75, "AAPL": 333.45, "GOOGL": 343.84, "MSFT": 514.75,
    "AMZN": 251.1,  "META": 729.01, "AVGO": 352.82, "TSLA": 372.98,
    "TSM": 471.64,  "BRK.B": 502.33,
}


def load_stocks(filename="Stocks"):
    data = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = [x.strip() for x in line.split(":")]
                if len(parts) != 3 or not parts[1].isdigit():
                    continue  # skips the header, blank lines, or anything unexpected
                name, qty, _ = parts
                if name not in Stock_Prices:
                    continue  # ignores unknown stock names
                data[name] = data.get(name, 0) + int(qty)  # merges old duplicate lines
    except FileNotFoundError:
        pass
    return data


def save_stocks(data, filename="Stocks"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(HEADER + "\n")
        for name, qty in data.items():
            file.write(f"{name} : {qty} : {round(Stock_Prices[name] * qty, 3)}\n")


def get_quantity(prompt, maximum=None):
    """Returns a positive whole number, or None if the input is invalid."""
    try:
        quantity = int(input(prompt))
        if quantity <= 0 or (maximum is not None and quantity > maximum):
            raise ValueError
        return quantity
    except ValueError:
        if maximum is None:
            print("Please enter a whole number greater than 0\n")
        else:
            print(f"Please enter a whole number between 1 and {maximum}\n")
        return None


print("\t\t\t\t\tStock Re-stocker CLI App")
print("\t\t\t\t\t========================\n")

while True:
    print("Options")
    print(
        """
    1) To Re-Stock
    2) To see The Stock
    3) Sell a Stock
    4) Exit the App
    """
    )
    option = input("Enter: ").strip()
    print("\n")

    if option == "1":
        while True:
            print(f"Stocks = {list(Stock_Prices.keys())}")
            stock = input("Enter the Stock you want to Re-stock: ").strip().upper()

            if stock not in Stock_Prices:
                print("Please enter one of the stocks mentioned\n")
                continue

            quantity = get_quantity("Enter the Quantity you want to re-stock: ")
            if quantity is None:
                continue

            stocks = load_stocks()
            stocks[stock] = stocks.get(stock, 0) + quantity  # add to existing, or create new
            save_stocks(stocks)
            print("The Stock is Re-stocked\n")

            if input("Do you want to re-stock more (y/n): ").strip().lower() == "n":
                break

    elif option == "2":
        stocks = load_stocks()
        if not stocks:
            print("No stocks yet\n")
        else:
            print(f"{'Stock':<8}{'Qty':>6}{'Total':>14}")
            for name, qty in stocks.items():
                print(f"{name:<8}{qty:>6}{Stock_Prices[name] * qty:>14.2f}")
            print()

    elif option == "3":
        stocks = load_stocks()
        if not stocks:
            print("You have no stocks to sell\n")
            continue

        print(f"Your stocks = {stocks}")
        stock = input("Enter the Stock you want to sell: ").strip().upper()
        if stock not in stocks:
            print("You don't own that stock\n")
            continue

        quantity = get_quantity("Enter the Quantity you want to sell: ", maximum=stocks[stock])
        if quantity is None:
            continue

        stocks[stock] -= quantity
        if stocks[stock] == 0:
            del stocks[stock]  # remove the line when nothing is left
        save_stocks(stocks)
        print("The Stock is sold\n")

    elif option == "4":
        print("The changes are saved and you can safely exit \n")
        break

    else:
        print("You have entered the wrong Option\n")