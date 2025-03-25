
import requests
import smtplib
import databaseconn

url = "http://demo6036820.mockable.io/dummy_data"

def get_data():
    response = requests.get(url)

    if response.status_code == 200:
        get_data=response.json()
        print(get_data)
        choice = input("Do you want to order something from our catelogue? Please ener your choice : ").lower()
        quantity = int(input("Please enter how much quantity you need : "))

        if choice in get_data:
            price_category = get_data[choices]
            
        else:
            print("Please enter valid choice")

        total_amount = quantity * price_category
        print(f"Your Total Amount of order is {total_amount} .")
        print("Please Register / Login Account to generate a Bill")
        print("1. Register Account    2. Login Account")
        choices = int(input("Please enter your choice [1-2] : "))
        if choices == 1:
            databaseconn.registerData()
        elif choices == 2:
            databaseconn.login()
        else:
            print("Please enter valid choice !")
                
    else:
        print("API link is not activated.")
        
    
    sender_email="divyaj501@gmail.com"
    mail_or_text_bill = input("Wants to get email or bill for your purchase ?")
    
    if mail_or_text_bill == "email":
        receiver_mail = input("Please share your gmail id to generate a bill for your purchase : ")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, "egascfzwffckkbmu")
        message = f"Hello! The total price of the {choice} is {total_amount}. Thank you for your purchase."

        try:
            s.sendmail(sender_email, receiver_mail, message)
            print("mail sent successfully")
            s.quit()
        except:
            print("mail not sent")
    else:
        print(f"Hello! The total price of the {choices} is {total_amount}. Thank you for your purchase.")

        
get_data()
    
    