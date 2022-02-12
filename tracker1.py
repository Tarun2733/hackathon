import mysql.connector as a
# import pyttsx3
from random import *





def password():
    password=input("Enter new strong password : ")
    p="@@".join(password)
    if len(password) >= 8:
        try:
            sql="UPDATE user_info set passwd=%s WHERE id=%s"
            values=(p,user_id)
            cursor.execute(sql,values)
            mydb.commit()
            print("Password Updated\n------------------")
        except:
            print("Error Occured")
            main()
    else:
        print("password less than 8 is not allowed.\n---------------")
        main()

def update_phone():
    updated_phone=int(input("Enter 10 Digit new Phone : "))
    if len(str(updated_phone)) == 10:
        try:
            sql="UPDATE user_info set User_phno=%s WHERE user_id=%s"
            values=(updated_phone,user_id)
            cursor.execute(sql,values)
            mydb.commit()
            print("Phone Number Updated. Please Login Again.\n------------------")
            login()
        except mysql.connector.Error as e:
            print(e)
            main()
    else:
        print("password less than 8 is not allowed.\n")
        main()

def update():
    user_ch_3 = int(input("Enter 1 for phone and 2 for password to change another key to exit: "))

    if user_ch_3 == 1:
        update_phone()
    elif user_ch_3 == 2:
        password()
    else:
        print("Something went wrong...\n-------------")
        main() 
        
def show_available_trackers():
    print("Remember the Tracker ID of the Tracker you are planning to book")
    sql = "Select trackerID,seatAvail From driverInfo;"
    cursor = mydb.cursor()
    cursor.execute(sql)
    row=cursor.fetchall()
    print(row)
    c = input("Do you want to go back to main menu(Y/N")
    if c=="Y" or "y":
        main()
    else:
        print("staying on the current page:")
        show_available_trackers()


def book():
    tracker = input("Enter the Tracker ID:")
    phno = int(inout("Enter your phone number:"))
    gen = input("Enter you gender(M/F):")
    j_date = input("Enter Journey date:")
    srt_point = input("Enter your current location: ")
    end_point = input("Enter your destination: ")
    number = int(input("Enter the number of ticket you want to book : "))

    for i in range(1, number + 1):
        n = input("Enter Passanger name  : ")
        age = int(input("Enter Passanger age : "))
        try:
            sql = "INSERT INTO Book (trackerID,name,user_phno,gender,j_date,str_Point,end_Point) VALUES ('{}',{},'{}','{}',{},{},'{}','{}')".format(
                tracker, n, age, phno, gen, j_date, srt_point, end_point,)
            cursor.execute(sql)
            mydb.commit()
            print(i, " ticket registered\n")
        except exception as e:
            print(e)
    main()
    
def enquiry():
    print("Driver Info:\n")

    sql = "Select phNo, drName, VacStat From driverInfo"
    cursor = mydb.cursor()
    cursor.execute(sql)
    mydb.commit()
    main()


def  report_iss():
    pass

def reciept():
    pass

def main():

    print("Welcome")
    print("-----------------------Menu------------------------\n")
    print("1-Show Available Trackers \n 2- Book Tracker \n 3-Enquiry of driver \n 4- Report Issue \n 5-Generate reciept\n ")
    print("")
    user_inp=int(input("Input your choice:"))
    if(user_inp==1):
        show_available_trackers()
    elif(user_inp==2):
        book()
    elif(user_inp==3):
        enquiry()
    elif(user_inp==4):
        report_iss()
    elif(user_inp==5):
        reciept()
    else:
        print("Sorry your Input is Invalid please try again ")
        main()

def login():
    global phone
    global user_id
    phone = int(input("Enter your Phone number of 10 Digit : "))
    password = input("Enter your password : ")
    p="@@".join(password)
    if len(str(phone))==10 or len(str(password))>=8:
      try:
        sql="SELECT * FROM user_info WHERE User_phno='{}' and passwd='{}';".format(phone,p)
        cursor=mydb.cursor()
        cursor.execute(sql)
        a=cursor.fetchone()
        user_id=a[0]
        data=cursor.rowcount
        if data==1:
            main()
        else:
            print("\nIncorrect details\n--------------")
            login()
      except:
        print("\nError Occured. Your details may be incorrect.\n--------------")
        log_sign()
    else:
        print("Invalid pnone number login again\n------------")
        login()
        
def signup():
    ui=int(input("Enter user ID:"))
    usename=input("Enter your username : ")
    age = int(input("Enter your age:"))
    gen = input("Enter your gender(M/F):")
    password=input("Enter your password : ")
    c_pass=input("Enter your password again : ")
    if password==c_pass and len(str(password))>=8:
        p="@@".join(password)
        phone=int(input("Enter your Phone number : "))

        r1=randrange(100,200)
        r2=randrange(100,200)
        print("Prove You are not robot ",r1,"+",r2)
        user_ans=int(input("Enter your Ans : "))
        if user_ans==r1+r2:
            if len(str(phone))==10:
              try:
                cursor=mydb.cursor()
                sql="INSERT INTO user_info (user_id,name,age,User_phno,gender,passwd) VALUES ({},'{}','{}','{}','{}','{}')".format(ui,usename, age, phone, gen, p)
                cursor.execute(sql)
                mydb.commit()
                print("Account Created succesfully\n---------------")
                log_sign()
              except:
                  print("Failed. The account may exist.\n-----------")
            print("Invalid Phone Number signup again\n--------------")
            signup()
        else:
                print("Wrong Ans signup again.\n--------------------")
                signup()

    else:
        print("Password does't matched\n------------- ")
        log_sign()


def log_sign():
    print("1. Sign Up\n2. Login\n3. See map and fee structure\n--------------------- ")

    user_ch_1=int(input("Enter Choice : "))
    if user_ch_1==1:
        signup()
    elif user_ch_1==2:
        login()
    elif user_ch_1==3:
        mapp()
    else:
        print("Wrong input chosen")
        log_sign()
        
        
try:
    
    global mydb
    user_id=""
    mydb=a.connect(host="localhost",user="root",passwd="Mapa@11dec",database="tracker")
    cursor=mydb.cursor()
    if user_id=="":
       log_sign()
    if user_id!="":
       main()
       
except:
    print("The server is probably not runnng....")        