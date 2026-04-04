import os
import subprocess
import sys

import matplotlib.pyplot as plt
from load_csv import load


def convert_population(val):
    """
    Converts a population value represented as a string with a suffix ('M' for
    millions, 'k' for thousands) or as a numeric type into a numerical
    representation of the population value.

    Args:
        val: The population value to convert. It can be a string ending with
            'M' or 'k', or a numeric type.

    Returns:
        float: The numerical representation of the population.

    Raises:
        ValueError: If the value cannot be converted to a number.
    """
    if isinstance(val, str):
        if val.endswith("M"):
            return float(val[:-1]) * 1_000_000
        elif val.endswith("k"):
            return float(val[:-1]) * 1_000
        return float(val)
    return val


def main():
    """
    Plots population projections for two specified countries using data from
    a dataset.

    The function reads a dataset file, filters population data for two
    specified countries, and plots projections of their population between
    the years 1800 and 2050. The plot uses customized x-ticks for every 40
    years and formats the y-axis to represent values in millions ('M').
    The functionality wraps potential errors during execution and prints
    the error message if one occurs.

    Raises:
        Exception: If there is any error in reading the dataset, filtering
            data, or generating the plot, an exception with a specific message
            is raised.
    """
    try:
        dataset = load("../population_total.csv")
        campus_a = "France"
        campus_b = "Belgium"

        # Filter data for the specified countries
        df_a = dataset[dataset["country"] == campus_a].iloc[0, 1:]
        df_b = dataset[dataset["country"] == campus_b].iloc[0, 1:]

        # Convert index to int and filter years from 1800 to 2050
        df_a.index = df_a.index.astype(int)
        df_b.index = df_b.index.astype(int)

        years = [year for year in range(1800, 2051)]
        pop_a = [convert_population(df_a[year]) for year in years]
        pop_b = [convert_population(df_b[year]) for year in years]

        # Create plot
        plt.plot(years, pop_b, label=campus_b, color="blue")
        plt.plot(years, pop_a, label=campus_a, color="green")

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        # Set x-ticks to be every 40 years
        plt.xticks(range(1800, 2051, 40))

        # Format y-axis to show 'M' for millions
        def format_y(x, _pos):
            if x >= 1e6:
                return f"{x / 1e6:.0f}M"
            elif x >= 1e3:
                return f"{x / 1e3:.0f}k"
            return f"{x:.0f}"

        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_y))
        plt.yticks([20e6, 40e6, 60e6])

        plt.legend(loc="lower right")
        plt.tight_layout()
        name = "population_projections.png"
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
