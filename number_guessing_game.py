#!usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Sept 2019
# This program 


import random


def main():
    # comment
    
    random_number = random.randint(1,100+1)
    number_of_students = int(input("Enter your prediction: "))
    print("")
    
    if number_of_students == random_number:
        print("You got it right!")
    else:
        print("Not the right number! Try again!")
        
        
if __name__ == "__main__":
        main()
