# inbuilt modules
import os
import re

# third party modules
import pandas as pd

# custom modules
import basic_functions as bf
import generic_functions as gfun
import config as cfg

# variable declarations
filename_object = ""
data = {'a':1, 'b':2}
df = pd.DataFrame(data, index=[0,1])


def parse_command(usercmd):
    args_list = []
    usercmd = usercmd.strip()

    # check if any arguments have the single quote or double quote

    regex = re.compile("[\'\"]")

    if usercmd.find("\'") != -1 or usercmd.find('\"') != -1:
        arguments = regex.split(usercmd)

        for item in arguments:
            if item != '':
                args_list.append(item.strip())
    else:
        args_list = usercmd.split(" ")

    cmd_args: list
    *cmd_args, = args_list

    if len(cmd_args) == 1:
        cmd = cmd_args[0]
        return [cmd]

    if len(cmd_args) == 2:
        cmd = cmd_args[0]
        param1 = cmd_args[1]
        return [cmd, param1]

    if len(cmd_args) == 3:
        cmd = cmd_args[0]
        param1 = cmd_args[1]
        param2 = cmd_args[2]
        return [cmd, param1, param2]

# print the splash screen at the start of the program
# This is the entry point of the program
gfun.fn_splash_screen()

while True:

    # global variables

    # local variables
    cmd_value = ""

    try:

        user_cmd = gfun.fn_get_input(filename_object)

        cmd_plus_args: list
        *cmd_plus_args, = parse_command(user_cmd)

        if len(cmd_plus_args) == 1:
            cmd_value = cmd_plus_args[0]

        if len(cmd_plus_args) == 2:
            cmd_value = cmd_plus_args[0]
            cmd_arg1 = cmd_plus_args[1]

        if len(cmd_plus_args) == 3:
            cmd_value = cmd_plus_args[0]
            cmd_arg1 = cmd_plus_args[1]
            cmd_arg2 = cmd_plus_args[2]

        if cmd_value not in cfg.command_list:
            print("Command '{}' not available".format(cmd_value))
            bf.fn_help()
            continue

        if cmd_value == "read_csv":
            # execute the read_csv function
            file_name = input("Enter the file name: ")
            df = bf.fn_read_csv(file_name, pd)
            if df is not None:
                print(df.head())
                filename_object = file_name

        if cmd_value == "info":
            # execute the fn_dataframe function
            try:
                bf.fn_dataframe_info(df)
            except NameError:
                gfun.show_dataframe_not_present_error()
            except AttributeError:
                gfun.show_dataframe_not_present_error()

        if cmd_value == "rename_col":
            # execute the rename column function
            try:
                bf.fn_rename_col(df)
                print("\n")
                print("Column renamed: " + "\n" + str(df.columns))
            except NameError:
                gfun.show_dataframe_not_present_error()
            except AttributeError:
                gfun.show_dataframe_not_present_error()

        if cmd_value == "help":
            # execute the help function
            bf.fn_help()

        if cmd_value == "exit" or cmd_value == "exit()":
            # exit the program
            exit()

        if cmd_value == "dir":
            # list the directory contents
            print(os.system("dir"))

        if cmd_value == "head" or cmd_value == "tail":
            if cmd_arg1:
                bf.fn_head_tail(df, cmd_value, cmd_arg1)
            else:
                bf.fn_head_tail(df, cmd_value, 5)

        if cmd_value == "columns" or cmd_value == "cols":
            # print the tail
            try:
                print(list(df.columns))
            except NameError:
                gfun.show_dataframe_not_present_error()
            except AttributeError:
                gfun.show_dataframe_not_present_error()

        if cmd_value == "cls" or cmd_value == "clear":
            # clear the screen
            gfun.clear_screen()

        if cmd_value == "hide_col":
            # hide the columns and display the dataframe
            # syntax: hide_col <col_name>
            print(cmd_value)
            print(cmd_arg1)
            
            try:
                display_column_list = bf.fn_hide_columns(df)
                df = df[display_column_list]
                print(df.head())
            except KeyError as ke:
                print("Try again " + str(ke))

        if cmd_value == "sort_values":
            # syntax: sort_values <col_name> <order>
            # syntax: sort_values <cmd_arg1> <cmd_arg2>
            try:
                if cmd_arg1 and cmd_arg2:
                    df = bf.fn_sort_values(df, cmd_arg1, cmd_arg2)

                if cmd_arg1 and not cmd_arg2:
                    df = bf.fn_sort_values(df, cmd_arg1, 'asc')

                print(df.head())
            except KeyError as ke:
                print("Column {} does not exist in the dataframe".format(ke))

    except KeyboardInterrupt:
        print("\n")
        print("Exiting Prapper.")
        exit()


# TODO: filtering the df based on columns
# TODO: Accessing based on iloc and loc
# TODO: save the df as a seperate file
# TODO: merge two or more dataframe
# TODO: append to a dataframe
# TODO: replace .nan values with other values
# TODO: setting the index
# TODO: deleting a dataframe from the memory
# TODO: aggregating based on value
# TODO: other methods of reading
# TODO: replacing column values
# TODO: replacing specific row / column value
# TODO: pivot feature
# TODO: logging feature
# TODO: tabulate module
# TODO: colorama
# TODO: if the dataframe is empty, remove the file name from the prompt
