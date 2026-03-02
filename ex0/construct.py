import os
import sys


def get_path():
    # Baut den typischen site-packages-Pfad des aktiven venv zusammen.
    return f"{os.getenv('VIRTUAL_ENV')}lib/python\
        {sys.version_info.major}.{sys.version_info.minor}/site-packages"


def check_env():
    # Prüft, ob eine virtuelle Umgebung aktiv ist.
    if os.getenv("VIRTUAL_ENV") is None:
        print_no_env()
    else:
        # Erfolgsfall: wir zeigen dem Nutzer, dass er isoliert arbeitet.
        print("MATRIX STATUS: Welcome to the construct!\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Enviroment: matrix_env")
        print(f"Environment Path: {os.getenv('VIRTUAL_ENV')}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\nthe global system")
        print("\nPackage installation path:")
        print(get_path())


def print_no_env():
    # Fehlerfall: keine venv aktiv, daher Warnung + kurze Anleitung.
    print("MATRIX Status: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Enviroment: Not Detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nToenter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate")
    print("matrix_env")
    print("Scripts")
    print("Activate      # on Windows")
    print("\nThen run this program again")


def main():
    # Einstiegspunkt: startet die Umgebungsprüfung.
    check_env()


if __name__ == "__main__":
    main()
