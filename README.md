# 📈 Stock Alert Project

A Python-based automation system that fetches real-time US stock market data, analyzes daily price changes, and alerts you when a company’s stock experiences a significant gain or loss.

---

## 🚀 Features

- Automated daily stock data fetching using `yfinance`
- Configurable schedule time through `config.json`
- Threshold alerts for major daily gainers or losers
- Simple configuration and modular code structure
- Ready for automation or cloud deployment

---

## 🗂️ Project Structure

```
Stock Alert Project/
│
├── Alert_Manager.py          # Handles gain/loss detection
├── Automation_function.py    # Schedules daily data fetching
├── Data_fetcher.py           # Fetches stock data using yfinance
├── Notifier.py               # Handles alert notifications
├── Main.py                   # Entry point to run everything
├── config.json               # Stores time, tickers, and thresholds
├── requirements.txt          # Dependency list
└── venv/                     # Virtual environment (ignored by Git)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/stock-alert-project.git
cd stock-alert-project
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🧩 Configuration

Edit the `config.json` file to customize settings:

```json
{
  "schedule_time": "23:45",
  "tickers": ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA", "META", "NVDA", "NFLX", "JPM", "DIS"],
  "thresholds": {
    "gain": 3.0,
    "loss": -3.0
  }
}
```

| Key | Description |
|------|--------------|
| `schedule_time` | Time of day to fetch stock data (24h format) |
| `tickers` | List of stock tickers to track |
| `thresholds` | Daily % thresholds for gain/loss alerts |

---

## ▶️ Running the Project

Run the main script:

```bash
python Main.py
```

The system will:
1. Wait until the scheduled time
2. Fetch data for all tickers
3. Calculate daily returns and volatility
4. Print or send alerts for big movers

---

## 📊 Example Output

```
✅ Stored 10 stock records for 2025-10-07 at 23:45
🚀 Tesla, Inc. gained +4.5%
📉 Meta Platforms, Inc. dropped -3.2%
```

---

## 📦 Dependencies

Listed in `requirements.txt`:

```
yfinance==0.2.66
pandas==2.2.3
numpy==2.3.3
schedule==1.2.1
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🧠 Future Improvements

- Add email / Telegram alerts  
- Store history in CSV or a database  
- Add charts or a Streamlit dashboard  
- Improve error handling and retry logic  

---

## 👨‍💻 Author

**Your Name Here**  
Developed in Python 3.13  
GitHub: [@taha1778](https://github.com/taha1778)

---

## 🪪 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 💡 Notes

- Uses Yahoo Finance (`yfinance`) API for real stock market data.  
- Make sure your system time matches your region for accurate scheduling.  
- You can host this script on PythonAnywhere, Replit, or a VPS for 24/7 uptime.
