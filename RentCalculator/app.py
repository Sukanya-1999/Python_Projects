## inputs we need from the user
#total rent
#total food ordered for snacking
#electricity units spend
# charge per rent
#persons living in room/flat


##output
#total amount you have to pay is

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))


electricity_charges = electricity_spend * charge_per_unit

output = (food + rent + electricity_charges) // persons

print("Each person will pay = ", output)
