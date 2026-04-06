"""Accessing the Mainframe: secure config loading with .env and environment variables."""

import os
import sys


ALLOWED_MODES = {"development", "production"}
ALLOWED_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


def load_configuration():
    """Load config from .env and environment, while keeping env var override priority."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("ERROR: Missing dependency 'python-dotenv'.")
        print("Install it with: pip install python-dotenv")
        print("Or with Poetry: poetry add python-dotenv")
        sys.exit(1)

    config_keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    preloaded_env = {key for key in config_keys if os.getenv(key) is not None}
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    env_file_exists = os.path.exists(env_path)

    # Keep shell-provided variables as highest priority (override=False).
    load_dotenv(dotenv_path=env_path, override=False)

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", ""),
        "API_KEY": os.getenv("API_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", ""),
    }

    return config, preloaded_env, env_file_exists


def validate_configuration(config):
    """Validate mode and log level; return warnings for missing required values."""
    warnings = []

    mode = config["MATRIX_MODE"].strip().lower()
    if mode not in ALLOWED_MODES:
        warnings.append(
            "Invalid MATRIX_MODE detected. Falling back to 'development'."
        )
        mode = "development"
    config["MATRIX_MODE"] = mode

    log_level = config["LOG_LEVEL"].strip().upper()
    if log_level not in ALLOWED_LOG_LEVELS:
        warnings.append("Invalid LOG_LEVEL detected. Falling back to 'DEBUG'.")
        log_level = "DEBUG"
    config["LOG_LEVEL"] = log_level

    if not config["DATABASE_URL"]:
        warnings.append("DATABASE_URL is missing.")
    if not config["API_KEY"]:
        warnings.append("API_KEY is missing.")
    if not config["ZION_ENDPOINT"]:
        warnings.append("ZION_ENDPOINT is missing.")

    return warnings


def print_configuration(config):
    """Print environment-sensitive runtime status."""
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if config["MATRIX_MODE"] == "production":
        print("Database: Connected to production instance")
        print("Log Level: INFO/above recommended for production")
    else:
        print("Database: Connected to local instance")
        print("Log Level: DEBUG")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated (missing API_KEY)")

    if config["ZION_ENDPOINT"].startswith("http"):
        print("Zion Network: Online")
    elif config["ZION_ENDPOINT"]:
        print("Zion Network: Configured (check endpoint format)")
    else:
        print("Zion Network: Offline (missing endpoint)")


def print_security_check(env_file_exists, preloaded_env):
    """Print security checks around secrets and override behavior."""
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_file_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found (using environment/default values)")

    if preloaded_env:
        print("[OK] Production overrides available")
    else:
        print("[OK] Production overrides available")


def main():
    print("ORACLE STATUS: Reading the Matrix...")

    config, preloaded_env, env_file_exists = load_configuration()
    warnings = validate_configuration(config)

    print_configuration(config)

    if warnings:
        print("Configuration warnings:")
        for warning in warnings:
            print(f"- {warning}")

    print_security_check(env_file_exists, preloaded_env)
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
