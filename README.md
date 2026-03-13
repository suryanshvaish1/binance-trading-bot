# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot that places **Market and Limit orders** on Binance Futures Testnet (USDT-M).

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports **BUY and SELL**
- CLI input using Typer
- Input validation
- Structured project architecture
- Logging of API requests, responses, and errors

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py          # Binance client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging configuration
│   └── __init__.py
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
└── trading_bot.log        # Example logs

## Setup

1. Clone the repository

git clone <repo-link>

2. Navigate to the project folder

cd trading_bot

3. Install dependencies

pip install -r requirements.txt

4. Add your Binance Futures Testnet API keys in `cli.py`
