#Lists are data types in python
#They are the equivalent of arrays in other languages
my_list = []
my_other_list = list()

list_a = ["a","b","c","d"] #list of strings
list_b = [1,2,3,4,5,6] #list of numbers
list_c = [1,"west",34,"longitude"] #mixed list

#nesting lists
list_d = [ ["a","b","c","d"], [1,2,3,4,5,6], [1,"west",34,"longitude"] ]

#Two lists can be joined using the extend() method
list_a = ["a","b","c","d"]
list_b = [1,2,3,4,5,6]

#join list_b to list_a
list_a.extend(list_b)

print(list_a)
print(list_b)

#append() function
#used to append values on the list
list_e = ["a","b","c","d"]
list_e.append("e")
print(list_e)

#arranging lists using the reverse() and sort() methods
list_e = ["a","b","c","d"]
list_e.reverse() #reverse() method reverses the list order
print(list_e) #['d', 'c', 'b', 'a']

#sort() method
list_f = ["e","d","c","b","a"]
list_f.sort()
print(list_f)

#reverse and sort methodsonly work on the lists they were called on and have no return values


