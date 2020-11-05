from tkinter import *
from tkinter import StringVar
import tkinter.messagebox
from slotworker import showslotworker
import mysql.connector
from mysql.connector import connect

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


show_productionslot()