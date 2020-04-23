"""
To reduce clutter, all the generic functions i.e. functions that are specific to this program and not to pandas
are to be drafted in this module.

e.g. clear screen function
"""
# inbuilt modules
import os

# third party modules

# custom modules
import config as cfg


# local variables


def clear_screen():
    try:
        # for windows
        os.system("cls")
    except:
        # for linux / mac
        os.system("clear")


def fn_splash_screen():
    """
    Print the tool title
    :return: none
    """

    title = cfg.title
    ver = cfg.ver
    length_of_title = cfg.length_of_title

    clear_screen()

    print("\n")
    print(title, "v" + str(ver))
    print("-" * length_of_title)

    if cfg.help_msg:
        print(cfg.help_msg)

def fn_get_input(filename_object):
    """
    Get the pandas command from the user
    :return: command
    """
    print("\n")
    # global filename_object

    if filename_object == "" or filename_object is None:
        cmd = input("prapper>> ")
    else:
        cmd = input("prapper '" + filename_object + "'>> ")
    return cmd.strip()


def show_dataframe_not_present_error():
    """
    Show the generic error if dataframe is not initialized
    :return: None
    """
    print("Pandas dataframe not present.")
    print("Read the data file first. Use read_csv function to read the datafile")
