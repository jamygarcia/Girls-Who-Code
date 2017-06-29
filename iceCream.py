print("Welcome to the Jarianna Ice Cream parlor!")
print("What's your name?")
name = input()
if(name == "Diana" or name == "Anah" or name == "Jessica."):
    print("We don't serve people who break our codes.")
    exit()

print("How hungry are you %s?"%(name))
print("Hungry,Starving, or I'm boutta faint?")

choice = input()


if (choice == "I'm Hungry" or "hungry" or "im hungry"):
    print("so just one scoop?")

elif(choice == "Starving" or "I'm starving"):
    print("So just two scoops?")

elif(choice == "I'm boutta faint" or "faint"):
    print("Danggg you want three scoops?")
        
elif("I'm not hungry"):
     exit()

print("We got Madagascar Vanilla,Rainbow Sherbet,and Drizzling cookie dough.")

choice = input()
if(choice == "Madagascar Vanilla"):
   print("You're plain as H,E,double hockey sticks.")
elif(choice == "Rainbow Sherbet"):
     print("You sassy girl.")
elif(choice == "Drizzling cookie dough."):
    print("You're a loner.")
else:
     print("we don't got this here, what do you think this is Baskin Robbins?")


print("Cup or cone?")

choice = input()

if(choice == "cup"):
    print("Good choice, you're not a messy eater!")
   
elif(choice == "cone"):
    print("Be sure to grab a napkin on your way out.")

print("Here is a mediocore ice cream for a mediocore person.")
exit()
