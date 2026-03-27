# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all the numbers stored in the file and calculates their total.

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.

#Author: Sam Gaines
#Date: 3/27/2026
#Title: Average Numbers

def sum_numbers_from_file():
    ######################
    try:
        with open('names.txt', 'r') as file:
            total = 0
            count=0
            for line in file:
                try:    # This changes the value into an integer
                    number = int(line.strip())
                    total+= number
                    count+=1
                except ValueError:   #handles ValueError
                    print(f"Sorry: '{line.strip()}' is not a valid number please convert to a valid number ")

            if count > 0:
                print(f"total number of numbers is: {total}")
            else:
                print('Sorry you have entered an invalid number.')
            # This handles the IOError
    except IOError:
        print("Error reading the file.")
    except Exception as e:
        print(f"Sorry a error had occurred {e}")
    ######################
    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()

