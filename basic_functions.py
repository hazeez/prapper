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


def fn_head_tail(df, user_cmd, row_arg):
    """
    Display the rows of the dataframe; head - top rows; tail - bottom rows
    :param df: dataframe
    :param user_cmd: head or tail
    :param row_arg: number of rows to display
    :return: head | tail, no of rows to display
    """
    try:
        rows = int(row_arg)
    except:
        print("Enter a valid 'number' of rows. E.g. {} 10".format(user_cmd))
        return None

    if user_cmd == "head":
        print(df.head(rows))

    if user_cmd == "tail":
        print(df.tail(rows))


def fn_hide_columns(df, columns_to_hide):
    """
    Hides an user inputted column
    :param df: dataframe
    :return: new column list without columns hidden
    """

    global hidden_columns_list

    if len(hidden_columns_list) > 0:
        print("Hidden columns: ", hidden_columns_list)

    df_columns_list = list(df.columns)
    # columns_to_hide = input("Enter the column to hide: ")

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
            print("columns '{}' does not exist in the dataframe.".format(columns_to_hide))
            print("Available columns: " + str(list(df.columns)))


def fn_sort_values(df, col_name, order):
    """
    Sort values in ascending order
    :param df: dataframe
    :param col_name: column to sort
    :param order: ascending or descending
    :return: modified df if valid columns; else return the original df
    """

    order_list = ['asc', 'desc']
    order_dict = {
        'asc': True,
        'desc': False
    }

    if col_name in df_columns_list:
        if order in order_list:
            df = df.sort_values(col_name, ascending=order_dict[order])
            print("Sorted column '{}' in order {}".format(col_name, order))
        return df
    else:
        print('Not a valid column')
        print("\n")
        return df
