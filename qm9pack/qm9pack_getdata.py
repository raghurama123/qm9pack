import os
import argparse
from datetime import datetime
from setuptools import find_packages, setup
from pkg_resources import resource_filename
import pandas as pd
import qm9pack

data_folder = resource_filename('qm9pack', 'data')

def get_data(dataset):

    #start_time = datetime.now()
    #formatted_datetime = start_time.strftime("%Y-%m-%d %H:%M:%S")

    #print('')
    #print(' Current Time:', formatted_datetime)

    df1 = pd.read_csv(os.path.join(data_folder, 'qm9_part1.csv'))

    df2 = pd.read_csv(os.path.join(data_folder, 'qm9_part2.csv'))

    df3 = pd.read_csv(os.path.join(data_folder, 'qm9_part3.csv'))

    # Concatenate the dataframes
    df = pd.concat([df1, df2, df3], ignore_index=True)

    # add polarizability
    polarizability_df = pd.read_csv(os.path.join(data_folder, 'qm9_polarizability.csv'))
    df = pd.merge(df, polarizability_df, on='XYZ_file', how='inner')

    #df=pd.read_csv(os.path.join(data_folder, 'qm9.csv'))

    #parser = argparse.ArgumentParser(description='Options for qm9')

    #parser.add_argument('--summary', action='store_true', help='Print a summary of the dataset')
 
    #args = parser.parse_args()
 
    #if args.summary:
    #    print('Data available:')
    #    print('---------------')
    #    columns=df.columns
    #    for icol, col in enumerate(columns):
    #        print(icol,col)
    #    print('Summary of numerical data:')
    #    print('--------------------------')
    #    print(df.describe())
    #    print('------------------')

    return df


