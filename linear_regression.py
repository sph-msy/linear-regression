"""
Exercise: Implementing Linear Regression from Scratch
Libraries used: Numpy, Pandas, Matplolib, Scikit-Learn

Dataset used: Boston housing dataset (https://www.kaggle.com/datasets/altavish/boston-housing-dataset)
"""

import pandas as pd

def import_data(datafile):
    # input: datafile: string, name of the datafile with extension
    # output: raw_data: Pandas data frame file
    raw_data = pd.read_csv(datafile)
    # print("Size=",raw_data.shape)
    return raw_data

def count_missing_values_rows(data):
    # Count the number of rows in data containing missing values
    # input: data (Panda dataframe file)
    # output: null_val_row_count (int)

    null_val_row_count = 0

    for i in range(len(data)): # loop on every row
        if data.iloc[i].isnull().sum()!=0:
            null_val_row_count += 1
            # print(data.iloc[i])

    print("Rows with missing values:",null_val_row_count,"/",len(data))

    return null_val_row_count

def clean_data(data):
    # print(data.head()) # print the header

    count_missing_values_rows(data)

    

    pass

def main():
    data = import_data("HousingData.csv")
    clean_data(data)

main()