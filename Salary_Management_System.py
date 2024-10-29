import mysql.connector as ctr
from matplotlib import pyplot as plt
import tkinter as tk
from functools import partial
from tkinter import ttk
from tkinter import messagebox

mycon = mycursor = plot_month = track_month = ""

necessities_ab = 0.0
wants_ab = 0.0
savings_ab = 0.0
monthly_aftertax_income = 0.0

manual_necessities = 0.0
manual_wants = 0.0
manual_savings = 0.0

cnd_for_budget_creation = ""

track_cnd = ""

def connect(password, database):
    global mycon
    global mycursor
    psd = password.get()
    db = database.get()
    mycon = ctr.connect(host = "localhost", user = "root", password = psd, database = db)
    if mycon.is_connected():
        print("Successfully connected to MySQL")
        print()
    mycursor = mycon.cursor()
    Menu()
    
def Login():
   
    tkwindow = tk.Tk()  
    tkwindow.geometry('400x150')  
    tkwindow.title('Salary Management System Login')

    tk.Label(tkwindow, text="Password").grid(row=0, column=0)
    password = tk.StringVar()
    tk.Entry(tkwindow, textvariable=password, show='*').grid(row=0, column=1)  
   
    tk.Label(tkwindow, text="Database").grid(row=1, column=0)
    database = tk.StringVar()
    tk.Entry(tkwindow, textvariable=database).grid(row=1, column=1)  
   
    validateLogin1 = partial(connect, password, database)

    tk.Button(tkwindow, text = "Login", command = validateLogin1).grid(row=2, column=0)
   
    tkwindow.mainloop()

def Create_Tables():
    mycursor.execute("Create table Housing(Month varchar(9), Income_from_Houses float, Rent_Paid float, House_Maintainance float, House_Insurance float, Other_Spending_on_houses float)")
    mycursor.execute("Create table Transportation(Month varchar(9), Vehicle_Loan float, Vehicle_Insurance float, Vehicle_Maintainance float, Fuel_Expenses float, Other_Transportation_Expenses float)")
    mycursor.execute("Create table Living_Expenses(Month varchar(9), Groceries float, Clothing float, Entertainment float, Other_Living_Expenses float)")
    mycursor.execute("Create table Health_Care(Month varchar(9), Medical_Insurance float, Medical_Expenses float)")
    mycursor.execute("Create table Child_Care(Month varchar(9), Tuition float, Other_Expenses_for_Child float)")
    mycursor.execute("Create table Miscellaneous(Month varchar(9), Pet_Care float, Hobbies float, Gifts_and_Donations float, Vacation float, Other_Miscellaneous_Expenses float)")
    print("All the tables have been created")
    print()
      
def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, text=field)
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, fill=tk.X)
        entries.append((field, ent))
    return entries

def Housing():
    root = tk.Tk()
    root.title('Housing Table')
    fields = 'Month', 'Income from Houses', 'Rent Paid', 'House Maintainance', 'House Insurance', 'Other Spending on Houses'
    ents = makeform(root, fields)
    root.bind(lambda event, e=ents: Housing_Values(e))    
    tk.Button(root, text='Submit', command=(lambda e=ents: Housing_Values(e))).pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
   
def Housing_Values(entries):
    value_list = []
    for entry in entries:
        value = entry[1].get()
        value_list.append(value)
    a = tuple(value_list)
    h1, h2, h3, h4, h5, h6 = a
    if float(h2)<0 or float(h3)<0 or float(h4)<0 or float(h5)<0 :
        messagebox.showinfo("Invalid Input!!", "Please enter positive values")
    else :
        mycursor.execute("insert into Housing values('{}',{},{},{},{},{})".format(h1, float(h2), float(h3), float(h4), float(h5), float(h6)))
        mycon.commit()
        print("Values were added to the Housing table")
   
def Transportation():
    root = tk.Tk()
    root.title('Transportation Table')
    fields = 'Month', 'Vehicle Loan', 'Vehicle Insurance', 'Vehicle Maintainance', 'Fuel Expenses', 'Other Transportation Expenses'
    ents = makeform(root, fields)
    root.bind(lambda event, e=ents: Transportation_Values(e))    
    tk.Button(root, text='Submit', command=(lambda e=ents: Transportation_Values(e))).pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

