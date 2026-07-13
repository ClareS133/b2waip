#USES USER-DEFINED FUNCTIONS
#tHIS PROGRAM WILL output an ASCII art image
# - - - - - - - -
#User-defined function
# - - - - - - - -
def outputapple(): #def command, which means "define a section of code", then choose a suitable name
	print("""
			.:'
			;
		  ____  :  __;
		:_____   _____ .
	       :_____________:
		:_____________
		  :__________ - ;
		    .__ .-. __	
		""")

#ASCII art image of an apple, which is the code that is part of the user-defined function

def outputhelloworld(): #def command, which means "define a section of code", then choose a suitable name
	print("""

		 _   _      _ _        __        __         _     _ _ 
		| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
		| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
		|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
        |_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)

		""")

#The code that is part of the user-defined function has to be below the line where it is defined
#It needs to be indented by two or four spaces
# - - - - - - - -
#Main program
# - - - - - - - -
outputhelloworld()#call the user-defined function to run
#as user-defined functions are separate from the main program, the code inside them will not execute until called