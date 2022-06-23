# CTI-110
# P3HW2 - MealTipTax
# Michael Kord Chandler
# June 23rd 2022
#

cost = float(input("Please enter cost of meal: "))

tip = float(input("Enter tip amount of 15, 18, or 20: "))

tax = cost * .06

tipamount = tip/100 * cost

if tip == 15 or tip == 18 or tip == 20:
    print()
    print("Meal price: ", cost)
    print("Tax: ", tax)
    print("Tip: ", tipamount )
    print("Total: ", cost + tipamount + tax)
else:
    print("Error! You have entered an invalid tip amount. Please Rerun Program!")



