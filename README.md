# hha-data-cleanup
 Assignment 2 for HHA 507: Data Science

 The file 'cleanup.py' in the scripts folder acomplishes the following tasks:

    1. Reads in the data from the 'School_Learning_modalities.csv' file in the data folder and creates a dataframe 
    2. Cleans the data by:
        - Modifies all column names and row values to be lowercase, replaces spaces and special characters with underscores.
        - Removes all rows that are duplicated.
        - Sets all rows with missing data to NaN.
        - Converts all columns to the correct data type.
    3. Writes the cleaned data to the data folder as a csv file named 'school_learning_modalities_cleaned.csv' 
