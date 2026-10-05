# Project: Expense Tracker - Installment 2
# Author: Aubren Katriel P. Marquez
# Description: Displays the landing page and main menu for the expense tracker.

# Banner
print("=" * 40)
print("             EXPENSE TRACKER")
print("       Know where your money goes.")
print("=" * 40)
print()

# Main Menu
print("MAIN MENU")
print("  [1] Add an expense       (coming soon)")
print("  [2] View all expenses    (coming soon)")
print("  [3] Show total spent     (coming soon)")
print("  [4] Exit                 (coming soon)")
print()

# User Input - Greeting & Expenses
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
print()

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

# Calculations
total = amount1 + amount2
average = total / 2

# Summary Output
print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1:<10} ${amount1}")
print(f"  - {item2:<10} ${amount2}")
print(f"Total spent:   ${total}")
print(f"Average:       ${average}")
print("-" * 40)
print(f"Made by: {name}  |  Installment 2")

