import mysql.connector
from mysql.connector import connect
from tkinter import *
import tkinter.messagebox
# from manageProducts import showmanageProducts
from production_slot import show_productionslot
# from addnewworker import showaddWorkers
import manageProducts_backend
from addnewworker import showaddWorkers



def mainpage():
    root = Tk()
    root.title("Manufacturing Industry Database Management")
    root.config(bg="cadet blue")

    manufac_heading = Label(root, text = "Manufacturing Industry Database Management System")
    manufac_heading.grid(row = 0, column = 1, pady = 10, columnspan = 3)
    manufac_heading.config(width = 50)
    manufac_heading.config(font = ("Segoe UI", 24, 'bold'))

    windowHeading = Label(root, text = "MAIN PAGE")
    windowHeading.grid(row = 1, column = 1, pady = 10, columnspan = 3)
    windowHeading.config(font = ("Segoe UI", 20, 'bold'))

    man_products = Button(root, text = "Manage Products", command = showmanageProducts)
    man_products.grid(row = 5, column = 1, pady = 10, columnspan = 3)
    man_products.config(font = ("Segoe UI", 18, 'bold'))

    # registerButton = Button(root, text = "Register", command = displayRegistration)
    # registerButton.grid(row = 5, column = 2, pady = 10, columnspan = 3)
    # registerButton.config(font = ("Segoe UI", 18))

    addslot = Button(root, text = "Add Production Slot", command = show_productionslot)
    addslot.grid(row = 6, column = 1, pady = 10, columnspan = 3)
    addslot.config(font = ("Segoe UI", 18, 'bold'))

    showstock = Button(root, text = "Add New Workers", command = showaddWorkers)
    showstock.grid(row = 7, column = 1, pady = 10, columnspan = 3)
    showstock.config(font = ("Segoe UI", 18, 'bold'))

    showstock = Button(root, text = "Show Product Stocks", command = showmanageProducts)
    showstock.grid(row = 8, column = 1, pady = 10, columnspan = 3)
    showstock.config(font = ("Segoe UI", 18, 'bold'))

    quitButton = Button(root, text = "Quit!", command = root.destroy)
    quitButton.grid(row = 9, column = 1, pady = 20, columnspan = 3)
    quitButton.config(font = ("Segoe UI", 18, 'bold'))

    root.mainloop()

