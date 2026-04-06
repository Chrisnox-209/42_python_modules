
import importlib
import sys


def check_import(library: str):
    try:
        module = importlib.import_module(library)
        print(f"[OK] {library} ({getattr(module, '__version__', 'no version')}) - Data manipulation ready")
        return True
    except ImportError as error:
        print(f"{error}\nplease: pip install "
              "-r requirements.txt or poetry install")
        return False


def scap_data(url):
    import requests
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    data = response.json()
    date_list = data['chart']['result'][0]['timestamp']
    data_list = data['chart']['result'][0]['indicators']['quote'][0]['close']

    clean_prices = []
    clean_dates = []

    for price, date in zip(data_list, date_list):
        if price is not None:
            clean_prices.append(price)
            clean_dates.append(date)

    return clean_prices, clean_dates


def ndarray(data_list, date_list):
    import numpy
    price_ndarray = numpy.array(data_list)
    dates_ndarray = numpy.array(date_list)

    prices_1000 = price_ndarray[-1000:]
    dates_1000 = dates_ndarray[-1000:]

    print("Analyzing Matrix data...")
    print(f"Processing {len(prices_1000)} data points...")
    print("Generating visualization...")
    return prices_1000, dates_1000


def structuring_data(data_ndarray, dates_ndarray):
    import pandas
    second_dates = pandas.to_datetime(dates_ndarray, unit='s')
    data_frame = pandas.DataFrame(data_ndarray, index=second_dates, columns=["Price barrel (USD)"])
    return data_frame


def generate_graph(data_frame, name_file):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.plot(data_frame.index, data_frame["Price barrel (USD)"], color='blue')

    plt.title("Évolution du prix du baril de pétrole (CL=F)")
    plt.xlabel("Date et Heure")
    plt.ylabel("Prix (USD)")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(name_file)
    plt.close()



if __name__ == "__main__":
    if not all([
        check_import("pandas"),
        check_import("numpy"),
        check_import("requests"),
        check_import("matplotlib")
    ]):
        sys.exit(1)

    url = "https://query1.finance.yahoo.com/v8/finance/chart/CL=F?range=5d&interval=1m"
    name_png = "matrix_analysis.png"
    prices, dates = scap_data(url)
    price_ndarray, date_ndarray = ndarray(prices, dates)
    data_frame = structuring_data(price_ndarray, date_ndarray)
    generate_graph(data_frame, name_png)


    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