def Transportation_Values(entries):
    value_list = []
    for entry in entries:
        value = entry[1].get()
        value_list.append(value)
    a = tuple(value_list)
    t1, t2, t3, t4, t5, t6= a 
    if float(t2)<0 or float(t3)<0 or float(t4)<0 or float(t5)<0 or float(t6)<0:
        messagebox.showinfo("Invalid Input!!", "Please enter positive values")
    else :
        mycursor.execute("insert into Transportation values('{}',{},{},{},{},{})".format(t1, float(t2), float(t3), float(t4), float(t5), float(t6)))
        mycon.commit()
        print("Values were added to the Transportation table")
   
def Living_Expenses():
    root = tk.Tk()
    root.title('Living Expenses Table')
    fields = 'Month', 'Groceries', 'Clothing', 'Entertainment', 'Other Living Expenses'
    ents = makeform(root, fields)
    root.bind(lambda event, e=ents: Living_Expenses_Values(e))    
    tk.Button(root, text='Submit', command=(lambda e=ents: Living_Expenses_Values(e))).pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
   
def Living_Expenses_Values(entries):
    value_list = []
    for entry in entries:
        value = entry[1].get()
        value_list.append(value)
    a = tuple(value_list)
    l1, l2, l3, l4, l5 = a
    if float(l2)<0 or float(l3)<0 or float(l4)<0 or float(l5)<0 :
        messagebox.showinfo("Invalid Input!!", "Please enter positive values")
    else :
        mycursor.execute("insert into Living_Expenses values('{}',{},{},{},{})".format(l1, float(l2), float(l3), float(l4), float(l5)))
        mycon.commit()
        print("Values were added to the Living Expenses Table")
   
def Health_Care():
    root = tk.Tk()
    root.title('Health Care Table')
    fields = 'Month', 'Medical Insurance', 'Medical Expenses'
    ents = makeform(root, fields)
    root.bind(lambda event, e=ents: Health_Care_Values(e))    
    tk.Button(root, text='Submit', command=(lambda e=ents: Health_Care_Values(e))).pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
   
def Health_Care_Values(entries):
    value_list = []
    for entry in entries:
        value = entry[1].get()
        value_list.append(value)
    a = tuple(value_list)
    hc1, hc2, hc3 = a
    if float(hc2)<0 or float(hc3)<0 :
        messagebox.showinfo("Invalid Input!!", "Please enter positive values")
    else :
        mycursor.execute("insert into health_care values('{}',{},{})".format(hc1, float(hc2), float(hc3)))
        mycon.commit()
        print("Values were added to the Health Care Table")
   
def Child_Care():
    root = tk.Tk()
    root.title('Child Care Table')
    fields = 'Month', 'Tuition', 'Other Expenses for Child'
    ents = makeform(root, fields)
    root.bind(lambda event, e=ents: Child_Care_Values(e))    
    tk.Button(root, text='Submit', command=(lambda e=ents: Child_Care_Values(e))).pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
   
def Child_Care_Values(entries):
    value_list = []
    for entry in entries:
        value = entry[1].get()
        value_list.append(value)
    a = tuple(value_list)
    cc1, cc2, cc3 = a
    if float(cc2)<0 or float(cc3)<0 :
        messagebox.showinfo("Invalid Input!!", "Please enter positive values")
    else :
        mycursor.execute("insert into child_care values('{}',{},{})".format(cc1, float(cc2), float(cc3)))
        mycon.commit()
        print("Values were added to the Child Care Table")
   
def Miscellaneous():
    root = tk.Tk()
    root.title('Miscellaneous Table')
    fields = 'Month', 'Pet Care', 'Hobbies', 'Gifts and Donations', 'Vacation', 'Other Miscellaneous Expenses'
    ents = makeform(root, fields)
    root.bind(lambda event, e=ents: Miscellaneous_Values(e))    
    tk.Button(root, text='Submit', command=(lambda e=ents: Miscellaneous_Values(e))).pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
   
