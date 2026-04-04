import os
import subprocess
import sys

import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Main function to load life expectancy data, process it for a
    specified country, and produce a plot visualizing the life
    expectancy over time.

    This function loads a dataset from a given file path, filters
    life expectancy data for a specific country, and generates a
    line plot to display the trends.

    Raises:
        Exception: If any error occurs during data loading,
                   processing, or plotting.

    """
    try:
        dataset = load("../life_expectancy_years.csv")
        country = "Brazil"

        # Find Country data
        country_data = dataset[dataset["country"] == country].iloc[0, 1:]

        # Prepare data for plotting
        years = country_data.index.astype(int)
        life_expectancy = country_data.values

        # Create plot
        plt.plot(years, life_expectancy)
        plt.title(f"{country} Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")

        # Set x-ticks to be every 40 years to avoid clutter
        plt.xticks(range(min(years), max(years) + 1, 40))

        plt.tight_layout()
        name = f"{country}_life_expectancy.png"
        plt.savefig(name)
        open_file(name)
    except Exception as e:
        print(f"An error occurred: {e}")


def open_file(file_path: str) -> None:
    try:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
        else:
            if sys.platform.startswith("win"):
                # Windows
                os.startfile(file_path)
            elif sys.platform == "darwin":
                # macOS
                subprocess.run(["open", file_path], check=False)
            else:
                # Linux/Unix (xdg-open is the common tool)
                subprocess.run(["xdg-open", file_path], check=False)
    except Exception as e:
        print(f"Could not open {file_path}: {e}")


if __name__ == "__main__":
    main()
