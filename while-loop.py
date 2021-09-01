#while loops run until a certain condition is met
players = 11

while players >= 5:
    print("The remaining players are", players)
    players -= 1

#break statement
#allows code to jump out of a loop whenever a certain condition is met
number = 0
while True:
    print("I love candy " + str(number))
    number +=1
    if number == 7:
        break

#continue statement
# allows us to jump back to the top of our loop
# continue keyword ignores all other statements under it and are not run
'''
in a team of 20, some numbers are taken and want to display the numbers
that are not taken so others don't  pick the picked numbers'''
#taken numbers
numTaken = [3,5,7,11,13]

print("Available numbers")

#loop
for i in range (1,21):
    if i in numTaken:
        continue
    print(i)
    