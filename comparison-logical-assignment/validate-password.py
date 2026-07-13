#using COMPARISON, LOGICAL and ASSIGNMENT operators
#password username checker program
actualpassword="password" #assignment operator
passwordentered = str(input("Enter your password ")) #assignment operator

if (passwordentered!=actualpassword): #relational operator 'not equal to'
	print("Invalid password")#This will be printed if the password entered by the user does not match the actual password stored in the program. The 'not equal to' operator is used to compare the two values and determine if they are different. If they are different, the condition evaluates to True and the message "Invalid password" is printed. If they are the same, the condition evaluates to False and the program continues to the else block, which prints "Valid password".
else:
	print("Valid password")#This will be printed if the password entered by the user matches the actual password stored in the program. The 'not equal to' operator is used to compare the two values and determine if they are different. If they are different, the condition evaluates to True and the message "Invalid password" is printed. If they are the same, the condition evaluates to False and the program continues to the else block, which prints "Valid password".

#CHALLENGE, now let's incorporate a username and LOGICAL operators
actualusername="Joe Bloggs" #assignment operator
usernameentered=str(input("Enter your name ")) #assignment operator
if (passwordentered!=actualpassword) or (usernameentered!=actualusername): #logical operator 'or'
	print("Invalid username")#This will be printed if either the password entered by the user does not match the actual password stored in the program, or if the username entered by the user does not match the actual username stored in the program. The 'or' operator is used to combine the two conditions and determine if either of them is True. If either condition is True, the message "Invalid username" is printed. If both conditions are False, meaning both the password and username are correct, the program continues to the else block, which prints "Valid username".
else:
	print("Valid username")#This will be printed if both the password entered by the user matches the actual password stored in the program, and if the username entered by the user matches the actual username stored in the program. The 'or' operator is used to combine the two conditions and determine if either of them is True. If either condition is True, meaning either the password or username is incorrect, the message "Invalid username" is printed. If both conditions are False, meaning both the password and username are correct, the program continues to the else block, which prints "Valid username".

#This program is not very secure, but it is a good example of how to use comparison, logical and assignment operators in Python.
#The program checks if the password and username entered by the user match the actual password and username stored in the program. If either the password or username is incorrect, it will print "Invalid username". If both are correct, it will print "Valid username".	
#This program can be improved by adding more features such as allowing the user to try again if they enter an incorrect password or username, or by using a more secure method of storing passwords such as hashing.
#Overall, this program is a simple example of how to use comparison, logical and assignment operators in Python to create a basic password and username checker.
