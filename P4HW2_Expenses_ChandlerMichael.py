# CTI-110
# P4HW2 - Expences
# Michael Kord Chandler
# June 7th 2022


amount = float(input("Enter starting amount in account: $"))
keep_going = "y"
total = 0
count = 0
print()
while keep_going.lower() == "y":
    count +=1
    expense = float(input("Enter expense " + str(count) + ": $"))
    total += expense
    keep_going = input("Do you want to enter another expense?(y/n) :")
    print()

subtracted_amount = amount - total
print("Amount in account BEFORE expenses subtracted: $",format(amount,',.2f'),sep='')
print("Number of expenses entered: ", count)
print("Amount in account AFTER expenses subtracted is: $",format(subtracted_amount,',.2f'),sep='')

