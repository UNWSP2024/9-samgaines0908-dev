# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

#Author: Sam Gaines
#Date: 3/262026
#Title: Item Counter

def count_file_lines():
    #######################
    with open('names.txt', 'r') as file:
            # Reads all the lines from the files
            lines = file.readlines()

            # This counts the number of lines/names
            num_names = len(lines)

            # This prints the result of it
            print(f'There are {num_names} names in the file.')




    ######################
    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()