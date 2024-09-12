#PROGRAMMING EXERCISE 8
#Write a program that calculates the total amount of a meal purchased.
#The program should ask to enter the charge for the food, then calculate amounts of 18% percent
#tip and 7% sales tax. Display each amounts and total

tip_rate= .18 #Tip rate percentage
tax_rate= .07 #Tax rate percentage
#Ask user for meal charged
meal_purchase= float(input("Please enter meal purchased price: $"))
tip= float(meal_purchase * tip_rate) #Calculate the tip 
sales_tax= float(meal_purchase* tax_rate) #Calculate the tax
total_amount= meal_purchase + tip + sales_tax #Calculate meal
#Display each value
print (f'Total Tip: ${tip:.2f}')
print (f'Total Sales Tax: ${sales_tax:.2f}')
print (f'Total Amount: ${total_amount:.2f}')
