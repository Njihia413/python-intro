name = 'Maureen'
age = 20

print(f"My name is {name} and I am {age} years old")
#f stands for f-strings which allow us to put replacement fields {} with variable names inside our strings

#raw strings: Types of strings that allow us to ignore all escape characters(\)
print('Beyonce\'s lemonade stand')
print(r'Beyonce\'s lemonade stand') #r stands for raw string

'''
isalpha() - returns True if the string consists of letters only and is not blank
isalnum() - returns True if the string consists of numbers and letters and is not blank
isdecimal() - returns True if the string contains only numeric characters
isspace() - returns True if the string contains only space,tabs or new lines
istitle() - returns True if the string contains words that start with uppercase letters
'''

#Type Casting: Act of converting one type of data to another so as to manipulate it in some way
name = 'Atara'
age = 10

#str() method converts integers to strings
#int() method converts strings to integers
#float() method converts what is passed to a float
print("My name is " + name + " I am " + str(age) + " years old")

#Slicing Strings: Act of getting subsets or parts of strings,lists or tuples
greetings = 'Hello, Moringa!'
part_one = greetings[0:5] #0 is where to start slicing and 5 is where to stop but not including that position
print(part_one)

#negative indexes during slicing
greetings = 'Hello, Moringa!'
part_one = greetings[-8:-1] 
print(part_one)

#slicing without specifying last index
greetings = 'Hello, Moringa!'
part_one = greetings[0:]
print(part_one)

#slicing without specifying first index
number = [1,2,3,4,5,6,7,8,9]
four_digits = number[:4]
print(four_digits)