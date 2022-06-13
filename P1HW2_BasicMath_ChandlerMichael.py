# Basic Math Home Work
# 9th June 2022
# CTI-110 P1HW2 - Basic Math
# Michael Kord Chandler
#

expense = str(input("Enter name of expense: "))
charge = float(input("Enter monthly charge: "))
tax = charge * .06
monthly_charge = charge + tax
annual_charge = monthly_charge * 12

print("Monthly tax: ",tax)
print("Monthly charge: ",monthly_charge)
print("Annual charge: ",annual_charge)
