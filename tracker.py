# Project: Expense Tracker - Installment 5
# Author: Aubren Katriel P. Marquez
# Description: The Tracker has menus added

# Banner
print("=" * 40)
print("            EXPENSE TRACKER")
print("        Know where your money goes.")
print("=" * 40)
print()

# Questions asked once per run
name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")

subtotal = 0.0
count = 0

# Menu choices
while True:
    print(" MAIN MENU  ")
    print("  [1] Add an expense")
    print("  [2] View all expenses         (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")
    
    choice = input("Choose 1-4: ")
    
    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
            
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
        
    elif choice == "3":
        tax_amount = subtotal * (tax_percent / 100)
        grand_total = subtotal + tax_amount
        over_budget = grand_total - budget
        
        # Option 3 output
        print(f"  Expenses:\t{count}")
        print(f"  Subtotal:\t${subtotal:.1f}")
        print(f"  Tax ({tax_percent:.1f}%):\t${tax_amount:.1f}")
        print(f"  Grand total:\t${grand_total:.1f}")
        
        # Verdict Logic
        if grand_total > budget:
            print(f"  Over budget by ${over_budget:.1f}!")
        elif grand_total > (0.9 * budget):
            left = budget - grand_total
            print(f"  Careful: only ${left:.1f} left.")
        else:
            left = budget - grand_total
            print(f"  Within budget. ${left:.1f} left.")
            
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("----------------------------------------")
        print("Made by: Aubren Katriel P. Marquez  |  Installment 5")
        break
        
    else:
        print("  Please choose 1, 2, 3 or 4.")