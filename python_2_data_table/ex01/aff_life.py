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
        country = 'Brazil'

        # Find Country data
        country_data = dataset[dataset['country'] == country].iloc[0, 1:]

        # Prepare data for plotting
        years = country_data.index.astype(int)
        life_expectancy = country_data.values

        # Create plot
        plt.plot(years, life_expectancy)
        plt.title(f"{country} Life Expectancy Projections")
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')

        # Set x-ticks to be every 40 years to avoid clutter
        plt.xticks(range(min(years), max(years) + 1, 40))

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
