#Programming Exercise #4
#A customer in a store is purchasing 5 items. Write a program that asks 
#for the price of each item, then displays the subtotal of the sale, 
#the amount of sales tax, and the total

sales_tax_rate= 0.7 #Define Sales Tax Rate
Item1= float(input("Enter the first item price: "))#Ask customer for price of each item purchased
Item2= float(input("Enter the second item price: "))
Item3= float(input("Enter the third item price: "))
Item4= float(input("Enter the fourth item price: "))
Item5= float(input("Enter the fifth item price: "))
sub_total= (Item1 + Item2 + Item3 + Item4 + Item5) #Calculate total price of all items
sales_tax= sales_tax_rate*sub_total #Calculate sales tax
total= sales_tax + sub_total #calculate the total
#Display the totals
print (f"Subtotal: ${sub_total:.2f}")
print (f"Sales Tax: ${sales_tax:.2f}")
print (f"Entire Total: ${total: .2f}")