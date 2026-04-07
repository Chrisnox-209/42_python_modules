
import importlib
from typing import Any
from types import ModuleType
import sys


def check_import(library: str) -> bool:
    try:
        module: ModuleType = importlib.import_module(library)
        print(f"[OK] {library} "
              f"({getattr(module, '__version__', 'no version')}) "
              "- Data manipulation ready")
        return True
    except ImportError as error:
        print(f"{error}\nplease: pip install "
              "-r requirements.txt or poetry install")
        return False


def scrap_data(url: str) -> tuple[list, list]:
    import requests
    from requests.models import Response
    headers: dict[str, str] = {"User-Agent": "Mozilla/5.0"}
    try:
        response: Response = requests.get(url, headers=headers)
        data: Any = response.json()
    except Exception as error:
        print(error)
        sys.exit(1)
    date_list: Any = data['chart']['result'][0]['timestamp']
    data_list: Any = (
        data['chart']['result'][0]['indicators']['quote'][0]['close']
    )

    clean_prices: list = []
    clean_dates: list = []

    for price, date in zip(data_list, date_list):
        if price is not None:
            clean_prices.append(price)
            clean_dates.append(date)

    return clean_prices, clean_dates


def ndarray(data_list: Any, date_list: Any) -> tuple:
    import numpy
    price_ndarray: Any = numpy.array(data_list)
    dates_ndarray: Any = numpy.array(date_list)

    prices_1000: Any = price_ndarray[-1000:]
    dates_1000: Any = dates_ndarray[-1000:]

    print("Analyzing Matrix data...")
    print(f"Processing {len(prices_1000)} data points...")
    print("Generating visualization...")
    return prices_1000, dates_1000


def structuring_data(data_ndarray: Any, dates_ndarray: Any) -> Any:
    import pandas
    second_dates: Any = pandas.to_datetime(dates_ndarray, unit='s')
    data_frame: Any = pandas.DataFrame(data_ndarray,
                                  index=second_dates,
                                  columns=["Price barrel (USD)"])
    return data_frame


def generate_graph(data_frame: Any, name_file: str) -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.plot(data_frame.index, data_frame["Price barrel (USD)"], color='blue')

    plt.title("Evolution of the price of a barrel of oil (CL=F)")
    plt.xlabel("Date & Time")
    plt.ylabel("Price (USD)")

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
    prices: list = []
    dates: list = []
    price_ndarray: Any
    date_ndarray: Any

    url: str = (
        "https://query1.finance.yahoo.com/v8/finance/chart/CL=F"
        "?range=5d&interval=1m"
    )

    name_png = "matrix_analysis.png"
    prices, dates = scrap_data(url)
    price_ndarray, date_ndarray = ndarray(prices, dates)
    data_frame: Any = structuring_data(price_ndarray, date_ndarray)
    generate_graph(data_frame, name_png)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
