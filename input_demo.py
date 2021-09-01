"""print("What is your name?")
name = input()

print("How old are you?")
age = int(input()) #int() function is used to conver the age into a number

print(name)
print(age)"""

import sys

name = sys.argv[1] #sys.argv is used to store user input from the console and store it in a list
age = sys.argv[2] 

print("How old are you?")
age = int(input())
print(name)
print(age)

