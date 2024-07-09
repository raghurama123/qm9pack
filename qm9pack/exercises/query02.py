import pandas as pd

df = pd.read_csv('/Users/rr/repos/qm9pack/qm9pack/data/qm9_part1.csv',index_col=False)

print(df)

index=0

mol = df.iloc[index, :]
print(mol)
