# Project: Expense Tracker - Installment 4
# Author: Aubren Katriel P. Marquez
# Description: The Tracker Makes Decisions

# Banner
print("=" * 40)
print("            EXPENSE TRACKER")
print("        Know where your money goes.")
print("=" * 40)
print()

# Main Menu
print("MAIN MENU")
print("  [1] Add an expense       (coming soon)")
print("  [2] View all expenses    (coming soon)")
print("  [3] Show total spent     (coming soon)")
print("  [4] Exit                 (coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

# First Expense
expense1 = input("First expense? ")
amount1 = float(input("Amount? "))

# Size message for Expense 1
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Second Expense
expense2 = input("Second expense? ")
amount2 = float(input("Amount? "))

# Size message for Expense 2
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

# Inputs for Tax and Budget
tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

# Calculations
subtotal = amount1 + amount2
average = subtotal / 2
tax_amount = subtotal * (tax_rate / 100)
grand_total = subtotal + tax_amount

over_budget = grand_total - budget

# Summary Output
print("----------------------------------------")
print("SUMMARY")
print(f"  - {expense1}:\t${amount1:.1f}")
print(f"  - {expense2}:\t${amount2:.1f}")
print(f"Subtotal:\t${subtotal:.1f}")
print(f"Average:\t${average:.1f}")
print(f"Tax ({tax_rate:.1f}%):\t${tax_amount:.1f}")
print(f"Grand total:\t${grand_total:.1f}")

# Verdict Logic using over_budget and ensuring no negative amount is shown
if grand_total > budget:
    print(f"Over budget by ${over_budget:.1f}!")
elif grand_total > (0.9 * budget):
    left = budget - grand_total
    print(f"Careful: only ${left:.1f} left.")
else:
    left = budget - grand_total
    print(f"Within budget. ${left:.1f} left.")

print("----------------------------------------")
print("Made by: Aubren Katriel P. Marquez  |  Installment 4")