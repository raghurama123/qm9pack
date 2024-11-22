import qm9pack
import os

df = qm9pack.get_data('qm9')

# Define the stoichiometry of interest in the order NH, NC, NN, NO, NF
stoi = "[4,6,1,1,1]" # corresponds to H4 C6 N1 O1 F1 or C6H4NOF

# Collect coordinates in a file
filename='QM9_subset_C6H4NOF.xyz'

# Extract subset of QM9 with the stoichiometry defined above
filtered_df = df[df['Stoichiometry'].apply(lambda x: x == stoi)]

Nmols=len(filtered_df)
print(f"{Nmols} molecules are found in QM9 for the defined stoichiometry")

# Print SMILES and the property of interest such as dipole moment
for _, mol in filtered_df.iterrows():
    print(f"{mol['SMILES']},{mol['Dipole_debye']}")

with open(filename, 'w') as f:
    pass

# Loop through each molecule in the subset
for index in range(len(filtered_df)):

    tmpfile = 'mol_' + str(index) + '.xyz'  # Temporary file

    qm9pack.makexyz(index, filtered_df, tmpfile)     # Create the XYZ

    with open(tmpfile, 'r') as temp_file:
        contents = temp_file.read()

    with open(filename, 'a') as final_file: # copy in filename
        final_file.write(contents)

    os.remove(tmpfile)                      # Remove temporary file
