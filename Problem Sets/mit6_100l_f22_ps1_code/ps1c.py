## 6.100A PSet 1: Part C
## Name: Ben White
## Time Spent: 1 hrs
## Collaborators: N/A

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit=float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_house = 800000
portion_down_payment = 0.25
cost_of_down_payment = cost_of_house * portion_down_payment
months = 36
epsilon = 100
steps = 0
low = 0.0
high = 1.0
r = (high + low) / 2
amount_saved = initial_deposit * ((1+(r/12))**months)

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if initial_deposit - epsilon <= cost_of_down_payment:
    while abs(cost_of_down_payment - amount_saved) >= epsilon:
        r = (high + low) / 2
        amount_saved = initial_deposit * ((1+(r/12))**months)
        if abs(amount_saved) < cost_of_down_payment:
            low = r
        else:
            high = r
        if steps >= 100:
            r = None
            steps = 0
            break
        steps += 1

    print(f"Best savings rate: {r} [or very close to this number]")
    print(f"Steps in bisection search: {steps} [or very close to this number]")
else:
    print("You already have enough!")
