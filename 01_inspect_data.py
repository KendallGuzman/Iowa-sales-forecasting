from pathlib import Path
import pandas as pd
#pandas work with tables and as pd is just a short name for it.
#pandas will be frequently used to read, clean, and analyze business data.

# Find the project folder from this script's location
project_root = Path(__file__).resolve().parent.parent
# __file__ = this script's location / Path(...)= treat that location as a file path / .resolve()= get its full location
# first .parent = go up to src / second .parent = go up to iowa-sales-forecasting
# The results are store in a variable called project_root

#Locate first CSV part
file_path = (
    project_root
    /"data"
    /"raw"
    / "iowa_liquor_sales_2024_1261_rows"
    / "iowa_liquor_sales_2024_1261_rows_part_0001.csv"
)  # This follows the folder until it reaches the file

# Read only five rows for inspection
sample = pd.read_csv(file_path, nrows=5)

print("COLUMN NAMES:")
print(sample.columns.tolist())

print("\nFIRST FIVE ROWS:")
print(sample.to_string(index=False))

# Select four columns from the sample
selected_columns = sample[
    ["ordered_on", "store_name", "store_city", "category_name"]
]
#Inner brackets contain a list of column names and outer brackets sample[] select those columns from the table
# Display the selected columns
print("\nSIMPLIFIED VIEW:")
print(selected_columns.to_string(index=False))

# Display one column name per line
for column in sample.columns:
    print(column)

# Inspect products and quantities
# Select the columns needed to understand a purchase line.
purchase_details = sample[
    ["store_name", "im_desc","sales_bottles", "sales_dollars"]
]
print("\nPURCHASE DETAILS:")
print(purchase_details.to_string(index=False))
# Each row lets us examine which store purchased which product, how many bottles, and fow what dollar amount.

# Calculate the recorded dollar amount per bottle.
sample["dollars_per_bottle"] = (
    sample["sales_dollars"] / sample["sales_bottles"]
)

print(
    sample[
        ["im_desc", "sales_bottles", "sales_dollars", "dollars_per_bottle"]
    ].to_string(index=False)
)

# Col types
sample.info()

# Convert data text into actual dates.
sample["ordered_on"] = pd.to_datetime(
    sample["ordered_on"],
    format="%Y-%m-%d"
)

# Check the type
print(sample["ordered_on"].dtype)