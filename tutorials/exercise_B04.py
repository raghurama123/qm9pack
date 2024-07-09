import qm9pack  # Import the qm9pack module

# Fetch the QM9 dataset and store it in a DataFrame
df = qm9pack.get_data('qm9')

# Save XYZ for a molecule using its index
index = 0
filename = 'Mol_0.xyz'
qm9pack.makexyz(index, df, filename)

index = 1
filename = 'Mol_1.xyz'
qm9pack.makexyz(index, df, filename)
