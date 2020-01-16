a = 1


print("Cash register program")
while a == 1:
        
    in1 = float(input("Enter amount for item 1: "))
    in2 = float(input("Enter amount for item 2: "))
    in3 = float(input("Enter amount for item 3: "))

    result = in1 + in2 + in3

    print("Total: " + str(result))
    hold = 1

    while hold == 1:
        paid = float(input("Enter amount paid: "))

        if paid >= result:
            hold = 0
            final = paid - result
            print("Change: " + str(final))
        if paid < result:

            rem = result - paid
            result = rem
            print("Remaining: " + str(rem))
