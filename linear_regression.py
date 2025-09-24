"""
Exercise: Implementing Linear Regression from Scratch
Libraries used: Numpy, Pandas, Matplolib, Scikit-Learn

Dataset used: Boston housing dataset (https://www.kaggle.com/datasets/altavish/boston-housing-dataset)
"""

import pandas as pd
import matplotlib.pyplot as plt

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

def visualize_data(table):

    # count the number of rows with missing data
    count_missing_values_rows(table)

    # visualize the number of missing values for each columns
    print(table.isnull().sum())

    print("Number of columns with missing data:",(table.isnull().sum() != 0).sum(),"/",len(table.columns))

    # Visualize missing data
    plt.figure()
    plt.title("Distribution of the missing values")
    plt.imshow(table.isnull(), aspect="auto")
    plt.show()


    

def preprocess_data(data):
    # print(data.head()) # print the header

    visualize_data(data) # we assume from the heatmap than data is MAR

    

    pass

def main():
    data = import_data("HousingData.csv")
    preprocess_data(data)

main()