# inbuilt modules
import os

# third party modules
import pandas as pd

# custom modules
import basic_functions as bf
import generic_functions as gfun
import config as cfg

# variable declarations
filename_object = ""

# print the splash screen at the start of the program
# This is the entry point of the program
gfun.fn_splash_screen()

while True:

    # global variables

    # local variables

    try:

        user_cmd = gfun.fn_get_input(filename_object)

        if user_cmd not in cfg.command_list:
            print("Command '{}' not available".format(user_cmd))
            bf.fn_help()
            continue

        if user_cmd == "read_csv":
            # execute the read_csv function
            file_name = input("Enter the file name: ")
            df = bf.fn_read_csv(file_name, pd)
            if df is not None:
                print(df.head())
                filename_object = file_name

        if user_cmd == "info":
            # execute the fn_dataframe function
            try:
                bf.fn_dataframe_info(df)
            except NameError:
                gfun.show_dataframe_not_present_error()
            except AttributeError:
                gfun.show_dataframe_not_present_error()

        if user_cmd == "rename_col":
            # execute the rename column function
            try:
                bf.fn_rename_col(df)
                print("\n")
                print("Column renamed: " + "\n" + str(df.columns))
            except NameError:
                gfun.show_dataframe_not_present_error()
            except AttributeError:
                gfun.show_dataframe_not_present_error()

        if user_cmd == "help":
            # execute the help function
            bf.fn_help()

        if user_cmd == "exit" or user_cmd == "exit()":
            # exit the program
            exit()

        if user_cmd == "dir":
            # list the directory contents
            print(os.system("dir"))

        if user_cmd == "head" or user_cmd == "tail":
            # print the head
            try:
                cmd, rows = bf.fn_head_tail(user_cmd)
                if not None:
                    if cmd == "head":
                        print(df.head(rows))
                    if cmd == "tail":
                        print(df.tail(rows))
            except NameError:
                gfun.show_dataframe_not_present_error()
            except AttributeError:
                gfun.show_dataframe_not_present_error()
            except ValueError as ve:
                print("Try again.")
            except TypeError as te:
                print("Try again.")

        if user_cmd == "columns" or user_cmd == "cols":
            # print the tail
            try:
                print(df.columns)
            except NameError:
                gfun.show_dataframe_not_present_error()
            except AttributeError:
                gfun.show_dataframe_not_present_error()

        if user_cmd == "cls" or user_cmd == "clear":
            # clear the screen
            gfun.clear_screen()

    except KeyboardInterrupt:
        print("\n")
        print("Exiting Prapper.")
        exit()
