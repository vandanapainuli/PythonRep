def checkfun():
    day = 1
    while(day != 0):
        day = int(input("Enter any number, 0 to exit: "))
        match day:
            case 1 | 2 | 3 | 4 | 5:
                print("Today is a weekday")
            case 6 | 7:
                print("I love weekends!")
            case _:
                print("Invalid day number")
    else:2
        print("Exiting the program...")

checkfun()
