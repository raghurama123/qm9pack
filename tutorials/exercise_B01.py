import qm9pack  # Import the qm9pack module

# Fetch the QM9 dataset and store it in a DataFrame
df = qm9pack.get_data('qm9')

# Iterate over each column in the DataFrame and print the column name
for key in df.columns:
    print(key)
