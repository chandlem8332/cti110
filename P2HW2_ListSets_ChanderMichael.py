# Lists and Sets Home Work
# 16th June 2022
# CTI-110 P2HW2 - Lists and Sets
# Michael Kord Chandler
#

mylist = []

num = float(input("Enter Num 1: "))
mylist.append(num)
num = float(input("Enter Num 2: "))
mylist.append(num)
num = float(input("Enter Num 3: "))
mylist.append(num)
num = float(input("Enter Num 4: "))
mylist.append(num)
num = float(input("Enter Num 5: "))
mylist.append(num)
num = float(input("Enter Num 6: "))
mylist.append(num)
print()
print("Created List")
print(mylist)
print("Smallest number in list: ",min(mylist))

print("Largest number in list: ",max(mylist))

print("Sum of the numbers in list: ",sum(mylist))

print("Average of numbers in list: ",sum(mylist)/len(mylist))
print()

print("Created set")

print(set(mylist))

input("Press enter to exit")

