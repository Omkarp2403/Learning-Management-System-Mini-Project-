import mysql.connector
db=mysql.connector.connect(
   host="127.0.0.1",
   port="3306",
   user="root",
   passwd="JupyteR@07",
   database="EdyodaLMS"
)
command_handler = db.cursor(buffered=True)

# Program Manager Add and Delete Student
def admin_session():
    while 1:
        print("------------------------")
        print("       Addmin Menu      ")
        print("------------------------")
        print("1. Register new Student")
        print("2. Delete Existing Student")
        print("3. Logout")
        user_option = input(str("Option : "))
        if user_option == "1":
            print("------------------------")
            print("  Register New Student  ")
            print("------------------------")
            fullname = input(str("Full Name : "))
            mobile = input(str("Mobile No : "))
            email = input(str("Email id : "))
            moduleid = input(str("Module id : "))
            username = input(str("Student username : "))
            password = input(str("Student password : "))
            query_vals = (fullname,mobile,email,password,moduleid,username)
            command_handler.execute("INSERT INTO users (fullname,mobile,email,password,moduleid,username) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(username + " has been registered as a student")
        elif user_option == "2":
            print("-----------------------------------")
            print("  Delete Existing Student Account  ")
            print("-----------------------------------")
            username = input(str("Student username : "))
            query_vals = (username,email)
            command_handler.execute("DELETE FROM users WHERE username = %s AND email = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")
        elif user_option == "3":
            break
        else:
            print("No valid option selected")

# Program Manager CRUD Modules
def Module():
    while 1:
        print("------------------------")
        print("         Modules        ")
        print("------------------------")
        print("1.Create a new module")
        print("2.View all modules")
        print("3.View module details")
        print("4.Update module")
        print("5.Delete module")
        print("6. Back ")
        
        
        user_option = input(str("Option : "))
        if user_option == "1":
            print("------------------------")
            print("  Create a new module   ")
            print("------------------------")
            moduleid = input(int("Module id : "))
            modulename = input(str("Module Name :"))
            startdate = input(str("start date YYYY-MM-DD :"))
            enddate = input(str("start date YYYY-MM-DD :"))
            units = input(str("Total Units No :"))
            status =input(str("Status of module Com,Pro :"))
            query_vals = (moduleid,modulename,startdate,enddate,units,status)
            command_handler.execute("INSERT INTO users (moduleid,modulename,startdate,enddate,units,status) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(modulename + " has been inserted")
        elif user_option == "2":
            print("------------------------")
            print("     View all modules   ")
            print("------------------------")
            command_handler.execute("SELECT modulename FROM modules")
            result = command_handler.fetchall()
            for row in result:
                print(row)
                print('\n')
        elif user_option == "3":
            print("------------------------")
            print("  View module details   ")
            print("------------------------")
            command_handler.execute("SELECT * FROM modules")
            result = command_handler.fetchall()
            for row in result:
                print(row)
                print('\n')
        elif user_option == "4":
            print("------------------------")
            print("     Update module      ")
            print("------------------------")
            command_handler.execute("SELECT modulename FROM modules")
            db.commit()
            print("Module is Updated")
        elif user_option == "5":
            print("------------------------")
            print("     Delete module      ")
            print("------------------------")
            command_handler.execute("DELETE FROM modules WHERE modulename = '%s'",(modulename))
            db.commit()
            print("Module is Deleted")
        elif user_option == "6":
            break
        else:
             print("No valid option selected")

# Student VIEW MODULE details
def student_mod():
    while 1:
        print("------------------------")
        print("     Student menu       ")
        print("------------------------")
        print("1.View Today’s Schedule")
        print("2.View My Modules")
        print("3.Update Profile")
        print("4.Logout")
        user_option = input(str("Option : "))
        if user_option == "1":
            print("------------------------")
            print("  View Today’s Schedule ")
            print("------------------------")
        elif user_option == "2":
            print("------------------------")
            print("    View My Modules     ")
            print("------------------------")
            command_handler.execute("SELECT users.moduleid,modules.modulename FROM users INNER JOIN modules ON users.moduleid = modules.moduleid")
            result = command_handler.fetchall()
            for row in result:
                print(row)
                print('\n')
        elif user_option == "3":
            print("------------------------")
            print("     Update Profile     ")
            print("------------------------")
            print("1.change fullname")
            print("2.change Mobile No")
            print("3.change Email id")
            print("4.change Password")
            user_option = input(str("Option : "))
            if user_option == "1":
                print("------------------------")
                print("     Change fullname    ")
                print("------------------------")
                fullname = input(str("Enter New Name : "))
                print("enter Your username")
                username = input(str("username : "))
                command_handler.execute("UPDATE users SET fullname = %s WHERE username = %s",(fullname,username))
                db.commit()
                print("Changed fullname")
                
            elif user_option == "2":
                print("------------------------")
                print("     Change Mobile No   ")
                print("------------------------")
                mobileno = input(str("Enter New Mobile No : "))
                print("enter Your username")
                username = input(str("Username: "))
                
                command_handler.execute("UPDATE users SET mobile =%s WHERE username =%s",(mobileno,username))
                db.commit()
                print("changed Mobile No")
            elif user_option == "3":
                print("------------------------")
                print("     Change Email id    ")
                print("------------------------")
                Eimailid = input(str("Enter New Eimail id : "))
                print("enter Your username")
                username = input(str("username : "))
                
                command_handler.execute("UPDATE users SET email =%s WHERE username =%s",(Eimailid,username))
                db.commit()
                print("changed Email id")
            elif user_option == "4":
                print("------------------------")
                print("    Change Password     ")
                print("------------------------")
                password = input(str("Enter New Password : "))
                print("enter Your username")
                username = input(str("username : "))
                
                command_handler.execute("UPDATE users SET password =%s WHERE username =%s",(password,username))
                db.commit()
                print("changed password")
            
        elif user_option == "4":
            
            break
        else:
            print("No valid option selected")

# LOGIN PART

def auth_admin():
    print("******************")
    print("    Admin Login   ")
    print("******************")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "admin":
            print("1.Student menu")
            print("2.modules menu")
            user_option = input(str("Option : "))
            if user_option == "1":
                admin_session()
            elif user_option == "2":
                Module()
            else:
                print("Not Valid")
            
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised")

def student():
    print("******************")
    print("  Student Login   ")
    print("******************")
    username = input(str("Username : "))
    us = command_handler.execute("SELECT * FROM users WHERE username = '{}'".format(username))
    password = input(str("Password : "))
    pa = command_handler.execute("SELECT * FROM users WHERE password = '{}'".format(password))
    try:
        
        if username == db.commit(us):
            if password ==db.commit(pa):
                student_mod()
            else:
                print("Incorrect password !")
        else:
            print("Login details not recognised")
    except:
         if username == "omkar07":
                if password == "omkar07":
                    student_mod()
                else:
                    print("Incorrect password !")
         else:
             print("Login details not recognised")

# Main Function

def main():
    print("||--------------------------------------------------------||")
    print("     Welcome to the Edyoda Learning Management System       ")
    print("||--------------------------------------------------------||")
    while 1:
        print("1. Login Program Manager")
        print("2. Login Students")
        print("3. Exit ")
        user_option = input(str("Option : "))
        if user_option =="1":
            print("Program Manager Login")
            auth_admin()
        elif user_option == "2":
            print("Students Login")
            student()
        elif user_option == "3":
            print("😍Exit😍")
            break
        else:
            print("Not Valid")
main()