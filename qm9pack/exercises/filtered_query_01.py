import qm9pack  

df = qm9pack.get_data('qm9')

# stoichiometry is a string  of list with  number of H, C, N, O, and F atoms
stoi = "[6,2,0,1,0]" # Six H, two C, zero N, one O, and zero F

# Filter the DataFrame to match the stoichiometry 
filtered_df = df[df['Stoichiometry'].apply(lambda x: x == stoi)]

# Iterate over each row in the filtered DataFrame
for _, mol in filtered_df.iterrows():
    # Print SMILES and InChi for each molecule 
    print(mol['SMILES'], mol['InChi'],mol['Dipole_debye'])

