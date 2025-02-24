 # Zomato Data Analysis

This project involves loading, displaying basic statistics, and plotting data from a Zomato dataset.

## Requirements

- Python 3.x
- pandas
- matplotlib

## Installation

To install the required Python packages, you can use pip:

```sh
pip install pandas matplotlib
```

## Usage

1. Place your Zomato dataset CSV file in the root directory of the project.
2. Update the `file_path` variable in the `main()` function if your file has a different name or path.

## Script Description

The script performs the following tasks:

1. **Load the Dataset**: 
    - Loads the dataset from a CSV file using pandas.
    - Handles any encoding errors that might occur during the loading process.

2. **Display Basic Statistics**: 
    - Prints basic statistics of the dataset using pandas' `describe()` method.

3. **Plot Data**: 
    - Plots a scatter plot of two specified columns from the dataset using matplotlib.

## Example

To run the script, execute the following command:

```sh
python your_script_name.py
```

Replace `your_script_name.py` with the name of your Python script file.

## Functions

- `load_data(file_path, encoding='utf-8')`: Loads the dataset from a CSV file.
- `display_basic_statistics(df)`: Displays basic statistics of the dataset.
- `plot_data(df, column_x, column_y)`: Plots data from the dataset.

## Main Function

The `main()` function:
1. Specifies the path to the CSV file.
2. Loads the dataset.
3. Displays basic statistics of the dataset.
4. Plots data from the dataset.

## Example Output

```
Basic Statistics:
       AggregateRating        votes
count       10000.000000  10000.000000
mean            3.654321   5000.123456
std             1.234567   1000.123456
min             1.000000   1000.000000
25%             2.500000   4000.000000
50%             3.500000   5000.000000
75%             4.500000   6000.000000
max             5.000000  10000.000000
```

A scatter plot of `votes` vs `AggregateRating` will be displayed.

## Notes

- Ensure that the column names `AggregateRating` and `votes` exist in your dataset. If they are named differently, update the `plot_data` function call in the `main()` function accordingly.
