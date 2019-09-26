
d = 1    #used to keep the loop
e = " "  #define input 1
n = " "  #define input 2

while d == 1:								#comare to d, the var we will use to stay in loop, if changed it will break out of the loop 
	
	n = input("Type a word to begin (1/2)") #input a word to start
	if n == "exit":     					#Compare to the typed value, if its 'exit', it will exit the program (pt1)
		d = 0 								#break the loop
		print("Goodbye")

	if d == 1:								#if loop hasnt broken, move to the second var
		e = input("word #2 (2/2)")	#second input

	if e == "exit":                     	#Compare to the typed value, if its 'exit', it will exit the program (pt2)
		d = 0 								#break the loop
		print("Goodbye")
	
	if d == 1:								#make sure we havent broken the loop, if we have this function wont happen
		print("This is a demonstration with spacing :" + n) #string with a space before we link the var
		print("This is a demonstration without spacing:" + e) #string without a space before we link var
	
print("########## END ##########") #let the user know the program has terminated, wont happen unless we break the while loop
