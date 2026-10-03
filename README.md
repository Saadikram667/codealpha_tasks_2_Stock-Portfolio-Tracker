# codealpha_tasks_2_Stock-Portfolio-Tracker

```markdown
# 📈 Stock Portfolio Tracker (CLI)

A light, robust Command-Line Interface (CLI) application written in Python that allows users to manage a stock portfolio, track real-time holdings, re-stock shares, sell holdings, and persist portfolio data across sessions using local file I/O.

---

## 🌟 Features

- **Portfolio Re-Stocking**: Add new or existing stock tickers to your portfolio with automatic input sanitization (`.strip().upper()`).
- **Holdings Summary**: Display your current portfolio in a clean, formatted table showing ticker symbols, share quantities, and total holding values.
- **Selling Mechanism**: Sell custom quantities of owned shares with automatic stock removal when quantities hit zero.
- **File Persistence**: Reads from and writes to a text file (`Stocks`) so your portfolio state persists across application restarts.
- **Robust Input Validation**: Safely handles missing files (`FileNotFoundError`), invalid tickers, negative/zero quantities, non-numeric inputs, and over-selling attempts.

---

## 🏗️ How It Works & Architecture


```

```
             +-----------------------+
             |   Stock_Prices Dict   |
             | (Ticker -> Unit Price)|
             +-----------+-----------+
                         |
                         v

```

+-----------------+  +-------+-------+  +-------------------+
|  Main Menu Loop |->| Helper Functions|->| Stocks Text File  |
|  (1, 2, 3, 4)   |  | (Load/Save/Val) |  | (Persistent Data) |
+-----------------+  +---------------+  +-------------------+

```

### 1. Predefined Price Dictionary (`Stock_Prices`)
The application references standard market prices stored in a central Python dictionary:
- Supported Tickers: `NVDA`, `AAPL`, `GOOGL`, `MSFT`, `AMZN`, `META`, `AVGO`, `TSLA`, `TSM`, `BRK.B`.

### 2. Persistent Storage (`Stocks`)
Portfolio data is stored in a simple plain-text file formatted as:
```text
Stock : Quantity : Total Price
NVDA : 10 : 2347.5
AAPL : 5 : 1667.25

```

### 3. Core Functions

* `load_stocks(filename="Stocks")`: Reads the saved file line-by-line, ignores headers/empty lines, validates ticker existence, aggregates duplicate entries, and returns a dictionary of current holdings.
* `save_stocks(data, filename="Stocks")`: Rewrites the `Stocks` file with updated quantities and recalculated total values rounded to 3 decimal places.
* `get_quantity(prompt, maximum=None)`: Validates user input to ensure positive integers, handles `ValueError` exceptions gracefully, and enforces upper limits when selling shares.

---

## 🛠️ Usage Instructions

### Prerequisites

* Python 3.x installed on your system.

### Running the Application

1. **Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/Stock-Portfolio-Tracker.git](https://github.com/YOUR_USERNAME/Stock-Portfolio-Tracker.git)
cd Stock-Portfolio-Tracker

```


2. **Run the Python script:**
```bash
python Task_2_Stock_Portfolio_Tracker.py

```


3. **Menu Options:**
* **`1` Re-Stock**: Enter a stock ticker and quantity to buy/add shares.
* **`2` See the Stock**: View a tabular summary of your current portfolio.
* **`3` Sell a Stock**: Remove shares from an existing holding.
* **`4` Exit the App**: Close the application.



---

## 🎯 Example Menu Interaction

```text
========================================
       Stock Re-stocker CLI App
========================================

Options:
 1) Re-Stock
 2) See the Stock
 3) Sell a Stock
 4) Exit the App

Enter: 1
Stocks = ['NVDA', 'AAPL', 'GOOGL', ...]
Enter the Stock you want to Re-stock: nvda
Enter the Quantity you want to re-stock: 10
The Stock is Re-stocked!
Do you want to re-stock more (y/n): n

```

---

## 🤝 Acknowledgment & Internship

Developed as part of the **CodeAlpha** Internship Task 2 (`Task_2_Stock_Portfolio_Tracker.py`).

```

```
