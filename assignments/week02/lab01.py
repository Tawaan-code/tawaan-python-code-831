weight = float(input("Enter your weight : "))
height = float(input("Enter yout height : "))
bmi = weight/height**2
if bmi >=30 : 
    print("obese")
elif 25 <= bmi < 30:
    print("overweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("underweight")
