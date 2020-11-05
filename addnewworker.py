from tkinter import *
from tkinter import StringVar
import tkinter.messagebox
import mysql.connector
from mysql.connector import connect

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

showaddWorkers()