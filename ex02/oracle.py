"""This is a module for the Oracle class."""

import os
import sys
import importlib


REQUIRED_LIBS = {
    "dotenv": "python-dotenv"
}

REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

ALLOWED_MODES = ["production", "development", "testing"]
ALLOWED_LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def check_env() -> bool:
    if os.getenv("VIRTUAL_ENV") is None:
        return False
    return True


def check_required_libs() -> bool:
    missing_libs = []
    for lib, package in REQUIRED_LIBS.items():
        try:
            importlib.import_module(lib)
        except ImportError:
            missing_libs.append(package)
    if missing_libs:
        print(f"Missing required libraries: {', '.join(missing_libs)}")
        return False
    return True


def print_env_instructions() -> None:
    if check_env() is False:
        print("ERROR: You're not in a virtual environment!")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate")
        print("matrix_env\\Scripts\\activate      # on Windows")
        print("\nThen run this program again")
    else:
        print("MATRIX STATUS: Welcome to the Oracle!\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: Detected")
        print(f"Environment Path: {os.getenv('VIRTUAL_ENV')}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\nthe global system")
        print("\nPackage installation path:")


def print_install_instructions() -> None:
    if check_env() is False:
        print("ERROR: You're not in a virtual environment!")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate")
        print("matrix_env\\Scripts\\activate      # on Windows")
        print("\nThen run this program again")
    else:
        print("run python3 -m pip install python-dotenv to install")


def load_configuration() -> dict:
    from dotenv import load_dotenv
    load_dotenv()
    config = {}
    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if value is None:
            print(f"ERROR: Missing required environment variable: {var}")
            return {}
        config[var] = value
    return config


def validate_configuration(config: dict) -> bool:
    mode = config.get("MATRIX_MODE")
    log_level = config.get("LOG_LEVEL")
    if mode not in ALLOWED_MODES:
        print(f"ERROR: Invalid MATRIX_MODE: {mode}")
        print(f"Allowed modes: {', '.join(ALLOWED_MODES)}")
        return False
    if log_level not in ALLOWED_LOG_LEVELS:
        print(f"ERROR: Invalid LOG_LEVEL: {log_level}")
        print(f"Allowed log levels: {', '.join(ALLOWED_LOG_LEVELS)}")
        return False
    return True


def main():
    print_env_instructions()
    if check_env() is False:
        return
    if not check_required_libs():
        print_install_instructions()
        return
    config = load_configuration()
    if not config:
        return
    if not validate_configuration(config):
        return
    print("\nConfiguration loaded successfully!")
    print("You're ready to connect to the Oracle and access the "
          "secrets of the Matrix.")


if __name__ == "__main__":
    main()
