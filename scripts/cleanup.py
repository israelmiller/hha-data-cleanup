#import packages
import pandas as pd
import numpy as np

#1. read in data
school_learning_modalities = pd.read_csv('data/school_learning_modalities.csv')

#2. Prints the number rows and columns in the dataset
rows = school_learning_modalities.shape[0]
columns = school_learning_modalities.shape[1]
print('There are {} rows and {} columns in the dataset'.format(rows, columns))

#3.lists the name of the columns in the dataset
list(school_learning_modalities)

#4. Clean Columns: Ensures all column names are lowercase and replaces spaces with underscores
school_learning_modalities.columns = school_learning_modalities.columns.str.lower().str.replace('[^A-Za-z0-9]+', '_')

#lists the name of the columns in the dataset to ensure they are all lowercase and have underscores
list(school_learning_modalities)

#prints the data types in the dataframe
school_learning_modalities.dtypes
#7. changes the dtype of "week" to datetime
school_learning_modalities['week'] = pd.to_datetime(school_learning_modalities['week'])

#5,6. defines a function 'cleanup' that uses a for loop to clean the data in the rows 
# by removing spaces, replacing them with '_', and removing special characters.
def cleanup():
    for column in school_learning_modalities.columns:
        if school_learning_modalities[column].dtype == 'object':
            school_learning_modalities[column] = school_learning_modalities[column].str.lower().str.replace('[^A-Za-z0-9]+', '_')
        else:
            pass
    return print('Data has been cleaned')
cleanup()

#lists a random sample of 10 rows from the dataset
school_learning_modalities.sample(10)

#8. looks for duplicate rows in the dataset and removes them
school_learning_modalities.drop_duplicates(inplace=True)

# checks for empty cells in the dataset and sets them to NaN
school_learning_modalities.replace(to_replace='', value=np.nan, inplace=True)
school_learning_modalities.replace(to_replace=' ', value=np.nan, inplace=True)

#9. Counts missing values in each column
school_learning_modalities.isnull().sum()

#10. Creates a column called "modality_inperson" that is a boolean value of whether the modality is in person or not

    #Defines a function that returns a boolean value of whether the modality is in person or not
def inperson(row):
    if row['learning_modality'] == 'in_person':
        return True
    else:
        return False

    #Applies the function to the dataframe
school_learning_modalities['modality_inperson'] = school_learning_modalities.apply(lambda row: inperson(row), axis=1)

    #lists a random sample of 10 rows from the 'learning_modality' and 'modality_inperson' columns to ensure the new column was created
school_learning_modalities[['learning_modality', 'modality_inperson']].sample(10)

    #counts the number of true and false values in the 'modality_inperson' column
school_learning_modalities['modality_inperson'].value_counts()

#Saves the cleaned dataset to a csv file
school_learning_modalities.to_csv('clean/school_learning_modalities_cleaned.csv', index=False)