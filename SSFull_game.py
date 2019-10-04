mode = input("Please select a mode. Options are: \n1.SS1\n2.SS2\n3.SS3\nexit\n")
answer = " "

ex = 0
hold = 0
while ex == 0:
	if mode == "Skye":
		hold = 1
		answer = " "
		while hold == 1:
			answer = input("Greetings, creator. How was your travels?\nGreat \nMeh \nTerriable\n")
		
		
			if answer == "Great":
				print("Glad to hear! hope it stays that way.")
				hold = 0
			elif answer == "Meh":
				print("Oh, well hopefully it wasn't too much trouble.")
				hold = 0
			elif answer == "Terriable":
				print("well...that....sucks. Well here, have a cookie.")
				hold = 0
			else: 
				answer = input("Invalid response, try again.\n") 
		mode = "reset"
		hold = 0
	elif mode == "reset":
		print("DEBUG:Resetting game...")
		mode = "0"
		hold = 1
		while hold == 1:
			mode = input("Please select a mode. Options are: \n1.SS1\n2.SS2\n3.SS3\nexit\n")
			if mode == "Skye":
				hold = 0
			if mode == "exit":
				hold = 0
			if mode == "SS1":
				hold = 0
			if mode == "SS2":
				hold = 0
			if mode == "SS3":
				hold = 0				
	elif mode == "exit":
		print("Thanks for playing!\nJTP TECH")
		exit()
	elif mode == "help im stuck":
		hold = 1
		answer = " "
		while hold == 1:
			answer = input("Quick! Go grab a crowbar! Oh wait......")
			if answer == "exit":
				hold = 0
				mode = "reset"
			if answer == "help":
				print("The crickets chirp in the wind at your meaningless cries for help.")
