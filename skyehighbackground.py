import turtle
#import gabesturtlepart.py



#def local variables
speed = 0
screenx = 1000
screeny = 700
debug = 5

#------------------------------------------------start of main()

	
def main(debug):
							#main function
	if debug == 5:
		debugInt() # setup debug if the value is left untouched
	
	deb("Entering function main()")
		
	draw_default(debug)
	
	
#------------------------------------------------end of main()


#-------------------------setup debug
def debugInt():
	debug = int(input("Debug ok? 1 = y; 2 = n: "))
	if debug == 1:
		print("Debug activated. ")
	elif debug == 3:
		confirm = input("WARNING::Editing screen size!!\nPROCEED WITH CAUTION!\nContinue? y/n ")
		if confirm == "y":
			print("SCREEN SIZE EDITOR")
			print("Current settings:x = " + screenx + " y = " + screeny)
			screenx = int(input("Enter screen pixel size X: "))
			screeny = int(input("Enter screen pixel size Y: "))
			print("New screen settings: x = " + screenx + " y = " + screeny)
		else:
			print("Skipping editor...")

	else:
		print("Skipping debug... ")
		debug = 0

#-------------------------end of debug int

#-------------------------debug message formater
def Debugmsg(msg):
	if debug == 1:
		
		print("DEBUG::" + msg)
						######DEBUG PRINTER######
def deb(msga):
	if debug == 1:
		print("DEBUG::" + msga)
#--------------------------
'''

#def turtle variables-----------------

deb("setup::Setting Turtle varaibles...")

turta = turtle.Turtle()

deb("setup::setup turtle instance (turta)")

screen = turtle.Screen()

deb("setup::setup turtle screen (screen)")
turta.speed(speed)

deb("setup::setup draw_speed (speed)")
	

turtle.setup(screenx, screeny)
deb("setup::setup screen_size (screenx,screeny)")
deb("Finished setting turtle variables")
#********************************************************************
#            ######### END OF SETUP ##########
#********************************************************************
deb("...ending setup")
'''



def water(flow, debug):
	#water flow 
	if debug == 1:
		print("DEBUG::Entering function water()")
	
#--------------------------------------------------start of draw_default
	
def draw_default(debug):
	if debug == 1:
		Debugmsg("Entering function draw_default()")
	#def turtle variables-----------------

	deb("setup::Setting Turtle varaibles...")

	turta = turtle.Turtle()

	deb("setup::setup turtle instance (turta)")

	screen = turtle.Screen()

	deb("setup::setup turtle screen (screen)")
	turta.speed(speed)

	deb("setup::setup draw_speed (speed)")
	

	turtle.setup(screenx, screeny)
	deb("setup::setup screen_size (screenx,screeny)")
	deb("Finished setting turtle variables")

	
	
	
	
	turta.penup()
	
	screenxpos = screenx * -1
	screenypos = screeny * -1
	deb("Inversed values for cursor position")
	screenxpos2 = screenx * 2
	screenypos2 = screeny * 2
	
	
	#screenx = screen
	
	turta.goto(screenxpos,screenypos)
	
	turta.fillcolor("blue")
	turta.begin_fill()
	if (screenx > screeny):
		if debug == 1:
			Debugmsg("X is bigger than Y drawing X...")
		turta.forward(screenxpos2)
		turta.left(90)
		turta.forward(screenxpos2)
		turta.left(90)
		turta.forward(screenxpos2)
		turta.left(90)
		turta.forward(screenxpos2)
		

	elif (screenx < screeny):
		deb("Y is bigger than X drawing Y...")
		turta.forward(screenypos2)
		turta.left(90)
		turta.forward(screenypos2)
		turta.left(90)
		turta.forward(screenypos2)
		turta.left(90)
		turta.forward(screenypos2)
	
	
	

	turta.end_fill()
	deb("ending fill")
#--------------------------------------------------------------------------------------------------------------------
	
	
#execute background script
#main(debug)

#------------------------------------------------start of if __name__
if __name__=='__main__':
	main(debug)

	turtle.exitonclick()
	#deb("turtle exiting on click")
	#turtle.Terminator()
	#deb("turtle terminated")

#------------------------------------------------end 
#turtle.mainloop()









deb("Exiting Background script (skyehighbackground)...")
#end of script


'''
#########################################################################################################################################################3
#sudo apt install python3-tk
	


wn = turtle.Screen()   # create a turtle
t = turtle.Turtle()
t.color('green')      # set the color
t.forward(50)         # draw a green line of leng
t.up()                # lift up the tail
t.forward(50)         # move forward 50 without drawing
t.right(90)           # change direction to the right, left works too
t.down()              # put the tail down
t.backward(100)       # draw a green line 100 units long
wn.exitonclick()
'''
