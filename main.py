# inbuilt modules
import os

# third party modules
import pandas as pd

# custom modules
import basic_functions as bf

# variable declarations

filename_object = ""
command_list = ['help', 'read_csv', 'info', 'rename_col', 'exit', 'dir', 'head', 'tail', 'columns']


def fn_splash_screen():
    """
    Print the tool title
    :return: none
    """
    title = "Prapper - (P)andas W(rapper)"
    ver = 0.1

    try:
        # for windows
        os.system("cls")
    except:
        # for linux / mac
        os.system("clear")

    print("-" * 30)
    print(title, "v" + str(ver))
    print("-" * 30)


def fn_get_input():
    """
    Get the pandas command from the user
    :return: command
    """
    print("\n")
    global filename_object

    if filename_object == "":
        cmd = input("prapper>> ")
    else:
        cmd = input("prapper '" + filename_object + "'>> ")
    return cmd.strip().lower()


def show_dataframe_not_present_error():
    """
    Show the generic error if dataframe is not initialized
    :return: None
    """
    print("Pandas dataframe not present.")
    print("Read the data file first. Use read_csv function to read the datafile")

# print the splash screen at the start of the program
# This is the entry point of the program
fn_splash_screen()

while True:

    user_cmd = fn_get_input()

    if user_cmd not in command_list:
        print("Command '{}' not available".format(user_cmd))
        print("\n")
        bf.fn_help()
        continue

    if user_cmd == "read_csv":
        # execute the read_csv function
        file_name = input("Enter the file name: ")
        df = bf.fn_read_csv(file_name, pd)
        if df is not None:
            print(df.head())
            print("-" * 30)
            filename_object = file_name

    if user_cmd == "info":
        # execute the fn_dataframe function
        try:
            bf.fn_dataframe_info(df)
        except NameError:
            show_dataframe_not_present_error()
        except AttributeError:
            show_dataframe_not_present_error()

    if user_cmd == "rename_col":
        # execute the rename column function
        try:
            bf.fn_rename_col(df)
            bf.fn_dataframe_info(df)
        except NameError:
            show_dataframe_not_present_error()
        except AttributeError:
            show_dataframe_not_present_error()

    if user_cmd == "help":
        # execute the help function
        bf.fn_help()

    if user_cmd == "exit" or user_cmd == "exit()":
        # exit the program
        exit()

    if user_cmd == "dir":
        # list the directory contents
        print(os.system("dir"))

    if user_cmd == "head":
        # print the head
        try:
            print(df.head(5))
        except NameError:
            show_dataframe_not_present_error()
        except AttributeError:
            show_dataframe_not_present_error()

    if user_cmd == "tail":
        # print the tail
        try:
            print(df.tail(5))
        except NameError:
            show_dataframe_not_present_error()
        except AttributeError:
            show_dataframe_not_present_error()


    if user_cmd == "columns":
        # print the tail
        try:
            print(df.columns)
        except NameError:
            show_dataframe_not_present_error()
        except AttributeError:
            show_dataframe_not_present_error()
