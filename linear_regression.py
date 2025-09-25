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

    print("Number of rows with missing values:",null_val_row_count,"/",len(data))

    return null_val_row_count

def analyse_and_fill_data(table, heatmap=True, histo=False):
    """
    Count the missing values in columns, determine if columns are filled with continuous or discrete data,
    Replace the missing values by median or mode values depending on the distribution.

    Input:
        table: panda DataFrame containing the whole dataset
        heatmap (default: True): if True, display the heatmap distribution of the missing value
        histo (default: False): if True, plot and display the histogram of every column

    Output:
        complete_data: panda DataFrame without any missing value anymore (everything is filled)
    """

    # # visualize the number of missing values for each columns
    # print(table.isnull().sum())

    # print("Number of columns with missing data:",(table.isnull().sum() != 0).sum(),"/",len(table.columns))

    # Visualize missing data
    if heatmap:
        plt.figure()
        plt.title("Distribution of the missing values")
        plt.imshow(table.isnull(), aspect="auto")
        plt.show()

    # we assume from the heatmap than data is MAR

    print("-" * 30)

    # for i in range(len(table.columns)):
    for column in table.columns:

        # print(f"Column {table.columns[i]} has {table.isnull()[i]} missing values")
        print(f"Column {column} has {table[column].isnull().sum()} missing values")

        # Visualize the data repartition
        if histo:
            plt.figure()
            # plt.hist(table.iloc[:,i], bins=20, xlabel=f"{table.iloc[0,i]}")
            table[column].plot.hist(bins=20, legend=True)
            plt.show()
        

        # For each column with missing values, check the number of unique values
        # and depending on the distribution, fill column with median or mode value

        if table[column].isnull().sum()>0:
            unique_values = table[column].nunique()
            print(f"Unique values: {unique_values}")
            
            # Check if the column is more likely to be discrete or continuous
            if unique_values < 20:  # You can adjust this threshold
                print(f"Column '{column}' is likely discrete.")
                table[column] = table[column].fillna(table[column].mode()[0])
                print(f"Column '{column}' missing values replaced with mode.")

            else:
                print(f"Column '{column}' is likely continuous.")
                # table[column].fillna(table[column].median(), inplace=True)
                table[column] = table[column].fillna(table[column].median())
                print(f"Column '{column}' missing values replaced with median value.")

        print("-" * 30)

    # print('test')
    # print(table.isnull().sum())

    # rename the filled data
    complete_data = table

    return complete_data
    
        


        

    

def preprocess_data(data):

    # print(data.head()) # print the header

    # count the number of rows with missing data
    nb_missing_val_rows = count_missing_values_rows(data)

    if nb_missing_val_rows>0:
        complete_data = analyse_and_fill_data(data, heatmap=False)

        # # test
        # print(complete_data.isnull().sum())
        

    

    

    

def main():
    data = import_data("HousingData.csv")
    preprocess_data(data)

main()