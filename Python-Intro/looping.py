#for loop
#used when one wants to repeat something a number of times
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

#range() function takes two parameters, where to start the range and where to stop it
# list() method converts it to a list
list_a = list(range(0,5)) 
print (list_a)

#str() method converts the number i to a string so that we can concatenate it with the rest of the string 
for i in range(0,7):
    print("I would love " + str(i) + " cookies")

#looping with conditions
numbers = [1,2,3,4,5]
for i in numbers:
    if i % 2 == 0:
        print(i)
        

