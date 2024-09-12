#PROGRAMMING EXERCISE 12
#Write a program that displays: the amount of money paid for the stock,
#amount of commission Joe paid his broker when he bought the stock,
#amount joe sold the stock, commission joe paid his broker when stock sold, display money left

#Define Values for Purchase
shares_purchased= 2000 #original shares purchased
original_stock_dollars= 40 #dollars per share
purchase_commission_rate= .03 #percentage Joe paid his stockbroker
#calculations
total_amount_paid_for_stock= shares_purchased * original_stock_dollars
stockbroker_purchase_commission= total_amount_paid_for_stock*purchase_commission_rate
#define second half of problem
shares_sold=2000 #shares sold
stock_dollars_sold_price= 42.75 #Joe sold his stock at $42.75
sale_commission_rate=.03 #percentage he paid his broker when he sold his stocks
#Calculate
total_amount_sale=shares_sold*stock_dollars_sold_price
stockbroker_sold_commission=total_amount_sale*sale_commission_rate

remaining_money= (total_amount_sale-stockbroker_purchase_commission-stockbroker_sold_commission)
profit=remaining_money-total_amount_paid_for_stock

print (f"Joe paid ${total_amount_paid_for_stock} of stock." )
print (f"Joe paid ${stockbroker_purchase_commission} of commission to his stockbroker when he bought stock.")
print (f"Joe sold the stock for ${ total_amount_sale}.")
print (f"Joe paid ${stockbroker_sold_commission} of commission to his stockbroker when he sold stock.")
print (f"Joes has ${remaining_money} remaining left.")
