import mysql.connector
DB_HOST="localhost"
DB_USER="root"
DB_PORT=3306
DB_PASSWORD="Abinaya@638264"
DB_NAME="abinaya"

def get_connection():
    try:
        conn=mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            port=DB_PORT,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to database:", e)
        return None
    
def create_account():
    conn = get_connection()
    if conn is None:
        return
    account_holder=input("Enter account holder name: ")
    pin=input("Set a 4-digit PIN: ")
    balance_text=input("Enter initial deposit amount: ")
    if  not pin or not balance_text.isdigit():
        print("Invalid input. Please try again.")
        return
    if len(pin)!=4:
        print("pin must be four digit")
        return
    
    balance=int(balance_text)
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bank_info (account_holder, pin, balance) VALUES (%s, %s, %s)", (account_holder, pin, balance))
    conn.commit()
    print("Account added successfully.")
    
    cursor.close()
    conn.close()
    
def view_accounts():
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT id, account_holder, balance FROM bank_info")
    accounts = cursor.fetchall()
    
    print("Account ID | Account Holder | Balance")
    print("---------------------------------------")
    for account in accounts:
        print(f"{account[0]} | {account[1]} | {account[2]}")
    
    cursor.close()
    conn.close()

def update_acc_info():
    conn=get_connection()
    if conn is None:
        return
    
    id=input("Enter the id :").strip()
    if not id.isdigit():
        print("Please,Enter valid input id")
        return
    new_balance=input("Enter your current balance:")
    new_pin=input("Enter your current pin:")
    
    cursor=conn.cursor()
    cursor.execute("UPDATE bank_info SET balance=%s,pin=%s WHERE id=%s",(new_balance,new_pin,id))
    print("Upated successfully")
    conn.commit()
    cursor.close()
    conn.close()
    
def delete_account():
    conn=get_connection()
    if conn is None:
        return
    
    id=input("Enter the id to delete account:").strip()
    if not id.isdigit():
        print("Please,Enter valid input id")
        return
    
    cursor=conn.cursor()
    cursor.execute("DELETE FROM bank_info WHERE id=%s",(id,))
    print("Deleted successfully")
    conn.commit()
    cursor.close()
    conn.close()
    
    
def main():
    print("***Bank Management System***")
    while True:
        print("1.Create Account,2.View Account,3.Update Account,4.delete,5.Exit")
        choice=input("Enter your choice(1-5):")
        
        if choice=="1":
            create_account()
        elif choice=="2":
            view_accounts()
        elif choice=="3":
            update_acc_info()
        elif choice=="4":
            delete_account()
        elif choice=="5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("As per your request the process is exit from action")
            break

if __name__ == "__main__":
     main()
     