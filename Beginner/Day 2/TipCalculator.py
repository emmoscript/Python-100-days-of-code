# Welcome
print("Welcome to the tip calculator.")

# Bill value
bill_value = float(input("What was the total bill? $"))

# Tip percentage
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# Quantity of people
people = int(input("What is the number of people in which the bill will be divided? "))

# Calculation
tip_percentage = tip / 100
tip_amount = bill_value * tip_percentage
total_bill = bill_value + tip_amount
bill_per_person = total_bill / people

# Result
result = round(bill_per_person, 2)
result = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${result}")
