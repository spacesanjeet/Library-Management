#PYTHON MODULE: ISSUE
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os


def clrscreen():
    print('\n' * 5)


def SearchIssuedBooks():
    try:
        os.system('cls')
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Library')
        Cursor = cnx.cursor()
        mno = input("Enter Member No to search issued book : ")
        query = ("SELECT * FROM issue where mno = %s")
        rec_srch = (mno,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for (Bno,Mno,d_o_issue,d_o_ret) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("1.Book Code : ", Bno)
            print("2.Member Code : ", Mno)
            print("3.Date of Issue : ", d_o_issue)
            print("4.Date of Return : ", d_o_ret)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
        Cursor.close()
        cnx.close()
        print("You have done it!")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


def issueBook():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code to issue : ")
        mno = input("Enter Member Code : ")
        print("Enter Date Issue (Date/Month and Year separately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        Qry = ("INSERT INTO issue (bno,mno,d_o_issue) VALUES(%s, %s, %s) ")
        data = (bno,mno,date(YY,MM,DD))
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Recorded Inserted.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


def returnBook():
    try:
        cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Library')
        Cursor = cnx.cursor()
        bno = input("Enter Book Code of the Book to be returned to the Library : ")
        Mno = input("Enter Member Code of Member who is returning Book : ")
        retDate = date.today()
        Qry = ("""Update Issue set d_o_ret = %s WHERE BNO = %s and Mno = %s""")
        rec = (retDate, bno, Mno)
        Cursor.execute(Qry, rec)
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
