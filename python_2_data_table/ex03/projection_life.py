import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def parse_income(value):
    """
    Parses an income value that might have a 'k' suffix.
    Example: '10.3k' -> 10300
    """
    if isinstance(value, str):
        if value.endswith("k"):
            return float(value[:-1]) * 1000
        elif value.endswith("M"):
            return float(value[:-1]) * 1000000
        return float(value)
    return float(value)


def main():
    """
    Loads life expectancy and income data, filters for the year 1900,
    and displays a scatter plot of life expectancy vs. GNP.
    """
    try:
        life_expect = load("../life_expectancy_years.csv")
        gdp_data = load(
            "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
    except Exception as e:
        print(f"Error loading files: {e}")
        return

    year = "1900"

    # Extract the year 1900 data for both
    if year not in life_expect.columns or year not in gdp_data.columns:
        print(f"Year {year} not found in the data.")
        return

    # Use 'country' as index for both
    life_1900 = life_expect.set_index("country")[year]
    income_1900 = gdp_data.set_index("country")[year].apply(parse_income)

    # Align data by joining on the country index (this keeps only countries)
    df_1900 = pd.DataFrame(
        {"life": life_1900, "income": income_1900}
    ).dropna()

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(df_1900["income"], df_1900["life"])

    plt.xscale("log")
    plt.title(year)
    plt.xlabel("Gross national product")
    plt.ylabel("Life expectancy")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