def Miscellaneous_Values(entries):
    value_list = []
    for entry in entries:
        value = entry[1].get()
        value_list.append(value)
    a = tuple(value_list)
    mv1, mv2, mv3, mv4, mv5, mv6 = a
    if float(mv2)<0 or float(mv3)<0 or float(mv4)<0 or float(mv5)<0 or float(mv6)<0:
        messagebox.showinfo("Invalid Input!!", "Please enter positive values")
    else :
        mycursor.execute("insert into miscellaneous values('{}',{},{},{},{},{})".format(mv1, float(mv2), float(mv3), float(mv4), float(mv5), float(mv6)))
        mycon.commit()
        print("Values were added to the Miscellaneous Table")
   
def Menu():
   
    tkwindow = tk.Tk()   
    tkwindow.geometry('1000x500')    
    tkwindow.title('Main Menu')   
    tk.Label(tkwindow, text ='Main Menu', font = ('Arvo', 30, 'bold')).pack()   
    pane = tk.Frame(tkwindow)   
    pane.pack(fill = tk.BOTH, expand = True)   
    tk.Button(pane,text='Create tables', command = Create_Tables, font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)   
    tk.Button(pane,text='Input values', command = Table_Menu, font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Check Plots', command = Which_Month_Plots, font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Create budget', command = MAI, font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Track budget', command = Which_Month_Track_Budget, font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()
  
def Table_Menu():
   
    tkwindow = tk.Tk()
    tkwindow.geometry('1000x500')
    tkwindow.title('Table Menu')
    tk.Label(tkwindow, text ='Table Menu', font = ('Arvo', 30, 'bold')).pack()   
    pane = tk.Frame(tkwindow)
    pane.pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Housing', command = Housing,font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Transportation', command = Transportation,font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Living Expenses', command = Living_Expenses,font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Health Care', command = Health_Care,font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Child Care', command = Child_Care,font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Miscellaneous', command = Miscellaneous,font=('Arvo', 20), foreground='Green').pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()
   
def Which_Month_Plots():
   
    tkwindow = tk.Tk()
    tkwindow.title('Choosing Month for Plots')
    tkwindow.geometry('500x250')
    tk.Label(tkwindow, text = "Monthly Analysis", background = 'green', foreground ="white", font = ("Times New Roman", 15)).grid(row = 0, column = 1)
    tk.Label(tkwindow, text = "Select the Month :", font = ("Times New Roman", 10)).grid(column = 0, row = 5, padx = 10, pady = 25)
    monthchoosen = ttk.Combobox(tkwindow, width = 27, values=('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
    monthchoosen.grid(column = 1, row = 5)

    def selectmonth_action():        
        global plot_month    
        plot_month = monthchoosen.get()
        if plot_month == "":
             messagebox.showinfo("NO INPUT", "Kindly choose something")
        elif plot_month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
             messagebox.showinfo("WRONG INPUT", "Kindly use the dropdown")
        else:
            print(plot_month,"is chosen for checking Plots")
    ttk.Button(tkwindow, text="Get Value", command = selectmonth_action).grid(column = 3, row = 5)
    ttk.Button(tkwindow, text="Submit", command = Plot_Menu).grid(column = 3, row = 6)
    tkwindow.mainloop()
   
def Plot_Menu():
   
    tkwindow = tk.Tk()
    tkwindow.geometry('1000x500') 
    tkwindow.title("Plot Menu")
    tk.Label(tkwindow, text ='Plot Menu', font = ('Arvo', 30, 'bold')).pack()
    pane = tk.Frame(tkwindow)
    pane.pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Housing',font=('Arvo', 20), foreground='Green',  command = Plot_Housing).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Transportation',font=('Arvo', 20), foreground='Green',command = Plot_Transportation).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Living Expenses',font=('Arvo', 20), foreground='Green',command = Plot_Living_Expenses).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Health Care', font=('Arvo', 20), foreground='Green',command = Plot_Health_Care).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Child Care',font=('Arvo', 20), foreground='Green',command = Plot_Child_Care).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Miscellaneous',font=('Arvo', 20), foreground='Green', command = Plot_Miscellaneous).pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()
   
