#PYTHON MODULE: BOOK
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform


def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))


def insertData():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code : ")
        bname = input("Enter Book Name : ")
        Auth = input("Enter Book Author's Name : ")
        price = int(input("Enter Book Price : "))
        publ = input("Enter Publisher of Book : ")
        qty = int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date/Month and Year seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        Qry = ("INSERT INTO BookRecord VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data = (bno, bname, Auth, price, publ, qty, date(YY,MM,DD))
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


def deleteBook():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code of Book to be deleted from the Library : ")
        Qry = ("""DELETE FROM BookRecord WHERE BNO = %s""")
        del_rec = (bno,)
        Cursor .execute(Qry, del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


def SearchBookRec():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book No to be Searched from the Library : ")
        query = ("SELECT * FROM BookRecord WHERE BNo = %s ")
        rec_srch = (bno,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(Bno, Bname, Author, price, publ, qty, Date_of_Purchase) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("Book Code : ", Bno)
            print("Book Name : ", Bname)
            print("Author of Book : ", Author)
            print("Price of Book : ", price)
            print("Publisher : ", publ)
            print("Total Quantity in Hand : ", qty)
            print("Purchased On : ", Date_of_Purchase)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


def UpdateBook():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code of Book to be Updated from the Library : ")
        query = ("SELECT * FROM BookRecord WHERE BNo = %s ")
        rec_srch = (bno,)
        print("Enter new data")
        bname = input("Enter Book Name : ")
        Auth = input("Enter Book Author's Name : ")
        price = int(input("Enter Book Price : "))
        publ = input("Enter Publisher of Book : ")
        qty = int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date/Month and Year seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        Date_of_Purchase = date(YY,MM,DD)
        Qry = ("UPDATE BookRecord SET bname=%s, Auth=%s, price=%s, publ=%s, qty=%s, Date_of_Purchase=%s WHERE Bno=%s")
        data = (bname, Auth, price, publ, qty, Date_of_Purchase, bno)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()
