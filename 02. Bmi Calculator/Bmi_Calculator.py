height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight)/float(height)**2

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")
