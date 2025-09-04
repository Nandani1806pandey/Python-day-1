print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 0r 15? "))
people = int(input("How many people to split the bill? "))
tip_percentage = tip/100 
tip_amount = bill * tip_percentage
total = tip_amount + bill
peoples = total / people
final_amount = round(peoples, 2)
print(f"Each person should pay: ${final_amount}")