import sys

check = True
try:
    import pandas
    print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
except ImportError as error:
    check = False
    print(f"{error}\nplease: pip install "
          "-r requirements.txt or poetry install")

try:
    import numpy
    print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
except ImportError as error:
    check = False
    print(f"{error}\nplease: pip install "
          "-r requirements.txt or poetry install")

try:
    import requests
    print(f"[OK] requests ({requests.__version__}) - Network access ready")
except ImportError as error:
    check = False
    print(f"{error}\nplease: pip install "
          "-r requirements.txt or poetry install")

try:
    import matplotlib
    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
except ImportError as error:
    check = False
    print(f"{error}\nplease: pip install "
          "-r requirements.txt or poetry install")

if check is not True:
    sys.exit(1)
