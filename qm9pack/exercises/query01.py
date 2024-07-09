import qm9pack

df=qm9pack.get_data('qm9')
a=df.describe()
print(a)

print(df.head())
print(df.tail())

#=== Print the header for all data
for key in df.columns:
    print(key)

#=== Print more details for a column
key='RotC_GHz'
qm9pack.helper(key)

#=== Print more details for all columns
for key in df.columns:
    qm9pack.helper(key)

#=== 


print("--------")
index=0

mol=df.iloc[index,]

print(mol)
print("--------")

ele=mol['Elements']

print(ele)

ele=mol['Stoichiometry']

#print(ele)

#===
#stoi="[9,5,0,1,3]"
#stoi="[6,2,0,1,0]"

#filtered_df = df[df['Stoichiometry'] == stoi]

#print(filtered_df)
#===
Nat=20
filtered_df = df[df['N_atoms'] == Nat]
print(filtered_df)


index=0
qm9pack.makexyz(index,df,'Mol_0.xyz')

index=1
qm9pack.makexyz(index,df,'Mol_1.xyz')
