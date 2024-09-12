#PROGRAMMING EXERCISE 11
#Write a program that asks the user for the number of lions and tigers in
#at local zoo. Program should display % of lions in the exhibit.

#Define Variables based on user input
lions= int(input("Enter amount of Lions: "))
tigers= int(input("Enter amount of Tigers: "))
total_cats= lions+ tigers #calculate total of lions and tigers
#Define percentages, practice "if" statement, remember add :
if total_cats> 0:
      lion_percentage= (lions/total_cats) * 100
      tiger_percentage= (tigers/total_cats) * 100
else: print ("There are no lions or tigers to calculate percentages")
#Display total percentage
print (f'The percentage of lions can be calculated as: {lion_percentage:.2f}%')
print (f'The Percentage of tigers can be calculated as: {tiger_percentage:.2f}%')