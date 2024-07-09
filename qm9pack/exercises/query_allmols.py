import qm9pack                              # Import the qm9pack module
import os                                   # Import the os module
                                           
df = qm9pack.get_data('qm9')                # Fetch the QM9 dataset
                                           
filename = 'qm9_130831_molecules.xyz'       # Output filename

# Createthe output file
with open(filename, 'w') as f:
    pass

# Loop through each molecule in the dataset
for index in range(len(df)):
    tmpfile = 'mol_' + str(index) + '.xyz'  # Temporary filename

    qm9pack.makexyz(index, df, tmpfile)     # Create the XYZ file
    
    # Append contents to the main outputfile
    with open(tmpfile, 'r') as temp_file:
        contents = temp_file.read()
    
    with open(filename, 'a') as final_file:
        final_file.write(contents)
    
    os.remove(tmpfile)                      # Remove temporary file

