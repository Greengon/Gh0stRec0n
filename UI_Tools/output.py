"""
This file will hold all the tools for creating output for
the user, from just printing to writing to a file by format.
"""


# Print file directly to the terminal
def print_to_user(file_name):
    with open(file_name, "r") as file_to_print:
        for line in file_to_print.readlines():
            print(line)
