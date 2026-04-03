try:
    import pandas
    print("[OK] pandas (3.0.2) - Data manipulation ready")
except Exception as error:
    print(f"{error}\nplease: pip install "
          "-r requirement.txt")

try:
    import numpy
    print("[OK] numpy (2.4.4) - Numerical computation ready")
except Exception as error:
    print(f"{error}\nplease: pip install "
          "-r requirement.txt")

try:
    import requests
    print("[OK] requests (2.33.1) - Network access ready")
except Exception as error:
    print(f"{error}\nplease: pip install "
          "-r requirement.txt")

try:
    import matplotlib
    print("[OK] matplotlib (3.10.8) - Visualization ready")
except Exception as error:
    print(f"{error}\nplease: pip install "
          "-r requirement.txt")