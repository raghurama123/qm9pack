import qm9pack

df = qm9pack.get_data('qm9')

# Get counts of unique values in the 'Stoichiometry' column, in descending order
value_counts = df['Stoichiometry'].value_counts(ascending=False)

# Iterating over each unique value and its count
for index, count in value_counts.items():
    print(f"{index}: {count}")  # Printing each unique value and its count


