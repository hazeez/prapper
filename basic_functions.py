"""
The following functions are covered in this file
- read_csv: read csv files
- rename_col: rename column
"""
# import third party modules
import pandas as pd

# variable declarations
hidden_columns_list = []
df_columns_list = []


def fn_read_csv(filename, pd):
    """
    Takes the csv file name and returns the dataframe
    :param filename:
    :param pd: pandas object
    :return: dataframe
    """
    global df_columns_list

    try:
        df = pd.read_csv(filename)
        df_columns_list = list(df.columns)
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
    print('-' * len("List of commands available..."))
    print("\n")
    command_list = {
        'Data Definition Commands': {
            'read_csv': 'reads a csv file',
        },
        'Data Query Commands': {
            'columns': 'display the list of columns in the dataframe',
            'dir': 'list the directory contents',
            'head': 'displays the first 5 rows of the dataframe',
            'info': 'displays current dataframe information',
            'tail': 'displays the last 5 rows of the dataframe',
        },
        'Data Manipulation Commands': {
            'hide_col': 'hide a selected column in the dataframe',
            'rename_col': 'renames a pandas dataframe column',
        },
        'Miscellaneous Commands': {
            'exit': 'exits the program',
            'help': 'displays help message',
        },
    }

    for category in command_list:
        print("* " + category)
        print("-" * (len(category) + 2))
        for x, y in command_list[category].items():
            print(" * {} : {}".format(x.rjust(12), y.ljust(5)))
        print("\n")


def fn_head_tail(user_cmd):
    """
    Display the rows of the dataframe; head - top rows; tail - bottom rows
    :param user_cmd: head or tail
    :return: head | tail, no of rows to display
    """
    if user_cmd == "head" or user_cmd == "tail":
        rows = input("Enter the number of rows to display: ")
        try:
            rows = int(rows)
            return user_cmd, rows
        except:
            print("Enter a valid 'number' of rows.")
            return None


def fn_hide_columns(df):
    """
    Hides an user inputted column
    :param df: dataframe
    :return: new column list without columns hidden
    """

    global hidden_columns_list

    if len(hidden_columns_list) > 0:
        print(hidden_columns_list)

    df_columns_list = list(df.columns)
    columns_to_hide = input("Enter the column to hide: ")

    if type(columns_to_hide) == str:
        columns_to_hide = columns_to_hide.strip()
        if columns_to_hide in df.columns:
            if columns_to_hide not in hidden_columns_list:
                hidden_columns_list.append(columns_to_hide)
            for col_name in hidden_columns_list:
                try:
                    df_columns_list.remove(col_name)
                except ValueError:
                    pass
            print("Column hidden")
            print("Visible columns: ", df_columns_list)
            print("\n")
            return df_columns_list
        else:
            print("columns '{}' does not exist.".format(columns_to_hide))
            print(df.columns)

def fn_sort_values(df):
    """
    Sort values in ascending order
    :param df: dataframe
    :return: modified df if valid columns; else return the original df
    """
    sort_column = input("Enter the column to sort: ")
    sort_column = sort_column.strip()

    if sort_column in df_columns_list:
        df = df.sort_values(sort_column)
        return df
    else:
        print('Not a valid column')
        print("\n")
        return df