def showaddWorkers():
    root = Tk()
    root.title("Manufacturing Industry Database Management")
    root.geometry("1138x545+0+0")
    root.config(bg="cadet blue")

    worker_ID = StringVar()
    worker_name = StringVar()
    hours_worked = StringVar()
    dept_ID = StringVar()

    def Exit():
        bExit = tkinter.messagebox.askyesno("Manufacuring Database Management", "Confirm If you want to Exit")
        if bExit > 0:
            root.destroy()
            return

    def displayData():
        workerlist.delete(0, END)
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Worker;")
        rows = cursor.fetchall()
        db.close
        tab = "Worker_ID, Worker_Name, Hours Worked, Dept_ID"
        workerlist.insert(END, tab)
        for row in rows:
            workerlist.insert(END, row, str(" "))
    
    def addWorker():
        if ((len(worker_ID.get())!=0)):
            db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
            cursor = db.cursor()
            inquiry = "INSERT INTO worker VALUES (%s, %s, %s, %s);"
            data = (worker_ID.get(), worker_name.get(), hours_worked.get(), dept_ID.get())
            cursor.execute(inquiry, data)
            # cursor.execute("INSERT INTO Product VALUES (?, ?, ?, ?, ?)", (Product_ID, Product_Name, int(Cost_Price), int(MRP), descrip))
            db.commit()
            db.close
        displayData()
    
    def WorkerRec(event):
        global pd
        searchPrd = workerlist.curselection()
        pd = workerlist.get(searchPrd)

        workerIDText.delete(0, END)
        workerIDText.insert(END, pd[0])


    MainFrame = Frame(root, bg="cadet blue")
    MainFrame.pack()

    TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="cadet blue", relief=RIDGE)
    TitleFrame.pack()

    TitleLabel = Label(TitleFrame, font=('Segoe UI', 16, 'bold'), text="Add New Workers", bg = "cadet blue")
    TitleLabel.pack(pady=5, padx= 10) 

    ButtonFrame = Frame(MainFrame, bd=2, width=683, height=35, padx=9, pady=5, bg="Ghost white", relief=RIDGE)
    ButtonFrame.pack(side=BOTTOM)

    DataFrame = Frame(MainFrame, bd=1, width=683, height=200, padx=10, pady=10, bg="cadet blue", relief=RIDGE)
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=683, height=200, padx=10, pady=10, bg="Ghost White", 
    font=('Segoe UI', 18, 'bold'), relief=RIDGE, text="Add Worker\n")
    DataFrameLEFT.pack(side=LEFT)

    DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=225, height=100, padx=10, pady=10, bg="Ghost White", 
    font=('Segoe UI', 18, 'bold'), relief=RIDGE, text="Workers List\n")
    DataFrameRIGHT.pack(side=RIGHT)

    workerIDLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="WorkerID: ", bg = "Ghost White")
    workerIDLabel.grid(row=1, column=0, sticky=W) 
    workerIDText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=worker_ID, width =39)
    workerIDText.grid(row=1, column=1)

    slotnoLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Worker Name: ", bg = "Ghost White")
    slotnoLabel.grid(row=0, column=0, sticky=W) 
    slotnoText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=worker_name, width =39)
    slotnoText.grid(row=0, column=1)

    hoursworkedLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Hours Worked: ", bg = "Ghost White")
    hoursworkedLabel.grid(row=2, column=0, sticky=W) 
    hoursworkedText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=hours_worked, width =39)
    hoursworkedText.grid(row=2, column=1)
    
    deptIDLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Dept ID: ", bg = "Ghost White")
    deptIDLabel.grid(row=3, column=0, sticky=W) 
    deptIDText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=dept_ID, width =39)
    deptIDText.grid(row=3, column=1)

    scrollbar = Scrollbar(DataFrameRIGHT)
    scrollbar.grid(row=0, column=1, sticky='ns')

    workerlist = Listbox(DataFrameRIGHT, width=41, height=10, font=('Segoe UI', 12, 'bold'), yscrollcommand=scrollbar.set)
    workerlist.bind('<<ListboxSelect>>', WorkerRec)
    workerlist.grid(row=0, column=0, padx=8)
    scrollbar.config(command=workerlist.yview)

    displayData()

    btnAddWorker = Button(ButtonFrame, text="Add Worker", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=addWorker)
    btnAddWorker.grid(row=0, column=0)
    btnExit = Button(ButtonFrame, text="Exit", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=Exit)
    btnExit.grid(row=0, column=1)


    root.mainloop()

