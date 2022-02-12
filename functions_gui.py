def show_available_trackers():
    Label(root,text="Remember the Tracker ID of the Tracker you are planning to book\n").pack()

    sql = "Select trackerID,seatAvail From driverInfo;"
    cursor = mydb.cursor()
    cursor.execute(sql)
    row=cursor.fetchall()
    Label(root,text=f"{row}").pack()

    Button(text="Main Menu",command=main).pack()
    Button(text="Refresh",command=show_available_trackers).pack()
   

 def enquiry():
    Label(root,text="Driver Info:\n").pack()
    sql = "Select phNo, drName, VacStat From driverInfo"
    cursor = mydb.cursor()
    cursor.execute(sql)
    row=cursor.fetchall()
    Label(root,text=f"{row}").pack()

    Button(text="Main Menu",command=main).pack()
    Button(text="Refresh",command=enquiry).pack()


    def update():
    Button(text="Update phone number",command=update_phone).pack()

    Button(text="Update password",command=password).pack()

    Button(text="Main Menu",command=main).pack()

def ph_next():
    if len(str(updated_phone)) == 10:
        try:
            sql="UPDATE user_info set User_phno=%s WHERE user_id=%s"
            values=(updated_phone,user_id)
            cursor.execute(sql,values)
            mydb.commit()
            Label(root,text="Phone Number Updated. Please Login Again.\n------------------").pack()
            Button(text="Login",command=login).pack()
        except mysql.connector.Error as e:
            Label(root,text=f"{e}").pack()
            main()
            
    else:
        Label(root,text="password less than 8 is not allowed.\n").pack()
        main()
        
def update_phone():
    new_numb=IntVar()
    Label(root,text="Enter New Number:").pack()
    updated_phone=Entry(root,textvariable=new_numb)
    updated_phone.pack()
    Button(tex="Next",command=ph_next).pack()
    Button(text="Refresh",command=update_phone).pack()

 
def book():
    tracker= StringVar()
    Label(root,text="Enter the Tracker ID : ").pack()
    tracker_entry1=Entry(root,textvariable=tracker)
    tracker_entry1.pack()

   # n = input("Enter Passanger name  : ")
    n=StringVar()
    Label(root,text="Enter Passenger name :").pack()
    n1=Entry(root,textvariable=n)
    n1.pack()

   # phno = int(input("Enter your phone number:"))
    phno=IntVar()
    Label(roots,text="Enter your phone number:").pack()
    ph=Entry(root,textvariable=phno)
    ph.pack()

    #gen = input("Enter you gender(M/F):")
    gen=StringVar()
    Label(roots,text="Enter you gender(M/F) :").pack()
    g1=Entry(root,textvariable=gen)
    g1.pack()

    now = datetime.now()

    bookdate = now.strftime("%Y-%m-%d %H:%M:%S")
    #j_date = input("Enter the date of journey : ")
    j_date=IntVar()
    Label(roots,text="Enter the date of journey:").pack()
    d11=Entry(root,textvariable=j_date)
    d11.pack()

    #srt_point = input("Enter your current location: ")
    srt_point=StringVar()
    Label(roots,text=" Enter your current location :").pack()
    sr1=Entry(root,textvariable=srt_point)
    sr1.pack()

    #end_point = input("Enter your destination: ")
    end_point=StringVar()
    Label(roots,text=" Enter your destination :").pack()
    en1=Entry(root,textvariable=end_point)
    en1.pack()

    #num_seat = int(input("Enter the number of ticket you want to book : "))
    num_seat = IntVar()
    Label(roots,text="Enter the number of ticket you want to book :").pack()
    se1=Entry(root,textvariable=num_seat)
    se1.pack()


    try:
        sql = "INSERT INTO Book (trackerID , name, user_phno, gender, num_seats, Book_Date, j_date, str_Point, end_Point) VALUES({}, {}, {}, {}, {}, {}, {},{}, {});".format(tracker,n, phno, gen, num_seat ,bookdate ,j_date, srt_point, end_point)
        cursor.execute(sql)
        mydb.commit()

        sql = "SELECT name, trackerID, num_seats ,j_date, str_point, end_point FROM Book WHERE user_phno = '{}'  ".format(phno)
        cursor.execute(sql)
        row=cursor.fetchall()
        Label(root,text=f"{row}").pack()

        Label(root,text=f"{ticket registered}").pack()
    except exception as e:
        Label(root,text=f"{e}")
    main()

        
def main():
    Label(root,text="-----------============Welcome===========-------------- \n").pack()
    Label(root,text=("-----------------------Menu------------------------\n").pack()

    Button(text="1-Show Available Trackers ",command=show_available_trackers).pack()

    Button(text="2- Book Tracker", command=book).pack()

    Button(text="3-Enquiry of driver",command=enquiry).pack()

    Button(text="4- Report Issue",command=report_iss).pack()

    Button(text="5-Generate reciept",command=reciept).pack()

    Button(text="6- Update",command=update).pack()

    Button(text="7-Cancellation",command=cnacel).pack()


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
          
          

