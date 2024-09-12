#Programming Exercise #2
#Write a program that asks the user to enter the projected amount of total sales,
#then displays the profit that will be made from that amount

#Define the profit value
profit_percentage= .23
#Ask user for total amount of sales
current_sales= float (input("Please enter Current Sales:"))
#Calculate the estimated profit
estimated_profit= profit_percentage*current_sales
#Display projected Annual Profit
print ("The Projected Annual Profit is: $", estimated_profit)