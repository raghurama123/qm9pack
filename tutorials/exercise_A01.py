import qm9pack  # Import the qm9pack module

# Fetch the QM9 dataset and store it in a DataFrame
df = qm9pack.get_data('qm9')

# Print the summary statistics of the dataset
print(df.describe())

# Print the first 5 rows of the dataset
print(df.head())

# Print the last 5 rows of the dataset
print(df.tail())
