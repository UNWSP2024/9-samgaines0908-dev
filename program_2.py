# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

#Author: Sam Gaines
#Date: 3/26/2026
#Title: Random Number File Writer

import random   #imports random numbers
def random_numbers_to_file():
    while True:
        try:                    # Asks user how many numbers up to 1000
            num_numbers= int(input("How many numbers would you like(up to 1000)? : "))
            if 1 <= num_numbers <= 1000:
                break
                # Handles any user errors, was not sure if I was supposed to add this.
            print("Please enter a number between 1 and 1000")
        except ValueError:
            print("Please enter a number that is valid between 1 and 1000")

    with open('random_numbers.txt', 'w') as file:
        for _ in range(num_numbers):
            random_number = random.randint(1,500)
            file.write(str(random_number) + '\n')

    print(f" {num_numbers} random numbers where writen as instructed ")

if __name__ == '__main__':
    random_numbers_to_file()







