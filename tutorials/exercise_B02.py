import qm9pack  # Import the qm9pack module

# Fetch the QM9 dataset and store it in a DataFrame
df = qm9pack.get_data('qm9')

# Define a specific column name for which to print more details
key = 'RotC_GHz'

# Use the helper function from qm9pack to print more details for the 
# specified column
qm9pack.helper(key)
