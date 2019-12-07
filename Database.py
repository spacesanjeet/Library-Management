"""CREATING DATABASES AND ALL THE REQUIRED TABLES NEEDED TO RUN THE PROJECT
DATABASE NAME: Library
TABLES: Bookrecord, Member, Issue"""

import mysql.connector

def DatabaseCreate():
    cnx = mysql.connector.connect(user='root', password='123', host='localhost')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS Library")
    Cursor.execute("")
    Cursor.close()
    cnx.close()


def TablesCreate():
    cnx = mysql.connector.connect(user='root', password='123', host='localhost', database='Library')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS Bookrecord(Bno int(2), Bname varchar(20), Auth varchar(20), Price int(3), Publ varchar(20), Qty int(2), Date_of_Purchase Date)")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Member(Mno int(2), Mname varchar(20), Date_of_Membership Date, Addr varchar(24), Mob varchar(10))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Issue(Bno int(2), Mno int(2), d_o_issue Date, d_o_ret Date)")
    Cursor.close()
    cnx.close()
