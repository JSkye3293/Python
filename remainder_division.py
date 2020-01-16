# your code goes here
d = 0
while d == 0:
        

        n = float(input("please enter a numerator\n-> "))
        m = float(input("pease enter a divisor\n->  "))

        if m == 0:
            hold = 1
            while hold == 1:
        
                m = float(input("ERROR:Can not divide by 0, please try again\n-> "))
        
                if m > 0:
                    hold = 0
                    print("Moving on")
            

        a = str(n % m)
        ab = str(n // m)

        print("Quotient: " + ab + " Remainder: " + a)
