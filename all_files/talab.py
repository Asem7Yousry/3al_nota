import time
from tinydb import TinyDB , Query
from datetime import datetime , timedelta

# build a data base in json file for each talab
db = TinyDB("db.json")
talaby = Query()

#build an object for talab (order)
class Talab:
    def __init__(self, name,  price , quantity = 1, note = None):
        self.name = name
        self.price =price
        self.quantity = quantity
        self.note = note
        self.date = str(datetime.now().date())
        self.time = time.strftime("%p:%I:%M:%S")
        db.insert({
            "name":self.name,
            "quantity":self.quantity,
            "price":self.price,
            "date":self.date,
            "time":self.time,
            "note":self.note
        })
        
        
# function for deleting order from data base 
def del_talab(name, date):
    if db.search(talaby.date == date):
        db.remove(talaby.name == name)
        result = f"deleted successfully!"
    else:
        result = f"your order {name} is not exist in that date {date}"
    return result
 
# function for searching about talabat and represent it in list thet the newest represented first
def represent_talabat():
    list_OF_talabat =[]  # initialize list that will take orders values in side it 
    # to get all data in db
    all_talabat = db.all()
    talab_tuple = () # initialize tuple for each order(talab)
    # looping in in each order in db 
    for talab in all_talabat:
        #looping in each value in each order
        for value in talab.values():
            talab_tuple += (value,)
        list_OF_talabat.append(talab_tuple) # list consists of tuples each tuple consists of orders valeu
        talab_tuple = ()
    list_OF_talabat.reverse()
    return list_OF_talabat

# function for searching for talab by name in range of last one monthe
def show_talab_by_name(name):
    #initialize returned list
    returned_list = []
    # date of the day that user searches in 
    currunt_date = datetime.now().date()
    # to search for the last one monthe from the day of search
    limited_date = str(currunt_date - timedelta(weeks=8,days=5))
    # get all data base orders 
    all_db = represent_talabat()
    #looping in orders and get the last 2 monthes orders by date 
    for order in all_db:
        #to convert date from string to date type to compare it
        order_date = datetime.strptime(order[3],"%Y-%m-%d")
        limited_date_string = datetime.strptime(limited_date,"%Y-%m-%d")
        #compare if order that is in the range of last 2 monthes or not
        if order_date >= limited_date_string:
            if order[0] == name:
                returned_list.append(order)
        else:
            pass
    if returned_list == []:
        returned_list = f"sorry {name} could be not exist or not in last 2 monthes history, you could search by date."
    return returned_list

###functions for searching for talabat by date###

# search in specific date 
def search_talab_by_specific_date(date):
    # to get all talabat
    all_talabat = represent_talabat()
    #intiate returned talabat
    returned_talab = []
    for talab in all_talabat:
        if talab[3] == date:
            returned_talab.append(talab)
    return returned_talab

#search for talabat in range of dates
def search_talab_inRange(first_date, second_date):
    #to get all talabat in db
    all_talabat = represent_talabat()
    #intiate returned talabt
    searched_talabat = []
    #convert dates from string to data type to compare
    first_date = datetime.strptime(first_date, "%Y-%m-%d")  # older date
    second_date = datetime.strptime(second_date, "%Y-%m-%d")
    #looping
    for talab in all_talabat:
        date = datetime.strptime(talab[3],"%Y-%m-%d")
        if date >= first_date and date <= second_date:
            searched_talabat.append(talab)
    return searched_talabat
  
#method to deleate automaticly talabt from 4 monthes
def del_aotu():
    #initiate curunt date and date from 4 monthes
    curunt_date = datetime.now().date()
    compared_date = curunt_date - timedelta(weeks=17,days=2)
    #covert dates from date type to data type could be compared
    curunt_date = datetime.strptime(str(curunt_date),"%Y-%m-%d") 
    compared_date = datetime.strptime(str(compared_date),"%Y-%m-%d") 
    # to get all data
    all_date = represent_talabat()
    #looping
    for item in all_date:
        item_date = datetime.strptime(item[3],"%Y-%m-%d")
        if item_date < compared_date:
            del_talab(item[0],item[3])

#keep sure it deleats old orders in every single usage 
del_aotu()
