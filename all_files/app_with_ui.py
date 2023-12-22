# build the aplication with GUI
from tkinter import *
from talab import *
from PIL import Image , ImageTk

# method that open another window for result searching 
def show_another_window(result_got):
    root2 = Tk()
    root2.title("result")
    root2.config(bg="green")
    root2.minsize(width=750,height=550)
    if type(result_got) == str:
        labell = Label(root2,text="اسف الطلب مش في السجل",fg="red",bg="green",font=("helvetic",25,"bold")).pack()
    else:
        ### looping in result element to show it ###
        # cordinate of labels in results 
        t = 0
        z = 65
        label100 = Label(root2,text= f"نتائج البحث ",fg="red",font=("Helvetica",15,"bold"),bg="black").place(x= 250,y=0)
        label_gadwal_name = Label(root2,text= "الاسم",fg="blue",font=("Helvetica",12,"bold"),bg="black").place(x= 0,y=35)
        label_quantity = Label(root2,text= "الكميه",fg="blue",font=("Helvetica",12,"bold"),bg="black").place(x= 110,y=35)
        label_price = Label(root2,text= "السعر",fg="blue",font=("Helvetica",12,"bold"),bg="black").place(x= 220,y=35)
        label_date = Label(root2,text= "التاريخ",fg="blue",font=("Helvetica",12,"bold"),bg="black").place(x= 330,y=35)
        label_time = Label(root2,text= "الوقت",fg="blue",font=("Helvetica",12,"bold"),bg="black").place(x= 440,y=35)
        label_note = Label(root2,text= "ملاحظات",fg="blue",font=("Helvetica",12,"bold"),bg="black").place(x= 550,y=35)
        for element in result_got:
            for item in element:
                label11 = Label(root2,text=f"{item}",font=("Helvetica",11)).place(x=t , y=z)
                t += 110
            t = 0
            z += 30
    root2.mainloop()

# initialize ui 
root = Tk()

#control ui size 
root.minsize(900,510)

#add title
root.title("عالنوتة")
# background color 
root.config(bg="darkgray")

# add a head title 
head = Label(root,text="اهلا بيك في النوته",fg="red",bg="black",font=("Helvetica",18,"bold"),width=20,height=2).place(x=260,y=5)

# entry and label to show currunt home fund
# label_fund = Label(root,width=15,text= "masrof",font=("Helvetic",15,"bold"),fg='black',height=3).place(x= 10,y=10)
# label_home_fund = Label(root,font=("Helvetic",13,"bold"),text="ضيف مصروف البيت الجديد",bg="darkgray",fg="red").place(x=30,y=100)
# entry_fund = Entry(root,width=20,justify="center",font=("helvetic",10))
# sub_button_fund = Button(root,text="submit",fg="black",bg="blue"  ,font=("Helvetic",10,"bold")).place(x=60,y=160)
# entry_fund.place(x=30,y=130)

############add partition to add a new talab in nota############
## head of partition
label0 = Label(root,text="-:لو عايز تضيف طلبات جديدة",fg="red",font=("Helvetica",16,"bold"),width=20,bg="yellow").place(x=580,y=65)
# add talab name
label1 = Label(root,text="الاسم",bg="darkgray",width=10).place(x=230,y=100)
entry1 = Entry(root,width=25,justify="center",relief="solid")
# add quantity
label2 = Label(root,text="الكميه",bg="darkgray",width=10).place(x=430,y=100)
entry2 = Entry(root,width=5,justify="center",relief="solid")
# add price 
label3 = Label(root,text="السعر",bg="darkgray",width=5).place(x=520,y=100)
entry3 = Entry(root,width=10,justify="center",relief="solid")
# add notes
label4 = Label(root,text="ملاحظات",bg="darkgray",width=10).place(x=630,y=100)
entry4 = Entry(root,width=20,justify="center",relief="solid")

# method to add talab attribute to db 
def add_info():
    name = entry1.get()
    quantity = entry2.get()
    price = entry3.get() 
    notes = entry4.get()
    Talab(name,price,quantity,notes)
    # delete data in entries
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

