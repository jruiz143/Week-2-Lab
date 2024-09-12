#PROGRAMMING EXERCISE 10
#Write a program that asks the user how many cookies he or she wants to make,
#then displays the number of cups of each ingredient needed for the specified number of cookies.

#define recipe variables
sugar= 1.5 #cups
butter= 1 #cup
flour= 2.75 #flour
recipe = 48 #cookies produce
#Ask User for Cookie input
cookies=float(input("Enter number of Cookies: "))
sugar_needed=(cookies*sugar)/recipe
butter_needed=(cookies*butter)/recipe
flour_needed=(cookies*flour)/recipe
#Display result
print (f"You need {sugar_needed:.2f} cups of sugar, {butter_needed:.2f} cups of butter, and {flour_needed:.2f} cups of flour to make {cookies} amount of cookies.")
