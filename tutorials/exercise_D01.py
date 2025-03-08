import qm9pack

# Load the QM9 dataset
df = qm9pack.get_data('qm9')

# Calculate isotropic polarizability
df['alpha_iso'] = (df['A_xx'] + df['A_yy'] + df['A_zz']) / 3

# Calculate the difference between computed and provided polarizability
df['diff_polarizability'] = df['alpha_iso'] - df['Polarizability_bohr3']

# Display first few rows to verify
print(df[['XYZ_file', 'alpha_iso', 'Polarizability_bohr3', 'diff_polarizability']].head())

# Summary statistics of the difference
print("Summary of Difference:")
print(df['diff_polarizability'].describe())
