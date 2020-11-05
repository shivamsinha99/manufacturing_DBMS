import mysql.connector
from mysql.connector import connect
from tkinter import *
import tkinter.messagebox

# root = Tk()
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