#build a program to add daily orders from supermarkets 
from talab import *
import keyboard
import datetime

############ methods for app *************
# method for adding list o talabats in nota
def add_talabat():
    print("***************************************")
    while True:
        print("press GG to quit from adding list")
        name = input("talab name: ")
        if name == "GG":
            break
        quantity = float(input("quantity: "))
        price = float(input("price: "))
        note = input("note: ")
        Talab(name,price,quantity,note)

 # method to delete talab
def delete_talab():
    name = input("enter the talab you want to delete: ")
    choice = input("if talab you want to deleate is today press (y): " )
    if choice == "y":
        date = str(datetime.datetime.now().date())
    else:
        date = input("enter the date of talab you want it in way of (Y-M-D): ")
    print(del_talab(name, date))

#method to search in data base about talab
def search():
    choice = input(""" 
if you search for specific talab press in last monthes press(1)
for search for all talabat in specific date press(2)
for searching in range of dayes press (3)\n: """) 
    if choice == "1":
        name = input("talab name : ")
        result = show_talab_by_name(name)
    elif choice == "2":
        choice2 = input("if search date is today press (y): " )
        if choice2 == "y":
            date = str(datetime.datetime.now().date())
        else:
            date = input("enter the date of talab you want it in way of (Y-M-D): ")
        result = search_talab_by_specific_date(date)
    elif choice == "3":
        date1 = input("enter the older date of range of dayes you want it in way of (Y-M-D): ")
        date2 = input("enter the latest date of range of dayes you want it in way of (Y-M-D): ")
        result = search_talab_inRange(date1,date2)
    else:
        print("wrong option,try again")
    return result
    

#########################################    
########## the main programme ###########
while True:
    print("""
****** welcome in 3al Nota APP ******
for entering a new list press: 1
for deleting talab press: 2
for seacrching in nota history press: 3
for quit press:4""")
    choice = input("your choice : ")
    if choice == "1":
        add_talabat()
    elif choice == "2":
        delete_talab()
    elif choice == "3":
        print(search())
    elif choice == "4":
        break
    else:
        print("please enter number betwean 1 to 4")
    

