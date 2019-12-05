# Library-Management
![](https://cdn.discordapp.com/attachments/519576119503224842/652223060157399049/rainbow_line.gif)
Library Management Project.
1) To initialize the project, you need to have database named **Library** with tables namely **Bookrecord**, **member**, and **issue** inside it respectively.
2) You can accordingly may change the database name, the password to your local MYSQL and other tables names.
3) To create the database use the following code snippet: ```create database Library;```
4) That should create your database inside MYSQL, which you can check with ```show databases;```
5) To create the respective tables inside database **Library** use the following code snippets.
  - ```create table Bookrecord (bno int(3), bname varchar(14), Auth varchar(14), price int(3), publ varchar(14), date Date);```
  - ```create table member (mno int(3), mname varchar(14), date Date, addr varchar(14), mob varchar(14);```
  - ```create table issue (bno int(3), mno int(3), d_o_issue Date, d_o_ret Date);```
6) You can always change the values provided in the code to customize them according to your needs.
7) To use the Library Management Project, just download the files provided here and run the file named **Library Management.py** to get started.