def showmanageProducts():
    root = Tk()
    root.title("Manufacturing Industry Database Management")
    root.geometry("1138x545+0+0")
    root.config(bg="cadet blue")

    
    Product_ID = StringVar()
    Product_Name = StringVar()
    CP = StringVar()
    MRP = StringVar()
    Desc = StringVar()

    #####FUNCTIONS#####

    def Exit():
        bExit = tkinter.messagebox.askyesno("Manufacuring Database Management", "Confirm If you want to Exit")
        if bExit > 0:
            root.destroy()
            return
    
    def ProductData():
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS create table if not exists Product(Product_ID varchar(5) not null,
        Product_Name varchar(20), 
        Cost_Price INT,
        MRP INT,
        descrip varchar(50),
        constraint pid primary key(Product_ID));""")
        db.commit()
        db.close()

    def addProduct(Product_ID, Product_Name, Cost_Price, MRP, descrip):
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        inquiry = "INSERT INTO Product VALUES (%s, %s, %s, %s, %s);"
        data = (Product_ID, Product_Name, int(Cost_Price), int(MRP), descrip)
        cursor.execute(inquiry, data)
        # cursor.execute("INSERT INTO Product VALUES (?, ?, ?, ?, ?)", (Product_ID, Product_Name, int(Cost_Price), int(MRP), descrip))
        db.commit()
        db.close

    def viewProducts():
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM PRODUCT;")
        rows = cursor.fetchall()
        db.close
        return rows

    def deleteProduct(Product_ID):
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        # query = "DELETE FROM Product where Product_ID = '%s';"
        # data = (Product_ID)
        # cursor.execute(query, data)
        # print("DELETE FROM Product where Product_ID = %s;", (Product_ID))
        cursor.execute("DELETE FROM Product where Product_ID = '" + Product_ID + "';")
        
        db.commit()
        db.close

    def searchProduct(Product_ID=" ", Product_Name=" ", Cost_Price=" ", MRP=" ", descrip=" "):
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        # query = "SELECT * FROM PRODUCT WHERE Product_ID = %s OR  Product_Name = %s OR Cost_Price = %s OR MRP = %s OR descrip = %s"
        # data = (Product_ID, Product_Name, Cost_Price, MRP, descrip)
        # cursor.execute(query, data)
        cursor.execute("SELECT * FROM PRODUCT WHERE Product_ID = %s OR  Product_Name = %s OR Cost_Price = %s OR MRP = %s OR \
        descrip = %s;", (Product_ID, Product_Name, Cost_Price, MRP, descrip))
        rows = cursor.fetchall()
        db.close
        return rows

    def updateProduct(Product_ID=" ", Product_Name=" ", Cost_Price=" ", MRP=" ", descrip=" "):
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        cursor.execute("UPDATE Product SET Product_Name = %s, Cost_Price = %s ,\
        descrip = %s WHERE Product_ID = %s;", (Product_Name, Cost_Price, MRP, descrip, Product_ID))
        db.commit()
        db.close

    def clearData():
        PrIDText.delete(0, END)
        PrNameText.delete(0, END)
        CPText.delete(0, END)
        MRPText.delete(0, END)
        descText.delete(0, END)

    def addData():
        if (len(Product_ID.get())!=0):
            addProduct(Product_ID.get(), Product_Name.get(), CP.get(), MRP.get(), Desc.get())
            productlist.delete(0, END)
            productlist.insert(END, (Product_ID.get(), Product_Name.get(), CP.get(), MRP.get(), Desc.get()))

    def displayData():
        productlist.delete(0, END)
        for row in viewProducts():
            productlist.insert(END, row, str(" "))

    def ProductRec(event):
        global pd
        searchPrd = productlist.curselection()
        pd = productlist.get(searchPrd)

        PrIDText.delete(0, END)
        PrIDText.insert(END, pd[0])
        PrNameText.delete(0, END)
        PrNameText.insert(END, pd[1])
        CPText.delete(0, END)
        CPText.insert(END, pd[2])
        MRPText.delete(0, END)
        MRPText.insert(END, pd[3])
        descText.delete(0, END)
        descText.insert(END, pd[4])

    def deleteData():
        if (len(Product_ID.get())!=0):
            deleteProduct(Product_ID.get())
            # print(pd[0])
            # print(Product_ID.get())
            clearData()
            displayData()

    def searchDatabase():
        productlist.delete(0, END)
        for row in searchProduct(Product_ID.get(), Product_Name.get(), CP.get(), MRP.get(), Desc.get()):
            productlist.insert(END, row, str(" "))

    def update():
        if (len(Product_ID.get())!=0):
            deleteProduct(pd[0])
        if (len(Product_ID.get())!=0):
            addProduct(Product_ID.get(), Product_Name.get(), CP.get(), MRP.get(), Desc.get())
            productlist.delete(0, END)
            productlist.insert(END, (Product_ID.get(), Product_Name.get(), CP.get(), MRP.get(), Desc.get()))

    #####FRAMES#####
    MainFrame = Frame(root, bg="cadet blue")
    MainFrame.pack()

    TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="cadet blue", relief=RIDGE)
    TitleFrame.pack()

    TitleLabel = Label(TitleFrame, font=('Segoe UI', 22, 'bold'), text="Products", bg = "cadet blue")
    TitleLabel.pack(pady=5, padx= 10) 

    ButtonFrame = Frame(MainFrame, bd=2, width=683, height=35, padx=9, pady=5, bg="Ghost white", relief=RIDGE)
    ButtonFrame.pack(side=BOTTOM)

    DataFrame = Frame(MainFrame, bd=1, width=683, height=200, padx=10, pady=10, bg="cadet blue", relief=RIDGE)
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=683, height=200, padx=10, pady=10, bg="Ghost White", 
    font=('Segoe UI', 18, 'bold'), relief=RIDGE, text="Product Info\n")
    DataFrameLEFT.pack(side=LEFT)

    DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=225, height=100, padx=10, pady=10, bg="Ghost White", 
    font=('Segoe UI', 18, 'bold'), relief=RIDGE, text="Products\n")
    DataFrameRIGHT.pack(side=RIGHT)

    #####LABELS AND ENTRY WIDGETS#####
    PrIDLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Product ID: ", bg = "Ghost White")
    PrIDLabel.grid(row=0, column=0, sticky=W) 
    PrIDText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=Product_ID, width =39)
    PrIDText.grid(row=0, column=1)

    PrNameLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Product Name: ", bg = "Ghost White")
    PrNameLabel.grid(row=1, column=0, sticky=W) 
    PrNameText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=Product_Name, width =39)
    PrNameText.grid(row=1, column=1)

    CPLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Cost Price: ", bg = "Ghost White")
    CPLabel.grid(row=2, column=0, sticky=W) 
    CPText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=CP, width =39)
    CPText.grid(row=2, column=1)

    MRPLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="MRP: ", bg = "Ghost White")
    MRPLabel.grid(row=3, column=0, sticky=W) 
    MRPText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=MRP, width =39)
    MRPText.grid(row=3, column=1)

    descLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Description: ", bg = "Ghost White")
    descLabel.grid(row=4, column=0, sticky=W) 
    descText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=Desc, width =39)
    descText.grid(row=4, column=1)

    #####ListBox & ScrollB widget#####

    scrollbar = Scrollbar(DataFrameRIGHT)
    scrollbar.grid(row=0, column=1, sticky='ns')

    productlist = Listbox(DataFrameRIGHT, width=41, height=10, font=('Segoe UI', 12, 'bold'), yscrollcommand=scrollbar.set)
    productlist.bind('<<ListboxSelect>>', ProductRec)
    productlist.grid(row=0, column=0, padx=8)
    scrollbar.config(command=productlist.yview)

    #####Button Widget#####

    btnAddData = Button(ButtonFrame, text="Add New", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=addData)
    btnAddData.grid(row=0, column=0)
    btndisplayData = Button(ButtonFrame, text="Display", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=displayData)
    btndisplayData.grid(row=0, column=1)
    btnclearData = Button(ButtonFrame, text="CLEAR", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=clearData)
    btnclearData.grid(row=0, column=2)
    btndeleteData = Button(ButtonFrame, text="Delete", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=deleteData)
    btndeleteData.grid(row=0, column=3)
    btnsearchData = Button(ButtonFrame, text="Search", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=searchDatabase)
    btnsearchData.grid(row=0, column=4)
    btnupdateData = Button(ButtonFrame, text="Update", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=update)
    btnupdateData.grid(row=0, column=5)
    btnExit = Button(ButtonFrame, text="Exit", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=Exit)
    btnExit.grid(row=0, column=6)

    root.mainloop()

def show_productionslot():
    root = Tk()
    root.title("Manufacturing Industry Database Management")
    root.geometry("1138x545+0+0")
    root.config(bg="cadet blue")

    slot_no = StringVar()
    hours_run = StringVar()
    product_ID = StringVar()

    #####FUNCTIONS#####

    def Exit():
        bExit = tkinter.messagebox.askyesno("Manufacuring Database Management", "Confirm If you want to Exit")
        if bExit > 0:
            root.destroy()
            return
    def addSlot(Slot_no, hours_run,  Product_ID):
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        inquiry = "INSERT INTO Production_Slot VALUES (%s, %s, %s);"
        data = (Slot_no, hours_run, Product_ID)
        cursor.execute(inquiry, data)
        # cursor.execute("INSERT INTO Product VALUES (?, ?, ?, ?, ?)", (Product_ID, Product_Name, int(Cost_Price), int(MRP), descrip))
        db.commit()
        db.close

    def viewSlots():
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Production_Slot;")
        rows = cursor.fetchall()
        db.close
        return rows

    def displayData():
        slotlist.delete(0, END)
        for row in viewSlots():
            slotlist.insert(END, row, str(" "))
    
    def addData():
        if (len(slot_no.get())!=0):
            addSlot(slot_no.get(), hours_run.get(), product_ID.get())
            slotlist.delete(0, END)
            slotlist.insert(END, (slot_no.get(), hours_run.get(), product_ID.get()))
        displayData()

    MainFrame = Frame(root, bg="cadet blue")
    MainFrame.pack()

    TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="cadet blue", relief=RIDGE)
    TitleFrame.pack()

    TitleLabel = Label(TitleFrame, font=('Segoe UI', 22, 'bold'), text="Add Production Slot", bg = "cadet blue")
    TitleLabel.pack(pady=5, padx= 10) 

    ButtonFrame = Frame(MainFrame, bd=2, width=683, height=35, padx=9, pady=5, bg="Ghost white", relief=RIDGE)
    ButtonFrame.pack(side=BOTTOM)

    DataFrame = Frame(MainFrame, bd=1, width=683, height=200, padx=10, pady=10, bg="cadet blue", relief=RIDGE)
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=683, height=200, padx=10, pady=10, bg="Ghost White", 
    font=('Segoe UI', 18, 'bold'), relief=RIDGE, text="Add Slot Info\n")
    DataFrameLEFT.pack(side=LEFT)

    DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=225, height=100, padx=10, pady=10, bg="Ghost White", 
    font=('Segoe UI', 18, 'bold'), relief=RIDGE, text="Previous Slots\n")
    DataFrameRIGHT.pack(side=RIGHT)

    #####LABELS AND ENTRY WIDGETS#####
    slotnoLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Slot NO.: ", bg = "Ghost White")
    slotnoLabel.grid(row=0, column=0, sticky=W) 
    slotnoText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=slot_no, width =39)
    slotnoText.grid(row=0, column=1)

    hoursrunLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Hours Run: ", bg = "Ghost White")
    hoursrunLabel.grid(row=1, column=0, sticky=W) 
    hoursrunText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=hours_run, width =39)
    hoursrunText.grid(row=1, column=1)

    PrIDLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Product ID: ", bg = "Ghost White")
    PrIDLabel.grid(row=2, column=0, sticky=W) 
    PrIDText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=product_ID, width =39)
    PrIDText.grid(row=2, column=1)

    #####ListBox & ScrollB widget#####

    scrollbar = Scrollbar(DataFrameRIGHT)
    scrollbar.grid(row=0, column=1, sticky='ns')

    slotlist = Listbox(DataFrameRIGHT, width=41, height=10, font=('Segoe UI', 12, 'bold'), yscrollcommand=scrollbar.set)
    #slotlist.bind('<<ListboxSelect>>', ProductRec)
    slotlist.grid(row=0, column=0, padx=8)
    scrollbar.config(command=slotlist.yview)

    displayData()

    #####Button Widget#####

    btnAddData = Button(ButtonFrame, text="Add Slot", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=addData)
    btnAddData.grid(row=0, column=0)
    btnWorker = Button(ButtonFrame, text="Add Worker to Slot", font=('Segoe UI', 16, 'bold'), height=1, width=15, bd=4, command=showslotworker)
    btnWorker.grid(row=0, column=5)
    btnExit = Button(ButtonFrame, text="Exit", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=Exit)
    btnExit.grid(row=0, column=6)
    root.mainloop()

def showslotworker():
    root = Tk()
    root.title("Manufacturing Industry Database Management")
    root.geometry("1138x545+0+0")
    root.config(bg="cadet blue")

    slot_no = StringVar()
    worker_ID = StringVar()

    def Exit():
        bExit = tkinter.messagebox.askyesno("Manufacuring Database Management", "Confirm If you want to Exit")
        if bExit > 0:
            root.destroy()
            return

    def displayData():
        workerlist.delete(0, END)
        db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Worker;")
        rows = cursor.fetchall()
        tab = "Worker_ID, Worker_Name, Hours Worked, Dept_ID"
        workerlist.insert(END, tab)
        for row in rows:
            workerlist.insert(END, row, str(" "))
        db.close
    
    def addWorker():
        if (len(slot_no.get())!=0 and len(worker_ID.get())!=0):
            db = mysql.connector.connect(host = "localhost", user = "root", passwd = "piklu1999", database = "testing")
            cursor = db.cursor()
            inquiry = "INSERT INTO worker_slot VALUES (%s, %s);"
            data = (worker_ID.get(), slot_no.get())
            cursor.execute(inquiry, data)
            inq = "UPDATE Worker SET hours_worked = hours_worked + (select hours_run from Production_Slot where Slot_no= %s) where Worker_ID=%s;"
            data = (slot_no.get(), worker_ID.get())
            cursor.execute(inq, data)
            # cursor.execute("INSERT INTO Product VALUES (?, ?, ?, ?, ?)", (Product_ID, Product_Name, int(Cost_Price), int(MRP), descrip))
            db.commit()
            db.close
        displayData()
    
    def WorkerRec(event):
        global pd
        searchPrd = workerlist.curselection()
        pd = workerlist.get(searchPrd)

        workerIDText.delete(0, END)
        workerIDText.insert(END, pd[0])


    MainFrame = Frame(root, bg="cadet blue")
    MainFrame.pack()

    TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="cadet blue", relief=RIDGE)
    TitleFrame.pack()

    TitleLabel = Label(TitleFrame, font=('Segoe UI', 16, 'bold'), text="Add Workers Who Worked in Production Slot", bg = "cadet blue")
    TitleLabel.pack(pady=5, padx= 10) 

    ButtonFrame = Frame(MainFrame, bd=2, width=683, height=35, padx=9, pady=5, bg="Ghost white", relief=RIDGE)
    ButtonFrame.pack(side=BOTTOM)

    DataFrame = Frame(MainFrame, bd=1, width=683, height=200, padx=10, pady=10, bg="cadet blue", relief=RIDGE)
    DataFrame.pack(side=BOTTOM)

    DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=683, height=200, padx=10, pady=10, bg="Ghost White", 
    font=('Segoe UI', 18, 'bold'), relief=RIDGE, text="Add Worker\n")
    DataFrameLEFT.pack(side=LEFT)

    DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=225, height=100, padx=10, pady=10, bg="Ghost White", 
    font=('Segoe UI', 18, 'bold'), relief=RIDGE, text="Workers List\n")
    DataFrameRIGHT.pack(side=RIGHT)

    slotnoLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="Slot NO.: ", bg = "Ghost White")
    slotnoLabel.grid(row=0, column=0, sticky=W) 
    slotnoText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=slot_no, width =39)
    slotnoText.grid(row=0, column=1)

    workerIDLabel = Label(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), padx=2, pady=2, text="WorkerID: ", bg = "Ghost White")
    workerIDLabel.grid(row=1, column=0, sticky=W) 
    workerIDText = Entry(DataFrameLEFT, font=('Segoe UI', 16, 'bold'), textvariable=worker_ID, width =39)
    workerIDText.grid(row=1, column=1)

    scrollbar = Scrollbar(DataFrameRIGHT)
    scrollbar.grid(row=0, column=1, sticky='ns')

    workerlist = Listbox(DataFrameRIGHT, width=41, height=10, font=('Segoe UI', 12, 'bold'), yscrollcommand=scrollbar.set)
    workerlist.bind('<<ListboxSelect>>', WorkerRec)
    workerlist.grid(row=0, column=0, padx=8)
    scrollbar.config(command=workerlist.yview)

    displayData()

    btnAddWorker = Button(ButtonFrame, text="Add Worker to Slot", font=('Segoe UI', 16, 'bold'), height=1, width=25, bd=4, command=addWorker)
    btnAddWorker.grid(row=0, column=0)
    btnExit = Button(ButtonFrame, text="Exit", font=('Segoe UI', 16, 'bold'), height=1, width=10, bd=4, command=Exit)
    btnExit.grid(row=0, column=1)
    btnAddWorkers = Button(ButtonFrame, text="Add New Workers", font=('Segoe UI', 16, 'bold'), height=1, width=25, bd=4, command=showaddWorkers)
    btnAddWorkers.grid(row=0, column=7)


    root.mainloop()

mainpage()