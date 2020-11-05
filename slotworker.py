from tkinter import *
from tkinter import StringVar
import tkinter.messagebox
import mysql.connector
from mysql.connector import connect
from addnewworker import showaddWorkers

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
        db.close
        tab = "Worker_ID, Worker_Name, Hours Worked, Dept_ID"
        workerlist.insert(END, tab)
        for row in rows:
            workerlist.insert(END, row, str(" "))
    
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

showslotworker()