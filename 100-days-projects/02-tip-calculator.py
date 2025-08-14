print("Welcome to the tip calculator!")

initial_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much would you like to tip? (Don't include the % symbol) "))
# What happens if the person enters the percentage symbol? Figure out how to ignore that
# Same with entering a dollar sign in the first question; figure out how to ignore the dollar sign

tip_amount = initial_bill * (tip_percentage / 100)
total_bill = initial_bill + tip_amount

split_bill = total_bill / (int(input("How many people to split the bill? ")))

print(f"The total bill (including the tip) is ${total_bill:.2f}.\nThe amount that each person owes is ${split_bill:.2f}.")

# What happens when someone enters '0' for the split the bill question?
# There's still 1 person paying, so figure out how to make '0' print a response as if the answer was '1'
