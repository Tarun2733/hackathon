from tkinter import *

root = Tk()
root.title("Tracker Booking")

Label(root, text="Starting Page", font="lucida 20 bold").pack()
#photo = PhotoImage(file="tracker.PNG")
#pic=Label(image=photo)
#pic.pack()
import mysql.connector as a
import pyttsx3
from random import *

def main2():
    Label(root,text="-----------============Welcome===========-------------- \n").pack()
    Label(root,text="-----------------------Menu------------------------\n").pack()


    Button(text="1-Show Available Trackers ",command=show_available_trackers).pack()


    Button(text="2- Book Tracker", command=book).pack()

    Button(text="3-Enquiry of driver",command=enquiry).pack()

    #Button(text="4- Report Issue",command=report_iss).pack()

    #Button(text="5-Generate reciept",command=reciept).pack()

    Button(text="6- Update",command=update).pack()

    #Button(text="7-Cancellation",command=cancel).pack()

def show_available_trackers():
    Label(root,text="Remember the Tracker ID of the Tracker you are planning to book\n").pack()

    sql = "Select trackerID,seatAvail From driverInfo;"
    cursor = mydb.cursor()
    cursor.execute(sql)
    row=cursor.fetchall()
    Label(root,text=f"{row}").pack()

    Button(text="Main Menu",command=main2).pack()
    Button(text="Refresh",command=show_available_trackers).pack()

def book():
    tracker = StringVar()
    Label(root, text="Enter the Tracker ID : ").pack()
    tracker_entry1 = Entry(root, textvariable=tracker)
    tracker_entry1.pack()

    # n = input("Enter Passanger name  : ")
    n = StringVar()
    Label(root, text="Enter Passenger name :").pack()
    n1 = Entry(root, textvariable=n)
    n1.pack()

    # phno = int(input("Enter your phone number:"))
    phno = IntVar()
    Label(roots, text="Enter your phone number:").pack()
    ph = Entry(root, textvariable=phno)
    ph.pack()

    # gen = input("Enter you gender(M/F):")
    gen = StringVar()
    Label(roots, text="Enter you gender(M/F) :").pack()
    g1 = Entry(root, textvariable=gen)
    g1.pack()

    now = datetime.now()

    bookdate = now.strftime("%Y-%m-%d %H:%M:%S")
    # j_date = input("Enter the date of journey : ")
    j_date = IntVar()
    Label(roots, text="Enter the date of journey:").pack()
    d11 = Entry(root, textvariable=j_date)
    d11.pack()

    # srt_point = input("Enter your current location: ")
    srt_point = StringVar()
    Label(roots, text=" Enter your current location :").pack()
    sr1 = Entry(root, textvariable=srt_point)
    sr1.pack()

    # end_point = input("Enter your destination: ")
    end_point = StringVar()
    Label(roots, text=" Enter your destination :").pack()
    en1 = Entry(root, textvariable=end_point)
    en1.pack()

    # num_seat = int(input("Enter the number of ticket you want to book : "))
    num_seat = IntVar()
    Label(roots, text="Enter the number of ticket you want to book :").pack()
    se1 = Entry(root, textvariable=num_seat)
    se1.pack()

    try:
        sql = "INSERT INTO Book (trackerID , name, user_phno, gender, num_seats, Book_Date, j_date, str_Point, end_Point) VALUES({}, {}, {}, {}, {}, {}, {},{}, {});".format(
            tracker, n, phno, gen, num_seat, bookdate, j_date, srt_point, end_point)
        cursor.execute(sql)
        mydb.commit()

        sql = "SELECT name, trackerID, num_seats ,j_date, str_point, end_point FROM Book WHERE user_phno = '{}'  ".format(
            phno)
        cursor.execute(sql)
        row = cursor.fetchall()
        Label(root, text=f"{row}").pack()

        Label(root, text="ticket registered").pack()
    except exception as e:
        Label(root, text=f"{e}")
    main()


def enquiry():
    Label(root,text="Driver Info:\n").pack()
    sql = "Select phNo, drName, VacStat From driverInfo"
    cursor = mydb.cursor()
    cursor.execute(sql)
    row=cursor.fetchall()
    Label(root,text=f"{row}").pack()

    Button(text="Main Menu",command=main2).pack()
    Button(text="Refresh",command=enquiry).pack()

#def report_iss():
 #   pass


#def reciept():
 #   pass


