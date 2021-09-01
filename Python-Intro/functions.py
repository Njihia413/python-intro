#Functions are blocks of code that begin with the def keyword
def fun_a():  #function declaration
    print("I have been called")
fun_a() #calling the function

#passing arguments to functions
def fun_a(a,b):
    print(a+b)
fun_a(1,4)    

#functions that take in keyword arguments
def fun_a(a=6,b=7):
    print(a+b)
fun_a()

#creating an empty function
def fun_a():
    pass

#functions with return values
def fun_a(a,b):
    return a + b

sum = fun_a(4,5)
print(sum)
