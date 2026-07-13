#uses while loop and decision making
#guess the number program
mynumber=26#assign the secret number
print("Let's play a guessing game, what two-digit number am I thinking of?")#This line introduces the game to the user and prompts them to guess a two-digit number. It sets the stage for the game and encourages the user to participate.
while True:#This line starts an infinite loop that will continue until the user guesses the correct number. The loop allows the user to keep guessing until they find the right answer.
	usernumber = int(input("Guess a number:"))#This line prompts the user to enter their guess and converts the input from a string to an integer using the int() function. The user's guess is stored in the variable usernumber for further comparison with the secret number (mynumber).

	if usernumber < mynumber:#This line checks if the user's guess is less than the secret number. If it is, it means the user needs to guess a higher number.
		print("a little higher!")#This line provides feedback to the user, indicating that their guess was too low and encouraging them to guess a higher number in their next attempt.
	elif usernumber > mynumber:#This line checks if the user's guess is greater than the secret number. If it is, it means the user needs to guess a lower number.
		print("a little lower!")#This line provides feedback to the user, indicating that their guess was too high and encouraging them to guess a lower number in their next attempt.
	else:#This block executes if the user's guess is correct, meaning it matches the secret number (mynumber). It congratulates the user and breaks out of the loop to end the game.
		print("\nYou read my mind! It was " + str(mynumber) + ". well done!")#This line prints a congratulatory message to the user, including the correct number they guessed. The str() function is used to convert the secret number (mynumber) to a string so it can be concatenated with the rest of the message.
		break#This line breaks out of the while loop, ending the game since the user has guessed the correct number. The program will stop executing further iterations of the loop and will not prompt the user for more guesses.
#CHALLENGE, add a counter which increases with every guess, then outputs the number of guesses
guess_count = 0#This line initializes a variable called guess_count to 0. This variable will be used to keep track of the number of guesses the user has made throughout the game. Each time the user makes a guess, this counter will be incremented by 1, allowing the program to provide feedback on how many attempts it took for the user to guess the correct number.
while True:#This line starts an infinite loop that will continue until the user guesses the correct number. The loop allows the user to keep guessing until they find the right answer, while also keeping track of the number of guesses made.
	guess_count += 1#This line increments the guess_count variable by 1 each time the loop iterates, meaning every time the user makes a guess, the counter will increase. This allows the program to keep track of how many guesses the user has made throughout the game.
	usernumber = int(input("Guess a number:"))#This line prompts the user to enter their guess and converts the input from a string to an integer using the int() function. The user's guess is stored in the variable usernumber for further comparison with the secret number (mynumber). This line is executed every time the loop iterates, allowing the user to make multiple guesses until they find the correct number.

	if usernumber < mynumber:#This line checks if the user's guess is less than the secret number. If it is, it means the user needs to guess a higher number.
		print("a little higher!")#This line provides feedback to the user, indicating that their guess was too low and encouraging them to guess a higher number in their next attempt.
	elif usernumber > mynumber:#This line checks if the user's guess is greater than the secret number. If it is, it means the user needs to guess a lower number.
		print("a little lower!")#This line provides feedback to the user, indicating that their guess was too high and encouraging them to guess a lower number in their next attempt.
	else:#This block executes if the user's guess is correct, meaning it matches the secret number (mynumber). It congratulates the user and breaks out of the loop to end the game.
		print("\nYou read my mind! It was " + str(mynumber) + ". well done!")#This line prints a congratulatory message to the user, including the correct number they guessed. The str() function is used to convert the secret number (mynumber) to a string so it can be concatenated with the rest of the message.
		break#This line breaks out of the while loop, ending the game since the user has guessed the correct number. The program will stop executing further iterations of the loop and will not prompt the user for more guesses.
		print("It took you " + str(guess_count) + " guesses.")#This line prints the number of guesses the user took to find the correct number, using the guess_count variable that was incremented with each guess. The str() function is used to convert the guess_count integer to a string so it can be concatenated with the rest of the message. After printing this message, the break statement is executed to exit the loop and end the game.
		break#The break statement is executed to exit the loop and end the game.

#CHALLENGE, add a feature which allows the user to quit the game by entering a specific value, such as -1
guess_count = 0#This line initializes the guess_count variable to 0, which will be used to keep track of the number of guesses the user has made throughout the game. Each time the user makes a guess, this counter will be incremented by 1, allowing the program to provide feedback on how many attempts it took for the user to guess the correct number. This initialization is important to ensure that the counter starts at zero before any guesses are made.

while True:#This line starts an infinite loop that will continue until the user guesses the correct number or decides to quit the game by entering a specific value (in this case, -1). The loop allows the user to keep guessing until they find the right answer or choose to exit the game.
	guess_count += 1#increment the guess count with each iteration of the loop
	usernumber = int(input("Guess a number (or enter -1 to quit): "))#prompt the user to enter a guess or -1 to quit

	if usernumber == -1:#check if the user wants to quit the game
		print("Thanks for playing!")#print a goodbye message and exit the loop
		break#check if the user's guess is too low, too high, or correct
	elif usernumber < mynumber:#if the guess is too low, prompt the user to guess higher
		print("a little higher!")#This line if the guess is too low, prompts the user to guess lower
	elif usernumber > mynumber:#This line checks if the user's guess is too high, prompting them to guess lower
		print("a little lower!")#This line if the guess is too high, prompts the user to guess lower
	else:#This block executes if the user's guess is correct, congratulating them and showing the number of guesses taken
		print("\nYou read my mind! It was " + str(mynumber) + ". well done!")#This line prints a congratulatory message to the user, including the correct number they guessed
		print("It took you " + str(guess_count) + " guesses.")#This line prints the number of guesses the user took to find the correct number, using the guess_count variable that was incremented with each guess
		break
#This code is a simple number guessing game that uses a while loop to allow the user to keep guessing until they find the correct number. It also includes a counter to track the number of guesses and an option for the user to quit the game by entering -1.
#This code can be further enhanced by adding features such as a range for the secret number, multiple difficulty levels, or a leaderboard to track high scores.
#Overall, this code demonstrates the use of loops, conditionals, and user input in Python to create an interactive game.