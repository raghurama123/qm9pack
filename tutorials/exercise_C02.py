import numpy as np
import qm9pack

df = qm9pack.get_data('qm9')

# Conversion constants from Hartree to other units
hartree2ev = 27.211386245
hartree2kcm = 627.5094740631
hartree2kJm = 2625.4996394799

# U0 for H, C, N, O, and F atoms from the manual (in atomic units)
U0_atoms = np.array([-0.500273, -37.846772, -54.583861, -75.064579, -99.718730])


# Selecting the molecule at index 0
index = 0
mol = df.loc[index]

# Extracting the internal energy of the molecule at 0 K in atomic units (au)
U0_mol = mol['InternalEnergy_0K_au']

# Extracting the stoichiometry of the molecule
stoi = mol['Stoichiometry']

# Convert the stoichiometry string to an array of float
str_list = stoi.strip('[]').split(',')
stoi = [float(num) for num in str_list]

# Calculating the atomization energy
U0_atomization = U0_mol - np.dot(stoi, U0_atoms)

print(f'Atomization energy is {U0_atomization:.8f} hartree')
print(f'Atomization energy is {U0_atomization * hartree2ev:.6f} eV')
print(f'Atomization energy is {U0_atomization * hartree2kcm:.5f} kcal/mol')
print(f'Atomization energy is {U0_atomization * hartree2kJm:.4f} kJ/mol')

