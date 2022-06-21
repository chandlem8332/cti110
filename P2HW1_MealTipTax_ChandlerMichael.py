    # Meal Tip Tax
    # 6-19-2022
    # CTI-110 P2HW1 - Meal Tip Tax Calculator
    # Michael Kord Chandler
    #

food_cost = int(input("Enter Food Cost: "))
print()
tip_perc = float(input("Enter Tip Percentage: "))
tax_perc = float(input("Enter Tax Percentage: "))
print()
cal_tip = food_cost * tip_perc
cal_tax = food_cost * tax_perc
print("Calcuated Tip: ", cal_tip)
print("Calcuated Tax: ", cal_tax)
print()
print("Total cost including tip and tax: ", food_cost + cal_tip + cal_tax)