# button submit
sub_button = Button(root,text="submit",fg="black",bg="red",font=("Helvetica",12,"bold"),relief="solid",command=add_info).place(x=500,y=125) 
fasla1 = Label(root,text="*******************************************************************************************************************",fg="red",bg="darkgray").place(x=250,y=160)
#display all entry wedget of add partiation
entry1.place(x=285,y=100)
entry2.place(x=485,y=100)
entry3.place(x=560,y=100)
entry4.place(x= 700,y=100)

#####search partition##### 
## search by name ##
# heading
head_search = Label(root,text="البحث في السجل ",fg="red",font=("Helvetica",15),bg="blue",width=40,height=2).place(x=330 ,y=175)
# searching by name

# search method that create another ui  to show result
def show_search_name():
    talabb_name = entry_name.get().lower()
    result = show_talab_by_name(talabb_name)
    entry_name.delete(0,END)
    show_another_window(result)
    
head_search_name = Label(root,text="-:البحث بواسطه الاسم",fg="white",bg="darkgreen",font=10,width=20).place(x=630,y=230)
label_name = Label(root,text="الاسم",font=5,bg="darkgray").place(x=650,y=260)
entry_name = Entry(root,font=5,width=10,relief="solid",justify="center")
search_button = Button(root,text="بحث",font=("Helvetica",12,"bold"),fg="red",bg="yellow",command= show_search_name).place(x=690,y=290)
entry_name.place(x=690,y=260)

##### search by date ####
head_search_date = Label(root,text="-:البحث بواسطه التاريخ",fg="white",bg="black",font=10,width=20).place(x=420,y=230)
#search method in specific date
def search_date():
    years = entry_date_years.get()
    monthes = entry_date_monthes.get()
    dayes = entry_date_dayes.get()
    date = years + "-" + monthes + "-" + dayes
    result = search_talab_by_specific_date(date)
    entry_date_years.delete(0,END)
    entry_date_monthes.delete(0,END)
    entry_date_dayes.delete(0,END)
    show_another_window(result)

label_years = Label(root,text="التاريخ",font=5,bg="darkgray").place(x=400,y=260)
# label for each part of date entry
entry_date_years = Entry(root,font=5,width=5,relief="solid",justify="center")
entry_date_monthes = Entry(root,font=5,width=5,relief="solid",justify="center")
entry_date_dayes = Entry(root,font=5,width=5,relief="solid",justify="center")
search_button = Button(root,text="بحث",font=("Helvetica",12,"bold"),fg="red",bg="yellow",command= search_date).place(x=500,y=310)
# display each entry
entry_date_years.place(x=440,y=260)
entry_date_monthes.place(x=500,y=260)
entry_date_dayes.place(x=560,y=260)
# labels to clear what each entry for 
label_y = Label(root,text="Y",font=5,bg="darkgray",fg="red").place(x=458,y=283)
label_y = Label(root,text="M",font=5,bg="darkgray",fg="red").place(x=518,y=283)
label_y = Label(root,text="D",font=5,bg="darkgray",fg="red").place(x=578,y=283)

#####search by range of date#####
head_search_range_date = Label(root,text="-: البحث بين تاريخين",fg="white",bg="blue",font=("Helvetica",15),width=20).place(x=550,y=340)
#search method in specific date
def search_date_rage():
    # to compine the date1 one elements
    years1 = entry_date_years1.get()
    monthes1 = entry_date_monthes1.get()
    dayes1 = entry_date_dayes1.get()
    date1 = years1 + "-" + monthes1 + "-" + dayes1
    # to compine the date2 one elements
    years2 = entry_date_years2.get()
    monthes2 = entry_date_monthes2.get()
    dayes2 = entry_date_dayes2.get()
    date2 = years2 + "-" + monthes2 + "-" + dayes2
    result = search_talab_inRange(date1,date2)
    ## to clear entry after search ##
    # for date 1
    entry_date_years1.delete(0,END)
    entry_date_monthes1.delete(0,END)
    entry_date_dayes1.delete(0,END)
    # for date 1
    entry_date_years2.delete(0,END)
    entry_date_monthes2.delete(0,END)
    entry_date_dayes2.delete(0,END)
    show_another_window(result)

