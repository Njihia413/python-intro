#Dictionaries store collections of many values of different types
#Dictionary indexes do not have to be integers unlike lists
#Indexes in dictionaries are called keys
#The value is approximately called the value

#Creating dictionaries
my_dict = {}
my_dict = dict()

my_cat = {'name':'Mwihebs','age':5, 'color':'grey'}
print(my_cat)

#accessing values from the dictionary
cat_name = my_cat['name']
print(cat_name)

#adding items to a dictionary
birthdays = {"Mine":"July 1", "Babe":"August 8"}
birthdays["Mum"] = "February 16"
print(birthdays)

#using keys() method to get individual keys in the dictionary
print(birthdays.keys())
print(list(birthdays.keys()))

#setdefault() method
print("Enter a string:")
input_string = input()
characters = {}
for character in input_string:
    characters.setdefault(character,0) 
    characters[character] = characters[character] +1
    print(characters)
#setdefault() method creates a key for each character if the character does not exist in the dictionary
#the default value for each character is 0