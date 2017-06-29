print("This is you grocery list, looking nice and healthy. You know what they say an apple a day keeps the doctor away.")

groceryList = ["organic strawberries", "bluberries", "rasberries", "black berries", "apples", "peaches", "quinoa", "cucumbers"]

for x in groceryList:
    print(x)
print("We have amazing offers on our almond milk, Would you like to add 2 gallons of pure vanilla almond milk to your list?")

choice = input()
if (choice == "Yes" or "yes"):
        print("Great choice, personally I think this milk is better than the regular processed milk.")
        groceryList.append("vanilla almond milk")
        print(groceryList)


elif (choice == "no" or choice == "nah"):
        print(" You know this is a great price considering you wouldn't be drinking processed fatty cow milk. But maybe that's just me, Thank you for coming to the GWC organic store.")
        print(groceryList)
        exit()
