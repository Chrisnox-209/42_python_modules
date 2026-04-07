import sys
import os
import site


def outside(value: bool) -> str:
    if value:
        package: list[str] = site.getsitepackages()
        return (f"\nMATRIX STATUS: Welcome to the construct\n\n"
                f"Current Python: {sys.executable}\n"
                f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
                f"Environment Path: {sys.prefix}\n\n"
                "SUCCESS: You're in an isolated environment!\n"
                "Safe to install packages without affecting\n"
                "the global system.\n\n"
                "Package installation path:\n"
                f"{package[0] if package else ''}")
    else:
        return (f"\nMATRIX STATUS: You're still plugged in\n\n"
                f"Current Python: {sys.executable}\n"
                "Virtual Environment: None detected\n\n"
                "WARNING: You're in the global environment!\n"
                "The machines can see everything you install.\n\n"
                "To enter the construct, run:\n"
                "python -m venv matrix_env\n"
                "source matrix_env/bin/activate # On Unix\n"
                "matrix_env\\Scripts\\activate # On Windows\n\n"
                "Then run this program again.")


def check_environment() -> bool:
    path: str = os.path.dirname(os.path.abspath(__file__))
    env_path: str = os.path.dirname(sys.executable)
    if path in env_path:
        return True
    else:
        return False


if __name__ == "__main__":
    print(outside(check_environment()))
