print("choose 1 = thb to usd")
print("choose 2 = usd to thb")
choice = int(input("Enter your Choice 1 or 2 : "))
if choice == 1:
    thb = int(input("Enter your THB : "))
    amount_usd = thb / 35.5
    print("Your USD is : ",amount_usd)
elif choice == 2:
    usd = int(input("Enter your USD : "))
    amount_thb = usd * 35.5
    print("Your THB is : ",amount_thb)
else:
    print("Error Your Choice")    

