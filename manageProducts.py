from tkinter import *
from tkinter import StringVar
import tkinter.messagebox
import mysql.connector
from mysql.connector import connect


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

showmanageProducts()