def cancel():
    Label(root, text="Go to view ticket section to know your ticket id.\n--------------------").pack()

    phno = IntVar()
    Label(roots, text="Enter your phone number:").pack()
    ph1 = Entry(root, textvariable=phno)
    ph1.pack()

    try:
        sql = "SELECT * FROM book WHERE User_phno={};".format(phno)
        cursor.execute(sql)
        a = cursor.fetchall()
        Label(root, text=f"{a}").pack()

        confirmation = StringVar()
        Label(root, text=" Do you want to cancel the above ticket? [y/n] :").pack()
        confi1 = Entry(root, textvariable=confirmation)
        confi1.pack()
        Button(text="Next", command=check_confirm).pack()
    except:
        Label(root, text="Canceling Terminated.....").pack()
        main()

def pass_check():
    if len(password2) >= 8:
        try:
            sql = "UPDATE user_info set passwd=%s WHERE id=%s"
            values = (p, user_id)
            cursor.execute(sql, values)
            mydb.commit()
            Label(root, text="Password Updated\n------------------").pack()
        except:
            Label(root,text="Error Occured").pack()
            main()
    else:
        Label(root,text="password less than 8 is not allowed.\n---------------").pack()
        main()


def password():
    global password2
    password2 = StringVar()
    pass2_entry = Entry(root,textvariable=password2)
    pass2_entry.pack()

    p = "@@".join(password2)
    Button(text="Next", command=pass_check).pack()
    Button(text="Refresh", command=password).pack()


def ph_next():
    if len(str(updated_phone)) == 10:
        try:
            sql = "UPDATE user_info set User_phno=%s WHERE user_id=%s"
            values = (updated_phone, user_id)
            cursor.execute(sql, values)
            mydb.commit()
            Label(root, text="Phone Number Updated. Please Login Again.\n------------------").pack()
            Button(text="Login", command=login).pack()
        except mysql.connector.Error as e:
            Label(root, text=f"{e}").pack()
            main()

    else:
        Label(root, text="password less than 8 is not allowed.\n").pack()
        main()


def update_phone():
    new_numb = IntVar()
    Label(root, text="Enter New Number:").pack()
    updated_phone = Entry(root, textvariable=new_numb)
    updated_phone.pack()
    Button(text="Next", command=ph_next).pack()
    Button(text="Refresh", command=update_phone).pack()


def update():
    Button(text="Update phone number",command=update_phone).pack()

    Button(text="Update password",command=password).pack()

    Button(text="Main Menu",command=main2).pack()

def main():
    Label(root,text="-----------============Welcome===========-------------- \n").pack()
    Label(root,text="-----------------------Menu------------------------\n").pack()

    Button(text="1-Show Available Trackers ",command=show_available_trackers).pack()

    Button(text="2- Book Tracker", command=book).pack()

    Button(text="3-Enquiry of driver",command=enquiry).pack()

    Button(text="4- Report Issue",command=report_iss).pack()

    Button(text="5-Generate reciept",command=reciept).pack()

    Button(text="6- Update",command=update).pack()

    Button(text="7-Cancellation",command=cnacel).pack()

def log_sign2():
    Button(text="Signup", command=signup).pack()

    Button(text="Login", command=login).pack()
        # write =Label(text="1. Sign Up\n2. Login\n3. See map and fee structure\n--------------------- ")
        # write.pack()



def login_check():
    if len(str(phone)) == 10 or len(str(password3)) >= 8:
        try:
            sql = "SELECT * FROM user_info WHERE User_phno='{}' and passwd='{}';".format(phone, p)
            cursor = mydb.cursor()
            cursor.execute(sql)
            a = cursor.fetchone()
            global user_id
            user_id = a[0]
            data = cursor.rowcount
            if data == 1:
                main()
            else:
                Label(text="\nIncorrect details\n--------------").pack()
                login()
        except:
            Label(text="\nError Occured. Your details may be incorrect.\n--------------").pack()
            log_sign()
    else:
        Label(text="Invalid pnone number login again\n------------").pack()
        login()




def login():
    global phone
    #global user_id
    phone=IntVar()
    Label(text="Enter your Phone number of 10 Digit : ").pack()
    phone_entry=Entry(root,textvariable=phone)
    phone_entry.pack()
    global password3
    password3 = StringVar()
    Label(root,text="Enter your password : ").pack()
    password_enter=Entry(root,textvariable=password3)
    password_enter.pack()
    Button(text="Refresh", command=login).pack()
    Button(text="Next", command=login_check).pack()
    Button(text="Back", command=log_sign2).pack()

    p = "@@".join(password3)

