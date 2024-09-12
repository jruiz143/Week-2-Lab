#Programming Exercise#3

#Write a program that asks the user to enter the total square feet,
#in a tract of land and calculates the number of acres in the tract

#Define acre footage
acre= 43560
#Asks user for square feet
owners_acre= float(input('Please provide total square feet of land:'))
#Calculate the number of acres based on input
Total_number_Acres= float(owners_acre / acre)
#Display the number of acres in tract
print (f"The Total Number of Acres: {Total_number_Acres:.2f}")