# Hyperiondev-BootCamp-Projects
BootCamp Projects
# This is the Capstone Project for a financial calculation

'''
# This is Capstone Project for a financial calculation of an interest based on user input
# Explain to the user what words to enter to calculate the interest wether it is an investment or bond
# Ask the user to enter investment or bond and convert whatever a word entered to small letter using lower() function
# if user entered investment : ask the user to choose either simple or compound interest
# ask the user of what is the current interest rate and how much amount deposited as well as the number of years 
# base on what user entered earlier if simple/compound then use the right equation calculate the total money
  will be gained in that period and the interest rate applied and exit from the loop
# if user entered earlier the bond word then ask for the current value of the house and the current interest rate 
  and the number of the months needed then calculate the interest that will be applied using the given equation
  and display the amount then exit the loop 
# following the first request from user to enter a word either investment or bond, if any other words 
  entered print a text asking the customer to enter the right word.   
# 
'''

# Start 
# Explain to the user what they need to select and calculate 
print("investment - to calculate the amount of interest you will earn on your investment")
print("bond       - to calculate the amount you will have to pay on a home loan\n")

import math            #  Calling a mathematical function to be used later
amount_deposit = 0
interest_rate = 0
number_of_years = 0

# Ask to enter either investment or bond and convert it to a small letter 
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()
# If entered investment, ask to choose the type simple or compound 
if user_input == "investment":   
    # Request the required calculation values and use them for each investment type
    interest = input("Please enter the type of the interest (simple or compound): ").lower()
    interest_rate = int(input("Please input current interest rate (numbers only): ")) 
    r = interest_rate/100
    P = float(input("Please enter the amount is deposited (numbers only): £ "))
    t = float(input("Please enter the number of the years required (numbers only): "))
    # Check if user entered simple then do the required equation
    if interest == "simple":  
        A = P * (1+ r*t)
        print("The total amount you will get back is: £ ", A)
        # Check if user entered compound then do the required equation
    elif interest == "compound":
        A = P * math.pow((1+r),t)
        print("The total amount you will get back is: £ ", A)

# Check from the first entry if selected bond  
elif user_input == "bond":
    # Ask the user for the required values to apply the given equation 
    P = int(input("Please enter the present value of the house (numbers only): £"))
    interest_rate = int(input("Please input interest rate (numbers only): "))
    annual_interest_rate = interest_rate/100
    n = int(input("Please enter the months needed to repay the bond (numbers only): "))
    month_interest_rate = annual_interest_rate/12
    i = month_interest_rate
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print("The total money you will have to repay each month is: £ ", repayment)

  # At the beginning if entered a wrong word or numbers show an error message 
else:
    print("You have entered a wrong word, please try again")

## Please note that this is my first capston project to create and practice for HyperianDev Software Engineer BootCamp  😊
  
   
  
