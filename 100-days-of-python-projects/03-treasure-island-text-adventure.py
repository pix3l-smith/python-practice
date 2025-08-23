# treasure ascii art
print("Welcome to Treasure Island!\nYou're quest is to find the treasure...")

# trail ascii art
print("You're trekking along the trail to treasure island when you reach a fork in the path. Which way do you go?")
direction = input("Type left or right: ").lower()

if direction == "right":
    print("You take the right fork, but it leads right to a chasm that you don't see until it's too late.\nGAME OVER")

elif direction == "left":
    # lake ascii art
    print("You take the left fork and come to a lake. You see an island in the middle of it. How do you cross?")
    crossing = input("Type swim or boat: ").lower()

    if crossing == "swim":
        print("You attempt to swim across to the island, but you're devoured by a crocodile.\nGAME OVER")
    
    elif crossing == "boat":
        # doors ascii art
        print("You take a boat across to the island. As you step ashore, you see 3 doors built into a rock face. Which door do you open?")
        door = input("Type red, blue or yellow: ").lower()

        if door == "yellow":
            print("You open the yellow door and are immediately overcome by terrifying monsters.\nGAME OVER")
        
        elif door == "red":
            print("You open the red door and step inside. The last thing you hear is a click before you're engulfed in flame.\nGAME OVER")
        
        elif door == "blue":
            print("You open the blue door and realise that by some miracle, you've found the treasure!\nYOU WON!")
        
        else:
            print("Invalid input.\nGAME OVER")
    
    else:
        print("Invalid input.\nGAME OVER")

else:
    print("Invalid input.\nGAME OVER")
