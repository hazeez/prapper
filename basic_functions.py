"""
The following functions are covered in this file
- read_csv: read csv files
- rename_col: rename column
"""

import pandas as pd


def fn_read_csv(filename, pd):
    """
    Takes the csv file name and returns the dataframe
    :param filename:
    :param pd: pandas object
    :return: dataframe
    """
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("File '{}' is not present in the directory.".format(filename))
        print("Check file name once. Use the 'dir' command to view the directory contents.")
        return None


def fn_dataframe_info(df):
    """
    Take the dataframe and returns the information
    :param df: dataframe
    :return: dataframe information
    """
    return df.info()


def fn_rename_col(df):
    """
    Takes the dataframe
    :param df: dataframe
    :return: True
    """

    if df is not None:
        old_col_name = input("Enter the column name you want to rename: ")
        old_col_name = old_col_name.strip()

        if old_col_name not in df.columns:
            print("Column name {} not present in file".format(old_col_name))
            print("\n")
            print("list of columns available are ... ")
            print(df.columns)
            print("\n")
            fn_rename_col(df)
        else:
            new_col_name = input("Enter the new column name: ")
            new_col_name = new_col_name.strip()
            return df.rename(columns={old_col_name: new_col_name}, inplace=True)


def fn_help():
    """
    Print the help message
    :return: None
    """
    print("List of commands available...")
    command_list = {
        'columns': 'display the list of columns in the dataframe',
        'dir': 'list the directory contents',
        'exit': 'exits the program',
        'help': 'displays help message',
        'head': 'displays the first 5 rows of the dataframe',
        'info': 'displays current dataframe information',
        'read_csv': 'reads a csv file',
        'rename_col': 'renames a pandas dataframe column',
        'tail': 'displays the last 5 rows of the dataframe'
    }

    for x, y in command_list.items():
        print("{} : {}".format(x.rjust(12), y.ljust(5)))
