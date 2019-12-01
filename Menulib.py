#PYTHN MODULE: MENULIB
import Book
import Member
import Issue

def Menubook():
    while True:
        Book.clrscreen()
        print("\t\t\t Book Record Management\n")
        print("==========================================================")
        print("1. Add Book Record")
        print("2. Search Book Record")
        print("3. Delete Book Record")
        print("4. Update Book Record")
        print("5. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 5 -------> : "))
        if choice == 1:
            Book.insertData()
        elif choice == 2:
            Book.SearchBookRec()
        elif choice == 3:
            Book.deleteBook()
        elif choice == 4:
            Book.UpdateBook()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuMember():
    while True:
        Book.clrscreen()
        print("\t\t\t Member Record Management\n")
        print("==========================================================")
        print("1. Add Member Record")
        print("2. Search Member Record")
        print("3. Delete Member Record")
        print("4. Update Member Record")
        print("5. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 5 ------> : "))
        if choice == 1:
            Member.insertMember()
        elif choice == 2:
            Member.SearchMember()
        elif choice == 3:
            Member.deleteMember()
        elif choice == 4:
            Member.UpdateMember()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuIssueReturn():
    while True:
        Book.clrscreen()
        print("\t\t\t Member Record Management\n")
        print("==========================================================")
        print("1. Issue Book")
        print("2. Search Issue Book Record")
        print("3. Return Issued Book")
        print("4. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 4 ------> : "))
        if choice == 1:
            Issue.issueBook()
        elif choice == 2:
            Issue.SearchIssuedBooks()
        elif choice == 3:
            Issue.returnBook()
        elif choice == 4:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")
