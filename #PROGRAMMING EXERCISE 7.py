#PROGRAMMING EXERCISE 7
#Write a Program that asks the user for the number of miles driven
#and the gallons of gas used. It should calculate the car's mpg and display result.

#Ask user for mileage
mileage= float(input("Please enter total miles driven: "))
gallons= float(input("Please enter total gallons of gas used: "))
mpg= float(mileage / gallons) #Calculate the mpg
print (f"Car's MPG: {mpg:.2f}") #Display Result