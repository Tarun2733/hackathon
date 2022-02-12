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
    new_numb=StringVar()
    Label(root,text="Enter New Number:").pack()
    updated_phone=Entry(root,textvariable=new_numb)
    updated_phone.pack()
    Button(tex="Next",command=ph_next).pack()

        
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



