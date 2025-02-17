import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import os

def clear_screen():
    # Clear the terminal screen depending on the operating system.
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')

while True:
    clear_screen()
    # Zadej tikry porovnávaných akcií
    stocks = input("zadej tikry (např.....ASML, LRCX, KLAC):\n").upper().split(", ")

    # Načti historická data do současnosti (zadej od kerého data)
    start_date = input("Zadej datum od ve formátu: 2020-01-01:\n")
    end_date = datetime.date.today().strftime('%Y-%m-%d')

    data = yf.download(stocks, start=start_date, end=end_date)['Adj Close']
    dividends = {stock: yf.Ticker(stock).dividends for stock in stocks}

    # Normalizuj ceny na stejný bod (první řádek tabulky), aby graf začínal na stejné úrovni
    normalized_data = data / data.iloc[0] * 100 - 100    # - 100 aby osa Y začínala na 0% ne 100%

    # Vypočítání procentuální změny od začátku období
    percent_changes = data.iloc[-1] / data.iloc[0] * 100 - 100
    print(f"Procentuální pohyb za dané období:")
    for ticker, change in sorted(percent_changes.items(), key=lambda item: item[1], reverse=True):
        print(f"{ticker}: {change:.2f}%")
    # Vypočítání celkové návratnosti i se započtenou dividendou
    total_returns = {}
    for stock in stocks:
        total_dividends = dividends[stock].loc[start_date:end_date].sum()
        total_value = data[stock].iloc[-1] + total_dividends  # Cena + dividendy
        total_return = ((total_value / data[stock].iloc[0]) - 1) * 100
        total_returns[stock] = total_return
    print("Celková návratnost (včetně dividend):")
    for stock, total_return in sorted(total_returns.items(), key=lambda item: item[1], reverse=True):
        print(f"{stock}: {total_return:.2f}%")

    # Vykresli graf
    plt.figure(figsize=(12, 6))
    for stock in stocks:
        label = f"{stock} ({percent_changes[stock]:.2f}%)"
        plt.plot(data.index, normalized_data[stock], label=label)

    plt.title("Procentuální nárust/pokles ceny za dané období")
    plt.xlabel('Datum')
    plt.ylabel('Pohyb ceny v %')
    plt.legend()
    plt.grid(True)
    plt.show()

    end = input("\nPro ukončení zadej: q\nPro pokračování: Enter\n")
    if end == "q":
        break



