---
title: 'QM9PACK: A Python package for data-mining the QM9 dataset'
tags:
  - Python
  - Chemical Space
  - Molecules
  - Data mining
authors:
  - name: Raghunathan Ramakrishnan
    orcid: 0000-0002-7288-9238
    equal-contrib: true
    affiliation: 1
affiliations:
 - name: Tata Institute of Fundamental Research Hyderabad, India
   index: 1
   ror: 01dagn361
date: 14 March 2025
bibliography: paper.bib

---

# Summary

QM9PACK is an open-source package designed to facilitate data mining of the 
QM9, one of the most widely used quantum chemistry datasets, containing approximately 130,000 small organic molecules. 
The package provides streamlined tools for data retrieval, preprocessing, and statistical analysis, 
enabling researchers to extract and analyze molecular properties rapidly. By offering 
the QM9 data in CSV format, QM9PACK simplifies integration with other Python modules 
such as Pandas, allowing for efficient querying, filtering, and data exploration. 
Additionally, QM9PACK presents a platform for augmenting the database with new data, 
including additional molecular properties, enabling researchers to expand and refine 
the dataset for further studies.


# Statement of need

The QM9 dataset contains structures and various properties computed using density functional theory (DFT) 
for over 130,000 small organic molecules containing a maximum of
nine main group atoms C|N|O|F [@ramakrishnan2014quantum]. 
The initial geometries of QM9 molecules were obtained as the 
SMILES representation[@weininger1988smiles] collected from the GDB17 database containing 166.4 billion molecular graphs[@ruddigkeit2012enumeration].
While extensively used, researchers often face challenges in efficiently accessing 
and processing the QM9 dataset in its raw, unstructured form [@qm9dataset]. QM9PACK addresses this gap by providing user-friendly 
Python interfaces, efficient data handling routines, and example codes for large-scale 
data exploration. The package also serves as a platform for discussing unit 
conventions, ensuring consistency in molecular property reporting. 
This is more often the case when calculating thermochemistry energetics [@ochterski2000thermochemistry]. 
[@sangala2024graph] is an example study using the QM9PACK to extract
a subset of QM9 molecules for training a graph neural network model.
Additionally, QM9PACK facilitates the augmentation of QM9 data with new molecular properties, 
allowing researchers to expand and refine the dataset. 
By offering data in CSV format, it enables seamless integration with Python-based workflows, making it easier for users 
to import, manipulate, and analyze quantum chemistry data within Python environments.

From a pedagogical perspective, QM9PACK provides an accessible entry point for students 
and researchers with a chemistry background to engage with quantum chemistry big data. 
By leveraging tools such as Pandas[@reback2020pandas, @mckinney2010],  NumPy[@harris2020array], Matplotlib[@Hunter2007], and Scipy[@2020SciPy] the package introduces data analytics techniques that help users extract insights from molecular property datasets efficiently. 
This is particularly beneficial for students who may not have prior 
experience in programming or large-scale data processing, but wish to learn modern data-driven 
approaches. QM9PACK bridges the gap between traditional quantum chemistry calculations and 
computational data science, fostering a deeper understanding of molecular trends and statistical 
analysis methods relevant to quantum chemistry.

# Implementation

The QM9 dataset contains minimum energy geometries and various properties of 133,885 molecules, 
calculated using the density functional theory method B3LYP and the 6-31G(2df, p) basis set. 
Among these, 3,054 molecules faced convergence issues during structure optimization and were excluded, 
resulting in a final dataset of 130,831 molecules. The 3,054 ‘uncharacterized’ molecules have been analyzed 
separately, highlighting the critical role of quantum chemistry approximations in establishing the correspondence 
between a molecular graph and its three-dimensional structure[@senthil2021troubleshooting]. 

QM9PACK is implemented in Python and leverages popular libraries such as NumPy, Pandas, and Scikit-learn. 
The package provides the QM9 dataset in an accessible CSV format, facilitating rapid data mining and statistical analysis. 
Users can efficiently query molecular properties based on multiple criteria, filter molecules by stoichiometry, 
and perform batch processing through a command-line interface (CLI).

With QM9PACK, users can import the QM9 dataset and quickly obtain a quick overview using:
```
import qm9pack
df = qm9pack.get_data('qm9')
print(df.describe())
```
Python codes for advanced queries are provided in separate files. The explanations of the queries are
provided in a tutorial-styled manual.

This retrieves the dataset as a Pandas DataFrame, allowing for seamless exploration of molecular properties, 
including Cartesian coordinates, vibrational frequencies, and thermochemical energies. The package includes 
utilities for retrieving constitutional isomers, extracting molecular substructures, and performing multi-property queries, 
such as filtering molecules based on dipole moments and HOMO-LUMO gaps.

Due to the efficiency of the Pandas library, augmenting the QM9 dataset with additional molecular properties is straightforward. Users can seamlessly merge new properties into the existing dataset using Pandas' built-in functions. For example, given a CSV file containing new molecular properties, users can integrate it with the original QM9 dataset as follows:
```
# df is the dataframe with original QM9 properties
newprop_df = pd.read_csv(os.path.join(data_folder, 'qm9_newprop.csv'))
df = pd.merge(df, newprop_df, on='XYZ_file', how='inner')
```
This framework can extend the QM9 dataset by incorporating additional molecular properties not included in the original dataset, such as NMR shielding[@gupta2021revving]. 

Structured workflows 
within the package guide users through data retrieval, transformation, and analysis, enabling reproducible 
research. Through an intuitive API, comprehensive tutorials, and integration with Jupyter notebooks, 
QM9PACK simplifies quantum chemistry data analysis, making it accessible to both 
experienced researchers and students. 


# Acknowledgements

We acknowledge the contributions of the quantum chemistry and machine learning communities for their valuable feedback. Special thanks to collaborators and testers who provided insights during the development of QM9PACK, often by requesting data in new form or additional properties. We acknowledge the support of the Department of Atomic Energy, Government of India, under Project Identification No. RTI 4007.

# References
