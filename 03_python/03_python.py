print("Welcome to the Pizza Hut!")
size= input("What is the size of the pizza you want? S, M or L: ")
pepporoni =  input("Do you want pepporoni? type Y for yes and N for no ")
Extra_Cheese = input(" Do you want extra cheese? Y or N ")
bill = 0
if size == "s":
    bill+= 15
    print("Small size pizza is $15")
elif size == "m":
    bill += 20
    print("Medium size pizza is $20")
elif size == "l":
        bill+= 25
        print("Lagre size pizza is $25")
else:
    print("You typed the wrong inputs:")
if pepporoni == "y":
    if size == "s":
        bill+= 2
    else:
        bill+= 3
if Extra_Cheese == "y":
    bill+= 1
print(f"Your final bill is:${bill}")