def signup():
    Label(root, text="Enter your user id : ").pack()
    ui= IntVar()
    ui_enter = Entry(root,textvariable=ui)
    ui_enter.pack()
    usename= StringVar()
    Label(root,text="Enter your username : ").pack()
    name_entry = Entry(root, textvariable=usename)
    name_entry.pack()
    age=IntVar()
    Label(root, text="Enter your age:").pack()
    age_entry = Entry(root, textvariable=age)
    age_entry.pack()
    gen=StringVar()
    Label(root, text="Enter your gender(M/F):").pack()
    gen_entry = Entry(root, textvariable=gen)
    gen_entry.pack()
    #global password4
    password4 = StringVar()
    Label(root, text="Enter your password : ").pack()
    password_entry = Entry(root, textvariable=password4)
    password_entry.pack()
    #global c_pass
    c_pass = StringVar()
    Label(root, text="Enter your password again : ").pack()
    c_pass_entry = Entry(root, textvariable=c_pass)
    c_pass_entry.pack()

     #name_entry.pack()
    #age_entry.pack()
    #gen_entry.pack()
    #password_entry.pack()
    #c_pass_entry.pack()

    #else:
        #pass_not_match=Label(text="Password does't matched\n------------- ")
       # pass_not_match.pack()
       # log_sign()
    Button(text="Back",command=log_sign).pack()
    Button(text="Refresh", command=signup).pack()
    Button(text="Next", command=signup_check).pack()


def signup_check():
    if password4 == c_pass and len(str(password4)) >= 8:
       # p = "@@".join(password4)
        Label(root,text="Enter your phone number")
        global phone
        phone = IntVar()
        phoneEntry = Entry(root, textvariable=phone)
        phoneEntry.pack()

        r1 = randrange(100, 200)
        r2 = randrange(100, 200)
        robot = Label(root,text="Prove You are not robot ")
        robot.pack()
        random_num=Label(root,text=f"{r1} + {r2}")
        random_num.pack()

        check_ans= Label(root,text="Enter your Ans : ")
        check_ans.pack()
        user_ans = IntVar()
        user_ans_entry= Entry(root,textvariable= user_ans)
        user_ans_entry.pack()
        if user_ans == r1 + r2:
            if len(str(phone)) == 10:
                try:
                    cursor = mydb.cursor()
                    sql = "INSERT INTO user_info (user_id,name,age,User_phno,gender,passwd) VALUES ({},'{}','{}','{}','{}','{}')".format(
                        ui, usename, age, phone, gen, p)
                    cursor.execute(sql)
                    mydb.commit()
                    ac=Label(root,text="Account Created succesfully\n---------------")
                    ac.pack()
                    log_sign()
                except:
                    failed=Label(text="Failed. The account may exist.\n-----------")
                    failed.pack()
                    invalid_num=Label(text="Invalid Phone Number signup again\n--------------")
                    invalid_num.pack()
                    signup()
        else:
            wrong=Label(text="Wrong Ans signup again.\n--------------------")
            wrong.pack()
            signup()


def d_display():
    sql="Select * from book;"
    cursor=mydb.cursor()
    cursor.execute(sql)
    row=cursor.fetchall()
    Label(root,text=f"{row}")
    Button(text="Log out",command=log_sign).pack()

def dlogin():
    #tid=input("Enter tracker id:")
    tid=StringVar()
    Label(roots,text=" Enter tracker id :").pack()
    tid1=Entry(root,textvariable=tid)
    tid1.pack()

    #n=input("Enter name:")
    n=StringVar()
    Label(root,text="Enter name :").pack()
    n2=Entry(root,textvariable=n)
    n2.pack()

    Label(root,text="You are logged in!").pack()
    d_display()

def log_sign():
    Button(text="Signup", command=signup).pack()

    Button(text="Login", command=login).pack()

    Button(text="Driver's Login", command=dlogin).pack()




try:

    global mydb
    user_id = ""
    mydb = a.connect(host="localhost", user="root", passwd="passwd123", database="tracker")
    cursor = mydb.cursor()
    if user_id == "":
        log_sign()
    if user_id != "":
        main()

except:
    print("The server is probably not runnng....")

B1= Button(text="Start", command = log_sign).pack()

root.mainloop()
