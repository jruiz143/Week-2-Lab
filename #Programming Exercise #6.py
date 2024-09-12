#Programming Exercise #6
#Write a program that will ask the user to enter the amount
#of a purchase. The program should then compute the state and county 
#sales tax. The program should display the amount of the purchase, the state sales
#tax, the county sales tax, the total sales tax, and the total of the sale
#(which is the sum of the amount of purchasr plus the total sales tax)

state_tax_rate= .005
county_tax_rate= .025
#Ask user to input purchase price
purchase_price= float(input("Please enter purchase amount price: $"))
state_tax= float(purchase_price * state_tax_rate)
county_tax= float(purchase_price* county_tax_rate)
total_sales_tax= state_tax + county_tax
total_sales= purchase_price + total_sales_tax
#Display totals
print (f"Purchase Amount: ${purchase_price}")
print (f"State tax: ${state_tax:.2f}")
print (f"County Tax: ${county_tax:.2f}")
print(f'Total Sales Tax: ${total_sales_tax:.2f}')
print (f'Total Amount: $ {total_sales}')