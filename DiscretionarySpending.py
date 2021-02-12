#PROGRAM: DiscretionarySpending.py
#COURSE: ITSE 1311 20Z1
#AUTHOR: Stacey Nash
#DESCRIPTION: The program DiscretionarySpending.py calculates the amount of money that is left over after rent, utilities, and groceries have been paid. 


#Declare variables and collect input from the user

payAmt = input("Enter pay amount: $")
rent = input("Enter rent amount: $")
utilities = input("Enter utilities amount: $")
groceries = input("Enter groceries amount: $")

#Calculate totalBills, discretionaryAmount 

totalBills = float(rent) + float(utilities) + float(groceries)
discretionaryAmount = float(payAmt) - float(totalBills)

#Display payAmt, totalBills, and discretionaryAmount 

print("Pay: ${:,.2f}".format(float(payAmt)))
print("Total bills: ${:,.2f}".format(totalBills))
print("Discretionary amount: ${:,.2f}".format(discretionaryAmount))

#The following expression was shared in Feb. 11, 2021 virtual class ITSE 1302
# ${0:,.2f}".format(var) displays income with applicable commas and two decimal places
