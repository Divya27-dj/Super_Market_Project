
import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Divya@123",
        database = "superMarket_db"
        )
        
mycursor = mydb.cursor()
    
def registerData():
        
    id = int(input("Please enter your id : "))
    fullname = input("Pleae enter your Fullname : ")
    emailid = input("Please enter your email id : ")
    buying_price = int(input("Enter total buying price : "))
    categoryname = input("Enter category name : ")
        
    sql = "insert into superMarketClothing(id, fullname, emailid, categoryname, buying_price) values (%s,%s,%s,%s,%s)"
    val = (id, fullname, emailid, categoryname, buying_price)
        
    mycursor.execute(sql,val)
    mydb.commit()
    print("Data Saved Successfully !")
        
def login():
        
    fullname = input("Please enter your full name : ")
    emailid = input("Please enter your email id : ")
        
    sql = "select * from superMarketClothing where fullname = %s and emailid = %s "
    val = (fullname, emailid)
        
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
        
    if result:
        print(f"Hi {fullname} login successfully !")
    else:
        print("Please enter correct credentials !")

"""registerData()
login()"""
            