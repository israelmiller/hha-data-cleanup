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


Assignment Instructions:

1.     Loads the
data into python


2.     Prints the
count of columns and rows


3.     Provides a
print out of the column names


4.     Cleans the
column names


5.     Cleans the
strings that might exist within each column


6.     Assesses
white space or special characters


7.     Converts
the column types to the correct types (e.g., DOB field is datetime and not
object)


8.     Look for
duplicate rows and remove duplicate rows


9.     Assess
missingness (count of missing values per column)


10.  New data
field: attempt to create a new column called modality_inperson.  This
column should contain a binary value of true or false. Try to write a function that takes in the old column
name (learning modality), and recodes the value for a specific row to true, if
the learning modality value is ‘in-person’, and recodes it to false if the value
is either ‘remote’ or ‘hybrid