def Plot_Housing():
    tkwindow = tk.Tk()
    tkwindow.geometry('500x250')
    tkwindow.title("Plots for Housing Table")
    k = tk.Label(tkwindow, text ='Data Analysis', font = ('Arvo', 40, 'bold'))
    k.pack()
    pane = tk.Frame(tkwindow)
    pane.pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Bar Graph',font=('Arvo', 20),foreground='Green', command = bg_Housing).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Pie Chart',font=('Arvo', 20),foreground='Green', command = pg_Housing).pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()

def Plot_Transportation():
    tkwindow = tk.Tk()
    tkwindow.geometry('500x250')
    tkwindow.title("Plots for Transportation Table")
    k = tk.Label(tkwindow, text ='Data Analysis', font = ('Arvo', 40, 'bold'))
    k.pack()
    pane = tk.Frame(tkwindow)
    pane.pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Bar Graph',font=('Arvo', 20),foreground='Green', command = bg_Transportation).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Pie Chart',font=('Arvo', 20),foreground='Green', command = pg_Transportation).pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()
   
def Plot_Living_Expenses():
    tkwindow = tk.Tk()
    tkwindow.geometry('500x250')
    tkwindow.title("Plots for Living Expenses Table")
    k = tk.Label(tkwindow, text ='Data Analysis', font = ('Arvo', 40, 'bold'))
    k.pack()
    pane = tk.Frame(tkwindow)
    pane.pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Bar Graph',font=('Arvo', 20),foreground='Green', command = bg_Living_Expenses).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Pie Chart',font=('Arvo', 20),foreground='Green', command = pg_Living_Expenses).pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()

def Plot_Health_Care():
    tkwindow = tk.Tk()
    tkwindow.geometry('500x250')
    tkwindow.title("Plots for Health Care Table")
    k = tk.Label(tkwindow, text ='Data Analysis', font = ('Arvo', 40, 'bold'))
    k.pack()
    pane = tk.Frame(tkwindow)
    pane.pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Bar Graph',font=('Arvo', 20),foreground='Green', command = bg_Health_Care).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Pie Chart',font=('Arvo', 20),foreground='Green', command = pg_Health_Care).pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()

def Plot_Child_Care():
    tkwindow = tk.Tk()
    tkwindow.geometry('500x250')
    tkwindow.title("Plots for Child Care Table")
    k = tk.Label(tkwindow, text ='Data Analysis', font = ('Arvo', 40, 'bold'))
    k.pack()
    pane = tk.Frame(tkwindow)
    pane.pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Bar Graph',font=('Arvo', 20),foreground='Green', command = bg_Child_Care).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Pie Chart',font=('Arvo', 20),foreground='Green', command = pg_Child_Care).pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()
   
def Plot_Miscellaneous():
    tkwindow = tk.Tk()
    tkwindow.geometry('500x250') 
    tkwindow.title("Plots for Miscellaneous Table")
    k = tk.Label(tkwindow, text ='Data Analysis', font = ('Arvo', 40, 'bold'))
    k.pack()
    pane = tk.Frame(tkwindow)
    pane.pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Bar Graph',font=('Arvo', 20),foreground='Green', command = bg_Miscellaneous).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Pie Chart',font=('Arvo', 20),foreground='Green', command = pg_Miscellaneous).pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()

