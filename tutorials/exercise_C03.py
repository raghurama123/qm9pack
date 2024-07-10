import qm9pack

df = qm9pack.get_data('qm9')

# Conversion factor from hartree to eV
hartree2ev = 27.211386245

# Define minimum and maximum values for Dipole moment and HOMO-LUMO gap (in eV)
min_dipole = 5.0
max_dipole = 8.0

min_gap = 2.0 / hartree2ev  # Minimum HOMO-LUMO gap converted to eV
max_gap = 5.0 / hartree2ev  # Maximum HOMO-LUMO gap converted to eV

# Combined condition to filter rows based on two criteria
combined_condition = (
    (df['Dipole_debye'] >= min_dipole) & (df['Dipole_debye'] <= max_dipole) &
    (df['HOMO_LUMO_gap_au'] >= min_gap) & (df['HOMO_LUMO_gap_au'] <= max_gap)
)

# Apply the combined condition to filter the DataFrame
filtered_df = df[combined_condition]

# Sort filtered DataFrame by 'Dipole_debye' column in ascending order
sorted_df = filtered_df.sort_values(by='Dipole_debye', ascending=True)

# Write SMILES, HOMO-LUMO gap (in eV), and Dipole moment to file
with open('multiquery.txt', 'w') as f:
    for _, mol in sorted_df.iterrows():
        f.write(f"{mol['SMILES']} {mol['HOMO_LUMO_gap_au'] * hartree2ev} {mol['Dipole_debye']}\n")


