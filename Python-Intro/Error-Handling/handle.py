def get_age():
    print("How old are you?")
    try:
        age = int(input())
        return age
    except ValueError:
        return "That was not a valid input"    

print(get_age())

#try\except block is used to handle errors
#In the try block, we put in code that may throw an error
#In the except block we catch the thrown error and provide code to handle that error

'''
IndentationError - when you fail to separate code blocks properly.
NameError - when you call an undefined variable function or method.
TypeError - when you try and perform operations on unrelated types .
'''