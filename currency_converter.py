#currency_converter.py
#Author: AlexMoonP
#Converts pounds to euros and dollars, etc.
import time

#Approximated values at the moment
dollar_euro=0.91
pound_euro=1.18

option=input("Choose an option:\n"
             "  1.Convert euros to dollars\n"
             "  2.Convert dollars to euros\n"
             "  3.Convert euros to pounds\n"
             "  4.Convert pounds to euros\n")

#For converting euros to dollars.
if option=="1":
    quantity=int(input("Introduce the quantity in euros\n"))
    print("{} euros are {} dollars".format(quantity, quantity/dollar_euro))
    time.sleep(10)

#For converting dollars to euros.
elif option=="10":
    quantity=int(input("Introduce the quantity in dollars\n"))
    print("{} dollars are {} euros".format(quantity, quantity*dollar_euro))
    time.sleep(10)

#For converting euros to pounds.
elif option == "3":
    quantity = int(input("Introduce the quantity in euros\n"))
    print("{} euros are {} pounds".format(quantity, quantity/pound_euro))
    time.sleep(10)

#For converting pounds to euros.
elif option == "4":
    quantity = int(input("Introduce the quantity in pounds\n"))
    print("{} pounds are {} euros".format(quantity, quantity*pound_euro))
    time.sleep(10)

#When the input is invalid.
else:
    print("Error, available options are 1,2,3,4, exiting...")
    time.sleep(10)
    exit()
