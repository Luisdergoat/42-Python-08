#!/usr/bin/env python3
"""Loading Programs - Package Management Demo"""

import sys
import os
import importlib

os.environ['MPLBACKEND'] = 'Agg'


def check_dependencies():
    """Check and display installed dependency versions."""
    dependencies = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computations ready',
        'matplotlib': 'Visualization ready',
        'requests': 'Network access ready'
    }

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    all_ok = True
    versions = {}

    for package, description in dependencies.items():
        try:
            mod = importlib.import_module(package)
            version = getattr(mod, '__version__', 'unknown')
            versions[package] = version
            print(f"[OK] {package} ({version}) - {description}")
        except ImportError:
            print(f"[FAIL] {package} - Not installed")
            all_ok = False

    return all_ok, versions


def analyze_matrix_data():
    """Analyze matrix data and create visualization."""
    try:
        import pandas as pd
        import numpy as np

        print("Analyzing Matrix data...")

        # Generate sample data
        data_points = 1000
        print(f"Processing {data_points} data points...")

        data = pd.DataFrame({
            'x': np.random.randn(data_points),
            'y': np.random.randn(data_points)
        })

        # Create visualization
        print("Generating visualization...")
        try:
            import matplotlib.pyplot as plt
            plt.figure(figsize=(8, 6))
            plt.scatter(data['x'], data['y'], alpha=0.5)
            plt.xlabel('X Axis')
            plt.ylabel('Y Axis')
            plt.title('Matrix Data Analysis')
            plt.grid(True)
            plt.savefig('matrix_analysis.png')
            plt.close()
        except Exception:
            # If matplotlib fails, create a simple text summary instead
            with open('matrix_analysis.txt', 'w') as f:
                f.write("Matrix Analysis Summary\n")
                f.write(f"Points: {data_points}\n")
                f.write(f"Mean X: {data['x'].mean():.4f}\n")
                f.write(f"Mean Y: {data['y'].mean():.4f}\n")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    except ImportError as e:
        print(f"Error: Missing required package - {e}")
        print("Install dependencies with: pip install -r requirements.txt")
        sys.exit(1)


def main():
    """Main function."""
    all_ok, versions = check_dependencies()

    if not all_ok:
        print("\nMissing dependencies!")
        print("Install with: pip install -r requirements.txt")
        print("Or: poetry install")
        sys.exit(1)

    print()
    analyze_matrix_data()


if __name__ == '__main__':
    main()
