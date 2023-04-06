# import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

# function to define database
def Database():
    global conn, cursor
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STU1(STU_ID INTEGER PRIMARY KEY NOT NULL, STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT)")


# GUI
def DisplayForm():
    root = Tk()
    root.geometry("1000x500")
    root.title("Student Management System (BY Arshdeep Kaur Deol)")
    global tree
    global SEARCH
    global name, contact, email, rollno, branch
    SEARCH = StringVar()
    name = StringVar()
    contact = StringVar()
    email = StringVar()
    rollno = StringVar()
    branch = StringVar()
    # creating frames for layout
    TopViewForm = Frame(root, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    # first left frame for registration from
    LFrom = Frame(root, width="350", bd=7)
    LFrom.pack(side=LEFT, fill=Y)
    # seconf left frame for search form
    LeftViewForm = Frame(root, width=500, bg="gray", bd=7)
    LeftViewForm.pack(side=LEFT, fill=Y)
    # mid frame for displaying students record
    MidViewForm = Frame(root, width=600)
    MidViewForm.pack(side=RIGHT)
    # Heading
    lbl_text = Label(TopViewForm, text="Student Management System", font=('Arial Bold', 25), width=700, bg="red",
                     fg="white")
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LFrom, text="Enter Student Details", font=('Arial Bold', 14), bg="yellow")
    lbl_txtsearch.pack()
    Label(LFrom, text="Name  ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=name).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Email ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=email).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Rollno ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=rollno).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Branch ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=branch).pack(side=TOP, padx=10, fill=X)
    Button(LFrom, text="Submit", font=("Arial", 10, "bold"), command=register).pack(side=TOP, padx=10, pady=5, fill=X)

    ##Label For Search
    lbl_txtsearch = Label(LeftViewForm, text="Enter name to Search", font=('Arial bold', 14), bg="yellow")
    lbl_txtsearch.pack()
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    # Buttons
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData)
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_update = Button(LeftViewForm, text="Update", command=updateRecord)
    btn_update.pack(side=TOP, padx=10, pady=10, fill=X)
    # scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Name", "Contact", "Email", "Rollno", "Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    # setting headings for the columns
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Rollno', text="Rollno", anchor=W)
    tree.heading('Branch', text="Branch", anchor=W)
    # setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=150)
    tree.column('#2', stretch=NO, minwidth=0, width=175)
    tree.column('#3', stretch=NO, minwidth=0, width=230)
    tree.column('#4', stretch=NO, minwidth=0, width=150)
    tree.pack()
    DisplayData()


# function to insert data into database
def register():
    Database()
    name1 = name.get()
    con1 = contact.get()
    email1 = email.get()
    rol1 = rollno.get()
    branch1 = branch.get()
    # Validation
    if name1 == '' or con1 == '' or email1 == '' or rol1 == '' or branch1 == '':
        tkMessageBox.showinfo("Warning", "fill the empty field!!!")
    elif (len(con1) != 10):
        tkMessageBox.showinfo("Warning", "Enter valid Number !!!")
    elif not (".com" or ".org" or ".edu" or ".gov" or ".net" or "@") in email1:
        tkMessageBox.showinfo("Warning", "Enter valid email !!!")
    else:
        conn.execute('INSERT INTO STU1(STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_BRANCH) \
              VALUES (?,?,?,?,?)', (name1, con1, email1, rol1, branch1));
        conn.commit()
        tkMessageBox.showinfo("Message", "Stored successfully")
        DisplayData()
        conn.close()


# Reset
def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
    name.set("")
    contact.set("")
    email.set("")
    rollno.set("")
    branch.set("")
    # DElete


def Delete():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning", "Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor = conn.execute("DELETE FROM STU1 WHERE STU_ROLLNO = %d" % int(selecteditem[3]))
            conn.commit()
            cursor.close()
            conn.close()


# Update
def updateRecord():
    Database()
    name = name.get()
    con1 = contact.get()
    email1 = email.get()
    rol1 = rollno.get()
    branch1 = branch.get()
    conn.execute("UPDATE STU1 SET  STU_NAME=name1,STU_CONTACT=con1,STU_EMAIL=email1,STU_ROLLNO=rol1,STU_BRANCH=branch1")
    conn.commit()
    tkMessageBox.showinfo("Message", "Update successfully")
    DisplayData()
    conn.close()


# search data
def SearchRecord():
    Database()
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor = conn.execute(
            "SELECT STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_BRANCH FROM STU1 WHERE STU_NAME LIKE ?",
            ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


# Display data
def DisplayData():
    Database()
    tree.delete(*tree.get_children())
    cursor = conn.execute("SELECT STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_BRANCH FROM STU1")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


DisplayForm()
if __name__ == '__main__':
    mainloop()


