#Programming Exercise 9
#Write a program that converts Celsius temperatures to Fahrenheit temp. Formula:
# f= 9/5c + 32

#Define the celsius variable
celsius= float(input("Enter the temperature in Celsius: "))
#Change Celsius to Fahrenheit
celsius_to_fahrenheit= (celsius * 9/5) + 32
#Display the result
print (str(celsius)+ " Degree Celsius is equal to " + str(celsius_to_fahrenheit) + " Degree Fahrenheit.")