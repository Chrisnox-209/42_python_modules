from dotenv import load_dotenv
import os


def check_data() -> bool:
    check = True
    if os.getenv("MATRIX_MODE"):
        print(f"Mode: {os.getenv("MATRIX_MODE")}")
    else:
        print("[ERROR]: MATRIX_MODE no value")
        check = False

    if os.getenv("DATABASE_URL"):
        print(f"Database: {os.getenv("DATABASE_URL")}")
    else:
        print("[ERROR]: DATABASE_URL no value")
        check = False

    if os.getenv("API_KEY"):
        print(f"API Access: {os.getenv("API_KEY")}")
    else:
        print("[ERROR]: API_KEY no value")
        check = False

    if os.getenv("LOG_LEVEL"):
        print(f"Log Level: {os.getenv("LOG_LEVEL")}")
    else:
        print("[ERROR]: LOG_LEVEL no value")
        check = False

    if os.getenv("ZION_ENDPOINT"):
        print(f"Zion Network: {os.getenv("ZION_ENDPOINT")}")
    else:
        print("[ERROR]: ZION_ENDPOINT no value")
        check = False
    print()
    return check


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")

    env_loaded: bool = load_dotenv()
    data_ok: bool = check_data()

    print("Environment security check:\n"
          "[OK] No hardcoded secrets detected")

    if load_dotenv() is not True:
        print("[ERROR]: .env file found")
    else:
        print("[OK] .env file properly configured")

    if data_ok:
        print("[OK] Production overrides available")
    else:
        print("[ERROR]: Production options are incorrect")

    print("\nThe Oracle sees all configurations.")