def bg_Housing():
    Category = Expenditure = []
    mycursor.execute("select * from housing where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, ifh_plot, efh_plot, house_maintainance_plot, house_insurance_plot, other_spending_on_house_plot) = i
        Category = ["Income", "Rent Paid", "Maintainance", "Insurance", "Other Spending"]  
        Expenditure = [ifh_plot, efh_plot, house_maintainance_plot, house_insurance_plot, other_spending_on_house_plot]
        plt.style.use("ggplot")
        plt.bar(Category, Expenditure, color = ['r','b','g','black','yellow'], width = [0.5, 0.5, 0.5, 0.5, 0.5])
        plt.xlabel("Category")
        plt.ylabel("Expenditure")
        plt.title("Housing")
        plt.show()

def pg_Housing():
    mycursor.execute("select * from housing where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, ifh_plot, efh_plot, house_maintainance_plot, house_insurance_plot, other_spending_on_house_plot) = i
        slices = [ifh_plot, efh_plot, house_maintainance_plot, house_insurance_plot, other_spending_on_house_plot]
        labels = ["Income", "Rent Paid", "Maintainance", "Insurance", "Other Spending"]
        plt.style.use("ggplot")
        plt.pie(slices, labels=labels, shadow=True,  startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
        plt.title("Housing")
        plt.tight_layout()
        plt.show()
       
def bg_Transportation():
    Category = Expenditure = []
    mycursor.execute("select * from transportation where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, vehicle_loan_plot, vehicle_insurance_plot, vehicle_maintainance_plot, fuel_expenses_plot, other_te_plot) = i
        Category = ["Loan", "Insurance", "Maintainance", "Fuel", "Other"]
        Expenditure = [vehicle_loan_plot, vehicle_insurance_plot, vehicle_maintainance_plot, fuel_expenses_plot, other_te_plot]
        plt.style.use("ggplot")
        plt.bar(Category, Expenditure, color = ['r','b','g','black','yellow'], width = [0.5, 0.5, 0.5, 0.5, 0.5])
        plt.xlabel("Category")
        plt.ylabel("Expenditure")
        plt.title("Transportation")
        plt.show()

def pg_Transportation():
    mycursor.execute("select * from transportation where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, vehicle_loan_plot, vehicle_insurance_plot, vehicle_maintainance_plot, fuel_expenses_plot, other_te_plot) = i
        slices = [vehicle_loan_plot, vehicle_insurance_plot, vehicle_maintainance_plot, fuel_expenses_plot, other_te_plot]
        labels = ["Loan", "Insurance", "Maintainance", "Fuel", "Other"]
        plt.style.use("ggplot")
        plt.pie(slices, labels=labels, shadow=True,  startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
        plt.title("Transportation")
        plt.tight_layout()
        plt.show()

def bg_Living_Expenses():
    Category = Expenditure = []
    mycursor.execute("select * from living_expenses where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, groceries_plot, clothing_plot, entertainment_plot, other_le_plot) = i
        Category = ["Groceries", "Clothing", "Entertainment", "Other"]
        Expenditure = [groceries_plot, clothing_plot, entertainment_plot, other_le_plot]
        plt.style.use("ggplot")
        plt.bar(Category, Expenditure, color = ['r','b','g','black'], width = [0.5, 0.5, 0.5, 0.5])
        plt.xlabel("Category")
        plt.ylabel("Expenditure")
        plt.title("Living Expenses")
        plt.show()

def pg_Living_Expenses():
    mycursor.execute("select * from living_expenses where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, groceries_plot, clothing_plot, entertainment_plot, other_plot) = i
        slices = [groceries_plot, clothing_plot, entertainment_plot, other_plot]
        labels = ["Groceries", "Clothing", "Entertainment", "Other"]
        plt.style.use("ggplot")
        plt.pie(slices, labels=labels, shadow=True,  startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
        plt.title("Living Expenses")
        plt.tight_layout()
        plt.show()

def bg_Health_Care():
    Category = Expenditure = []
    mycursor.execute("select * from health_care where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, medical_insurance_plot, medical_expenses_plot) = i
        Category = ["Medical Insurance", "Medical Expenses"]
        Expenditure = [medical_insurance_plot, medical_expenses_plot]
        plt.style.use("ggplot")
        plt.bar(Category, Expenditure, color = ['r','b'], width = [0.5, 0.5])
        plt.xlabel("Category")
        plt.ylabel("Expenditure")
        plt.title("Health Care")
        plt.show()

def pg_Health_Care():
    mycursor.execute("select * from health_care where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, medical_insurance_plot, medical_expenses_plot) = i
        slices = [medical_insurance_plot, medical_expenses_plot]
        labels = ["Medical Insurance", "Medical Expenses"]
        plt.style.use("ggplot")
        plt.pie(slices, labels=labels, shadow=True,  startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
        plt.title("Health Care")
        plt.tight_layout()
        plt.show()
       
def bg_Child_Care():
    Category = Expenditure = []
    mycursor.execute("select * from child_care where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, tuition_plot, other_child_expense_plot) = i
        Category = ["Tuition", "Other"]
        Expenditure = [tuition_plot, other_child_expense_plot]
        plt.style.use("ggplot")
        plt.bar(Category, Expenditure, color = ['r','b'], width = [0.5, 0.5])
        plt.xlabel("Category")
        plt.ylabel("Expenditure")
        plt.title("Child Care")
        plt.show()

def pg_Child_Care():
    mycursor.execute("select * from child_care where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, tuition_plot, other_child_expense_plot) = i
        slices = [tuition_plot, other_child_expense_plot]
        labels = ["Tuition", "Other"]
        plt.style.use("ggplot")
        plt.pie(slices, labels=labels, shadow=True,  startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
        plt.title("Child Care")
        plt.tight_layout()
        plt.show()
       
def bg_Miscellaneous():
    Category = Expenditure = []
    mycursor.execute("select * from miscellaneous where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, pet_care_plot, hobbies_and_sports_plot, gifts_and_donations_plot, vacation_plot, other_miscellaneous_plot) = i
        Category = ["Pet Care", "Hobbies", "Gifts/Donations", "Vacation", "Other"]
        Expenditure = [pet_care_plot, hobbies_and_sports_plot, gifts_and_donations_plot, vacation_plot, other_miscellaneous_plot]
        plt.style.use("ggplot")
        plt.bar(Category, Expenditure, color = ['r','b','g','black','yellow'], width = [0.5, 0.5, 0.5, 0.5,0.5])
        plt.xlabel("Category")
        plt.ylabel("Expenditure")
        plt.title("Miscellaneous")
        plt.show()

def pg_Miscellaneous():
    mycursor.execute("select * from miscellaneous where Month = '{}'".format(plot_month))
    for i in mycursor.fetchall():
        (extra_month, pet_care_plot, hobbies_and_sports_plot, gifts_and_donations_plot, vacation_plot, other_miscellaneous_plot) = i
        slices = [pet_care_plot, hobbies_and_sports_plot, gifts_and_donations_plot, vacation_plot, other_miscellaneous_plot]
        labels = ["Pet Care", "Hobbies", "Gifts and Donations", "Vacation", "Other"]
        plt.style.use("ggplot")
        plt.pie(slices, labels=labels, shadow=True,  startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
        plt.title("Miscellaneous")
        plt.tight_layout()
        plt.show()
   
def MAI():
    root = tk.Tk()
    root.title("Monthly After-Tax Salary")
    fields = ('Enter the monthly after-tax salary',)
    ents = makeform(root, fields)
    root.bind(lambda event, e=ents: MAI_values(e))    
    tk.Button(root, text='Submit', command=(lambda e=ents: MAI_values(e))).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(root, text = "Proceed", command = Budget_Menu).pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
   
def MAI_values(entries):
    global necessities_ab, wants_ab, savings_ab, track_cnd, monthly_aftertax_income
    value_list = []
    for entry in entries:
        value = entry[1].get()
        value_list.append(value)
    for i in value_list:
        monthly_aftertax_income = float(i)
    necessities_ab = 0.5 * monthly_aftertax_income
    wants_ab = 0.3 * monthly_aftertax_income
    savings_ab = 0.2 * monthly_aftertax_income
    print("Monthly After Tax Income :",monthly_aftertax_income)
    track_cnd = "Auto Budget"
   
def Budget_Menu():
    tkwindow = tk.Tk()
    tkwindow.geometry('1000x500')
    tkwindow.title("Budget Menu")
    tk.Label(tkwindow, text ='Budget Menu', font = ('Arvo', 30, 'bold')).pack()
    pane = tk.Frame(tkwindow)
    pane.pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Automatic Budget', font=('Arvo', 20),foreground='Green', command = budget_desc).pack(fill = tk.BOTH, expand = True)
    tk.Button(pane,text='Manual Budget', font=('Arvo', 20),foreground='Green', command = Manual_Budget).pack(fill = tk.BOTH, expand = True)
    tkwindow.mainloop()
   
def budget_desc():
    tkwindow = tk.Tk()
    tkwindow.geometry('1000x400')
    tkwindow.title("Auto Budget Description")
    T = tk.Text(tkwindow, height =10, width = 200)
    l = tk.Label(tkwindow, text = "Attention")
    l.config(font =("Calibri", 20))
    Fact = """This is the most popular way of budgeting, in this rule of budgeting, you spend roughly 50% of your after-tax money on necessities, no more than 30% on wants, and at least 20% on savings. We like the simplicity of this plan. Over the long term, someone who follows these guidelines will have manageable debt, room to indulge occasionally, and savings to pay irregular or unexpected expenses and retire comfortably."""
    b1 = tk.Button(tkwindow, text = "Next", command = Auto_Budget_Desc)
    l.pack()
    T.pack()
    b1.pack()
    T.insert(tk.END, Fact)
    tkwindow.mainloop()

def Auto_Budget_Desc():
    global cnd_for_budget_creation
    print()
    print("According to the autobudget : ")
    print("Amount of money you should be spending on necessities - ₹",necessities_ab)
    print("Amount of money you should be spending on wants - ₹",wants_ab)
    print("Amount of money you should be saving - ₹",savings_ab)
    print()
    cnd_for_budget_creation = "Budget Created"
       
def Manual_Budget():
    root = tk.Tk()
    root.title("Manual Budget")
    fields = 'Necessities', 'Wants', 'Savings'
    ents = makeform(root, fields)
    root.bind(lambda event, e=ents: Manual_Budget_Values(e))    
    tk.Button(root, text='Submit', command=(lambda e=ents: Manual_Budget_Values(e))).pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
   
def Manual_Budget_Values(entries):
    global manual_necessities, manual_wants, manual_savings, track_cnd, cnd_for_budget_creation
    value_list = []
    for entry in entries:
        value = entry[1].get()
        value_list.append(value)
    manual_necessities = float(value_list[0])
    manual_wants = float(value_list[1])
    manual_savings = float(value_list[2])        
    total_sum = manual_necessities + manual_wants + manual_savings
    track_cnd = "Manual Budget"
    if total_sum != monthly_aftertax_income :
        messagebox.showinfo("Invalid input", "The total amount assigned doesn't add up to the monthly after-tax income.")
        print()
    else:
        print("According to the manual budget : ")
        print("Amount of money you should be spending on necessities - ₹",manual_necessities)
        print("Amount of money you should be spending on wants - ₹",manual_wants)
        print("Amount of money you should be saving - ₹",manual_savings)
        print("You're all done, we will help you keep track of this budget and let you know as you progress.")
        print()     
        cnd_for_budget_creation = "Budget Created"
        
def Necessities(tm):
    mycursor.execute("select tuition from child_care where month = '{}'".format(tm))
    rn1 = mycursor.fetchall()
    mycursor.execute("select medical_insurance from health_care where month = '{}'".format(tm))
    rn2 = mycursor.fetchall()
    mycursor.execute("select income_from_houses, rent_paid, house_insurance from housing where month = '{}'".format(tm))
    rn3 = mycursor.fetchall()
    mycursor.execute("select groceries from living_expenses where month = '{}'".format(tm))
    rn4 = mycursor.fetchall()
    mycursor.execute("select vehicle_insurance, vehicle_loan from transportation where month = '{}'".format(tm))
    rn5 = mycursor.fetchall()
    rn =  rn1[0][0] + rn2[0][0] - rn3[0][0] + rn3[0][1] + rn3[0][2] + rn4[0][0] + rn5[0][0] + rn5[0][1]  
    return rn

def Wants(tm):
    mycursor.execute("select * from miscellaneous where month = '{}'".format(tm))
    rw1 = mycursor.fetchall()
    mycursor.execute("select vehicle_maintainance, fuel_expenses, other_transportation_expenses from transportation where month = '{}'".format(tm))
    rw2 = mycursor.fetchall()
    mycursor.execute("select clothing, entertainment, other_living_expenses from living_expenses where month = '{}'".format(tm))
    rw3 = mycursor.fetchall()
    mycursor.execute("select house_maintainance, other_spending_on_houses from housing where month = '{}'".format(tm))
    rw4 = mycursor.fetchall()
    mycursor.execute("select medical_expenses from health_care where month = '{}'".format(tm))
    rw5 = mycursor.fetchall()
    mycursor.execute("select other_expenses_for_child from child_care where month = '{}'".format(tm))
    rw6 = mycursor.fetchall()
    rw = rw1[0][1] + rw1[0][2] + rw1[0][3] + rw1[0][4] + rw1[0][5] + rw2[0][0] + rw2[0][1] + rw2[0][2] + rw3[0][0] + rw3[0][1] + rw3[0][2] + rw4[0][0] + rw4[0][1] + rw5[0][0] + rw6[0][0]   
    return rw
   
def Savings(tm):
    rn_total = Necessities(tm)
    rw_total = Wants(tm)
    rs = monthly_aftertax_income - rn_total - rw_total
    return rs

def Which_Month_Track_Budget():
    
    if cnd_for_budget_creation == "Budget Created" :
        
        tkwindow = tk.Tk()
        tkwindow.title('Combobox')
        tkwindow.title('Choosing Month for Tracking Budget')
        tkwindow.geometry('500x250')
    
        tk.Label(tkwindow, text = "Monthly Analysis", background = 'green', foreground ="white", font = ("Times New Roman", 15)).grid(row = 0, column = 1)
        tk.Label(tkwindow, text = "Select the Month :", font = ("Times New Roman", 10)).grid(column = 0, row = 5, padx = 10, pady = 25)
        monthchoosen = ttk.Combobox(tkwindow, width = 27, values=('January','February','March','April','May','June','July','August','September','October','November', 'December' ))
        monthchoosen.grid(column = 1, row = 5)

        def selectmonth_action():        
            global track_month    
            track_month = monthchoosen.get()
            if track_month == "":
                messagebox.showinfo("NO INPUT", "Kindly choose something")
            elif track_month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
                messagebox.showinfo("WRONG INPUT", "Kindly use the dropdown")
            else:
                print(track_month,"is chosen for Tracking Budget")
                print()
        ttk.Button(tkwindow, text="Get Value", command = selectmonth_action).grid(column = 3, row = 5)
        ttk.Button(tkwindow, text="Submit", command = Track_Budget).grid(column = 3, row = 6)
        tkwindow.mainloop()
    
    else :
        
        messagebox.showinfo("ERROR", "Please Create Budget in order to Track Budget")
        
def Track_Budget():
    
    global track_cnd
      
    if track_cnd == "Auto Budget" :
        Track_Auto_Budget()
        
    if track_cnd == "Manual Budget" : 
        Track_Manual_Budget()
            
def Track_Auto_Budget():
               
    real_necessities = real_wants = real_savings = 0.0
    real_necessities = Necessities(track_month)
    real_wants = Wants(track_month)
    real_savings = Savings(track_month)
    track_necessities, track_wants, track_savings = necessities_ab, wants_ab, savings_ab   
    if real_necessities > track_necessities:
        print("You have exceeded the limit on the amount to be spent on necessities")
        print("Amount exceeded :",real_necessities - track_necessities)
        print()
    else:
        print("You have remained under the budget on necessities")
        print()
      
    if real_wants > track_wants:
        print("You have exceeded the limit on the amount to be spent on wants")
        print("Amount exceeded :",real_wants - track_wants)
        print()
    else:
        print("You have remained under the budget on wants")
        print()
      
    if real_savings > track_savings:
        print("You have exceeded the limit on the amount to be saved")
        print("Amount exceeded :",real_savings - track_savings)
        print()
    else:
        print("You have remained under the budget on for amount saved")
        print()   
                
def Track_Manual_Budget():
            
    real_necessities = real_wants = real_savings = 0.0
    real_necessities = Necessities(track_month)
    real_wants = Wants(track_month)
    real_savings = Savings(track_month)
    track_necessities, track_wants, track_savings = manual_necessities, manual_wants, manual_savings   
    if real_necessities > track_necessities:
        print("You have exceeded the limit on the amount to be spent on necessities")
        print("Amount exceeded :",real_necessities - track_necessities)
        print()
    else:
        print("You have remained under the budget on necessities")
        print()
      
    if real_wants > track_wants:
        print("You have exceeded the limit on the amount to be spent on wants")
        print("Amount exceeded :",real_wants - track_wants)
        print()
    else:
        print("You have remained under the budget on wants")
        print()
      
    if real_savings > track_savings:
        print("You have exceeded the limit on the amount to be saved")
        print("Amount exceeded :",real_savings - track_savings)
        print()
    else:
        print("You have remained under the budget on for amount saved")
        print()
                
Login()
