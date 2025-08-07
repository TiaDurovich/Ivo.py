
'''NOTE: This lesson focuses on variables and data types, NOT functions. Each task will therefore need to be run in its own file.'''

#  ----------------------------------------
# Task 1: Student Details
# ----------------------------------------

print("What is your given name on the card?", end=" ")
given_name = input("#")
print("What is your family name on the card?", end=" ")
family_name = input("#")
print("What is the SID on the card?", end=" ")
sid = input("#")

print(f"\nStudent Info:\nGiven Name: {given_name}\nFamily Name: {family_name}\nSID: {sid}\n")

# ----------------------------------------
# Task 2: Shout
# ----------------------------------------

print("Enter something to shout:", end=" ")
user_input = input("#")
print(user_input.upper())
print()

# ----------------------------------------
# Task 3: Running Total
# ----------------------------------------

total = 0
print(f"Running total is: {total}")
for i in range(3):
    print("Enter an integer:", end=" ")
    value = int(input("#"))
    total += value
    print(f"Updated running total is: {total}")
print()

# ----------------------------------------
# Task 4: Temperature Conversion
# ----------------------------------------

print("What degrees in Fahrenheit would you like to convert to Celsius?", end=" ")
f = float(input("#"))
c = round((f - 32) * 5/9)
print(f"That is roughly equivalent to {c} degrees Celsius.\n")

# ----------------------------------------
# Task 5: Weeks and Days Conversion
# ----------------------------------------

print("Enter a number of days:", end=" ")
days = int(input("#"))
weeks = days // 7
remaining_days = days % 7
print(f"That is {weeks} weeks and {remaining_days} days!\n")

# ----------------------------------------
# Task 6: Entrance Fee Calculator
# ----------------------------------------

print("Total adults:", end=" ")
adults = int(input("#"))
print("Total children (12 and below):", end=" ")
children = int(input("#"))

adult_price = 15.00
child_price = 6.00
service_tax = 0.06

adult_total = adults * adult_price
child_total = children * child_price
subtotal = adult_total + child_total
total_with_tax = subtotal * (1 + service_tax)

print(f"Total price for adults: ${adult_total:.2f}")
print(f"Total price for children: ${child_total:.2f}")
print(f"Total price inclusive service tax: ${total_with_tax:.2f}\n")

# ----------------------------------------
# Task 7: Coins to Wealth
# ----------------------------------------

print("5 cents:", end=" ")
c5 = int(input("#"))
print("10 cents:", end=" ")
c10 = int(input("#"))
print("20 cents:", end=" ")
c20 = int(input("#"))
print("50 cents:", end=" ")
c50 = int(input("#"))
print("1 dollar:", end=" ")
d1 = int(input("#"))
print("2 dollar:", end=" ")
d2 = int(input("#"))

total_cents = (
    c5 * 5 +
    c10 * 10 +
    c20 * 20 +
    c50 * 50 +
    d1 * 100 +
    d2 * 200
)

total_dollars = total_cents / 100
print(f"Total: ${total_dollars:.2f}")
