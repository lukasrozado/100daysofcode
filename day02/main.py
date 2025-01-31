bill = int(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10 12 15 porcent"))
people = int(input("How many people to split the bill?"))
tip = tip/100
earchPearson = int(bill + (bill * tip))/people
print(f"Each person should pay: {earchPearson}" )
