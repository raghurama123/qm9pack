def helper(key):
    help_content = {
        'XYZ_file': 'The file containing the XYZ coordinates of the molecule as submitted in the original QM9 article (https://doi.org/10.1038/sdata.2014.22). The name \'dsgdb9nsd_000001.xyz\' contain data for molecule-1 and so on. Overall, qm9 contains 130831 molecules',
        'Index': 'A unique identifier for each molecule in the dataset which ranges from 1 to 133885 of which 3054 will be missing as the corresponding molecular structures failed to converge with the DFT method, B3LYP, and the basis set, 6-31G(2df,p)',
        'SMILES': 'Simplified Molecular Input Line Entry System representation of the molecule.',
        'InChi': 'IUPAC International Chemical Identifier for the molecule.',
        'N_atoms': 'The number of atoms in the molecule.',
        'Stoichiometry': 'The stoichiometric formula of the molecule encoded as the array containing numbers of H, C, N, O, and F atoms. For CH4, the list corresponds to [4,1,0,0,0]',
        'Elements': 'List of elements present in the molecule. For CH4, the list is [\'C\',\'H\',\'H\',\'H\',\'H\']',
        'XYZ_Ang': 'The XYZ coordinates of the molecule in Angstroms calculated using the DFT method, B3LYP, and the basis set, 6-31G(2df,p).',
        'Mulliken_pop': 'Mulliken population analysis data for the molecule in units of charge of an electron, e.',
        'Harmonic_Freq_cmi': 'Harmonic vibrational frequencies of the molecule in cm^-1.',
        'RotA_GHz': 'Rotational constant A in GHz.',
        'RotB_GHz': 'Rotational constant B in GHz.',
        'RotC_GHz': 'Rotational constant C in GHz.',
        'Dipole_debye': 'Dipole moment of the molecule in debye.',
        'Polarizability_bohr3': 'Polarizability of the molecule in bohr^3.',
        'HOMO_au': 'Highest Occupied Molecular Orbital energy in atomic units, hartree.',
        'LUMO_au': 'Lowest Unoccupied Molecular Orbital energy in atomic units, hartree.',
        'HOMO_LUMO_gap_au': 'Energy gap between HOMO and LUMO in atomic units, hartree.',
        'R2_bohr2': 'Spread of the electron density calculated as the expectation value of the operator, R^2, in bohr^2',
        'ZOVE_au': 'Zero-point (harmonic) vibrational energy in atomic units, hartree',
        'InternalEnergy_0K_au': 'Internal energy of the molecule at 0 kelvin.',
        'InternalEnergy_298K_au': 'Internal energy of the molecule at 298.15 kelvin.',
        'Enthalphy_298K_au': 'Enthalpy of the molecule at 298.15 kelvin.',
        'GibbsFreeEnergy_298K_au': 'Gibbs free energy of the molecule at 298.15 kelvin.',
        'Heatcapacity_Cv_cal_mol_K': 'Heat capacity at constant volume in cal/(mol K).',
        'A_xx':'xx component of dipole electric field polarizability in bohr^3',
        'A_xy':'xy component of dipole electric field polarizability in bohr^3',
        'A_yy':'yy component of dipole electric field polarizability in bohr^3',
        'A_xz':'xz component of dipole electric field polarizability in bohr^3',
        'A_yz':'yz component of dipole electric field polarizability in bohr^3',
        'A_zz':'zz component of dipole electric field polarizability in bohr^3'
    }


    help_text = help_content.get(key, 'No help content available for this key.')

    print(f"'{key}': {help_text}")

    return help_text

def makexyz(index,df,filename):

    import numpy as np

    mol=df.iloc[index,:]

    ele=mol['Elements']

    coord=mol['XYZ_Ang']

    ele=ele.strip(']').strip('[').strip(',').split(',')
    atoms=[]
    for iele in ele:
        atoms.append(iele.strip("'"))

    coord=coord.strip(']').strip('[').strip(',').split(',')
    xyz=[]
    for icoord in coord:
        xyz.append(float(icoord.strip("'").strip(']').strip('[')))

    xyz=np.array(xyz)
    xyz=np.reshape(xyz,[len(atoms),3])

    xyzfile=open(filename,'w')

#   print(len(atoms))
    xyzfile.write(str(len(atoms))+'\n')
#   print(filename)
    xyzfile.write(filename+'\n')
    for i,atom in enumerate(atoms):
#       print('{:s}{:15.8f}{:15.8f}{:15.8f}'.format(atom,xyz[i][0],xyz[i][1],xyz[i][2]))
        xyzfile.write('{:s}{:15.8f}{:15.8f}{:15.8f}\n'.format(atom,xyz[i][0],xyz[i][1],xyz[i][2]))

    xyzfile.close()

    return
