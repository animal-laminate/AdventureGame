print("----------4000CEM Week 4 Lab 2 Task----------")
print("--------------Bored Of The Dings-------------")
print("-----------------<G and Alf>-----------------")
print("\n")
print("THIS IS CHANGE 19.31 17.10.18")

print("You awake in a dark room.  Do you:")
print("a) Scream for help.")
print("b) Press the light switch")
x = input("Enter a or b: ")
if x == "a":
    print("Someone hears your screams...")
    print("Do you:")
    print("a) Do something else.")
    print("b) Do nothing else")
    x = input("Enter a or b: ")
    if x == "a":
        print("At a nested if")       
    elif x == "b":
        print ("At another nested if")
        print("Do you:")
        print("a) Exclaim loudly that you cannot possibly keep track of where you are in this game.")
        print("b) Say No problem I know exactly where I am")
        x = input("Enter a or b: ")
elif x == "b":
    print("The light comes on.")
    print("You do not recognise the room but you have a really bad feeling...")
    # Contine adventure Here
else:
    print("That was not an option.  Game Over")
