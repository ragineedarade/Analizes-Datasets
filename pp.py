import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path, encoding='utf-10'):
    """
    Load the dataset from a CSV file.
    """
    try:
        return pd.read_csv(file_path, encoding=encoding)
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")
        return None


def display_basic_statistics(df):
    """
    Display basic statistics of the dataset.
    """
    if df is not None:
        print("Basic Statistics:")
        print(df.describe())
    else:
        print("No data to display statistics.")


def plot_data(df, column_x, column_y):
    """
    Plot data from the dataset.
    """
    if df is not None and column_x in df.columns and column_y in df.columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(df[column_x], df[column_y], alpha=0.5)
        plt.title(f'{column_y} vs {column_x}')
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.grid(True)
        plt.show()
    else:
        print("No data to plot or specified columns do not exist.")


def main():
    # Path to the CSV file
    file_path = 'zomato.csv'

    # Load the dataset
    df = load_data(file_path, encoding='ISO-8859-1')

    # Display basic statistics
    display_basic_statistics(df)

    # Plot data
    # Change 'AggregateRating' and 'votes' to the names of the columns you want to plot
    plot_data(df, 'AggregateRating', 'votes')


if __name__ == "__main__":
    main()
