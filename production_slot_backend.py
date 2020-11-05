import mysql.connector
from mysql.connector import connect
from tkinter import *

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