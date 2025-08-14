bill = 0

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25

else:
    print("Please enter a valid size (S, M or L).")

# Need to add loops for 'error' messages to allow question to repeat for an answer

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    
    else:
        bill += 3

elif pepperoni == "N":
    bill = bill

else:
    print("Invalid input. Do you want pepperoni on your pizza? Enter Y for yes or N for no: ")

cheese = input("Do you want extra cheese on your pizza? Y or N: ")

if cheese == "Y":
    bill += 1

elif cheese == "N":
    bill = bill

else:
    print("Invalid input. Do you want extra cheese on your pizza? Enter Y for yes or N for no: ")

print(f"Your total bill is ${bill:.2f}")
