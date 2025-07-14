## 6.100A PSet 1: Part B
## Name: Ben White
## Time Spent: 0.3 hrs
## Collaborators: N/A

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################


yearly_salary=float(input("Enter your yearly starting salary: "))
portion_saved=float(input("Enter the portion of your salary to be saved. This should be in decimal form (e.g. 0.1 for 10%): "))
cost_of_dream_home=float(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter the semi-annual raise as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment=0.25
amount_saved=0.0
r=0.05
months=0
times_raised=0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################


while amount_saved < (cost_of_dream_home * portion_down_payment):
    amount_saved = amount_saved * (1 + (r/12))
    amount_saved = amount_saved + ((yearly_salary/12) * portion_saved)
    months = months + 1
    if (months // 6) > times_raised:
        yearly_salary = yearly_salary * (1 + semi_annual_raise)
        print(yearly_salary)
        times_raised += 1
    print(months, amount_saved)

print("Number of months: ", months)
