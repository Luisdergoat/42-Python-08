import os
import sys


def get_path():
    venv_path = os.getenv("VIRTUAL_ENV", "")
    return os.path.join(
        venv_path,
        "lib",
        f"python{sys.version_info.major}.{sys.version_info.minor}",
        "site-packages",
    )


def check_env():
    if os.getenv("VIRTUAL_ENV") is None:
        print_no_env()
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(os.getenv('VIRTUAL_ENV', ''))}")
        print(f"Environment Path: {os.getenv('VIRTUAL_ENV')}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(get_path())


def print_no_env():
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print("Then run this program again.")


def main():
    check_env()


if __name__ == "__main__":
    main()