# date 1
label_date1 = Label(root,text="التاريخ الاول",font=5,bg="darkgray").place(x=560,y=375)
# entry for each part of date1 
entry_date_years1 = Entry(root,font=5,width=5,relief="solid",justify="center")
entry_date_monthes1 = Entry(root,font=5,width=5,relief="solid",justify="center")
entry_date_dayes1 = Entry(root,font=5,width=5,relief="solid",justify="center")

# date 2
label_date2 = Label(root,text="التاريخ الثاني",font=5,bg="darkgray").place(x=560,y=400)
# entry for each part of date2 
entry_date_years2 = Entry(root,font=5,width=5,relief="solid",justify="center")
entry_date_monthes2 = Entry(root,font=5,width=5,relief="solid",justify="center")
entry_date_dayes2 = Entry(root,font=5,width=5,relief="solid",justify="center")

search_button = Button(root,text="بحث",font=("Helvetica",12,"bold"),fg="red",bg="yellow",command= search_date_rage).place(x=700,y=450)
# entry_name.place(x=480,y=260)
# display each entry for date 1
entry_date_years1.place(x=640,y=375)
entry_date_monthes1.place(x=695,y=375)
entry_date_dayes1.place(x=750,y=375)
# display each entry for date 2
entry_date_years2.place(x=640,y=400)
entry_date_monthes2.place(x=695,y=400)
entry_date_dayes2.place(x=750,y=400)
# labels to clear what each entry for 
label_y = Label(root,text="Y",font=5,bg="darkgray",fg="red").place(x=655,y=425)
label_y = Label(root,text="M",font=5,bg="darkgray",fg="red").place(x=710,y=425)
label_y = Label(root,text="D",font=5,bg="darkgray",fg="red").place(x=765,y=425)

##### for deleting talab from note ####
#metod to deleate
def deletey():
    name_del = entry_name_del.get()
    years = entry_date_years_del.get()
    monthes = entry_date_monthes_del.get()
    dayes = entry_date_dayes_del.get()
    date = years + "-" + monthes + "-" + dayes
    del_talab(name_del,date)
    entry_name_del.delete(0,END)
    entry_date_years_del.delete(0,END)
    entry_date_monthes_del.delete(0,END)
    entry_date_dayes_del.delete(0,END)
    label_del = Label(root,text="تم المسح بنجاح",fg="yellow",font=("Helvetica",10),bg="black").place(x=380,y=470)

#method to deleate label_del 
def ok():
    label_del = Label(root,text="................",fg="darkgray",bg="darkgray",font=("Helvetica",10)).place(x=380,y=470)

heading_label = Label(root,text=":لو عايز تمسح طلب",font=("Helvetica",12,"bold"),bg="red",fg="black").place(x=370,y=340)
#labels
label_date_del = Label(root,text="الاسم",font=5,bg="darkgray").place(x=370,y=375)
label_name_del = Label(root,text="التاريخ",font=5,bg="darkgray").place(x=370,y=400)
# entries
entry_name_del = Entry(root,font=5,width=10,relief="solid",justify="center")
entry_date_years_del = Entry(root,font=5,width=5,relief="solid",justify="center")
entry_date_monthes_del = Entry(root,font=5,width=5,relief="solid",justify="center")
entry_date_dayes_del = Entry(root,font=5,width=5,relief="solid",justify="center")
deleate_button = Button(root,text="مسح",font=("Helvetica",12,"bold"),fg="yellow",bg="red",command= deletey).place(x=400,y=435)
deleate_button = Button(root,text="ok",font=("Helvetica",12,"bold"),fg="red",bg="yellow",command= ok).place(x=360,y=435)
#display entries
entry_name_del.place(x=410,y=375)
entry_date_years_del.place(x= 410,y=400)
entry_date_monthes_del.place(x= 460,y=400)
entry_date_dayes_del.place(x= 510,y=400)

root.mainloop()