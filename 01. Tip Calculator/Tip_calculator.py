"The program helps to find the total bill including tip"

print("Welcome to the tip calculator")
bill = float(input("What was your total bill? $ "))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay rupees: {final_amount}")
