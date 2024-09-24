import mysql.connector

def SqlCall(db,mycursor):
    import mysql.connector
    db = mysql.connector.connect(host='localhost',
                                 database='iitk_db',
                                 port=3306,
                                 user='root',
                                 password='password')
    mycursor = db.cursor()
    return db, mycursor

def LogIn():
    print()

    print("----Login----")
    print("|------------|")
    print("|1. Admin    |")
    print("|2. Expert   |")
    print("|3. Customer |")
    print("|4. Exit     |")
    print("|------------|")
    print()
    choice = int(input("Enter any one choice from the above options: "))
    print()

    # Connect to the database
    db = mysql.connector.connect(
        host='localhost',
        database='iitk_db',
        port=3306,
        user='root',
        password='password'
    )

    if choice == 1:
        print("***************")
        print("* Hello admin *")
        print("***************")
        print()
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")

        try:
            cursor = db.cursor()
            # Execute the SQL query to check admin credentials
            cursor.execute("SELECT * FROM employee WHERE empLoginId = %s AND empPassword = %s",
                           (admin_username, admin_password))

            # Fetch the result
            result = cursor.fetchone()

            if result:
                print("Login successful!")
                print("1. Customer Services")
                print("2. Employee Services")
                print("3. Bug Service")
                print()
                choice = int(input("Enter any one choice from the above options: "))
                print()
                if choice == 1:
                    print("****************************")
                    print("* Customer service section *")
                    print("****************************")
                    print("")
                    AdminCustomerServices()
                elif choice == 2:
                    print("****************************")
                    print("* Employee service section *")
                    print("****************************")
                    print("")
                    AdminEmployeeServices()
                elif choice == 3:
                    print("****************************")
                    print("* Bug service section *")
                    print("****************************")
                    print("")
                    AdminBugServices()
                else:
                    print("Enter a valid choice from the admin options")
            else:
                print("Invalid admin credentials")
                LogIn()

        except mysql.connector.Error as error:
            print("Error occurred while accessing the database: ", error)

    elif choice == 2:
        print("****************")
        print("* Hello expert *")
        print("*****************")
        print()
        expert_username = input("Enter expert username: ")
        expert_password = input("Enter expert password: ")

        try:
            cursor = db.cursor()
            # Execute the SQL query to check expert credentials
            cursor.execute("SELECT * FROM employee WHERE empLoginId = %s AND empPassword = %s",
                           (expert_username, expert_password))

            # Fetch the result
            result = cursor.fetchone()

            if result:
                print("Login successful!")
                Expert()
                # Implement expert functionality here

            else:
                print("Invalid expert credentials")
                LogIn()

        except mysql.connector.Error as error:
            print("Error occurred while accessing the database: ", error)

    elif choice == 3:
        print("****************************")
        print("* Hello customer *")
        print("****************************")
        print()
        Customer()

    elif choice==4:
        print("ThanK you")
        print("Exit")
        print()
        pass

    else:
        print("Enter a valid choice from the login page")

    # Close the database connection
    db.close()

def AdminCustomerServices():
    print("Admin Customer services Access")
    print("1.View all customer")
    print("2.Search customer by name")
    print("3.Search Customer by Login id")
    print()
    choice=int(input("Enter any one action: "))
    if choice==1:
        print("*************************")
        print("* To view all customers *")
        print("*************************")
        print("")
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                     database='iitk_db',
                                     port=3306,
                                     user='root',
                                     password='password')
        mycursor = db.cursor()
        sql = "Select * from customer"
        mycursor.execute(sql)
        allRows = mycursor.fetchall()
        print("all Customers list :")
        print()
        for row in allRows:
            # print(str(row[0]),"\t",str(row[1]),"\t\t",str(row[2]))
            print("{0:<10s} {1:<15s}{2:<40s}{3:<10s}{4:<15s}{5:<20s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]),str(row[4]),str(row[5])  ))
        print("***************************************")
        mycursor.execute(sql)
        db.close()
        LogIn()

        """mycursor = db.cursor()
        ans=mycursor.execute(
            "Select * from customer;")
        print(ans)
"""

    elif choice==2:
        print("***************************")
        print("* Search customer by name *")
        print("***************************")
        print("")
        import mysql.connector

        db = mysql.connector.connect(
            host='localhost',
            database='iitk_db',
            port=3306,
            user='root',
            password='password'
        )
        mycursor = db.cursor()

        custName = input("Enter the name of the customer to search: ")
        sql = "SELECT * FROM customer WHERE custName LIKE %s"
        mycursor.execute(sql, ('%' + custName + '%',))
        allRows = mycursor.fetchall()

        print("All Customers list:")
        print()
        for row in allRows:
            print("{0:<10s} {1:<15s}{2:<40s}{3:<10s}{4:<15s}{5:<20s}".format(
                str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])
            ))

        print("**************************************")

        mycursor.close()
        db.close()

        LogIn()



    elif choice==3:
        print("*******************************")
        print("* Search Customer by Login id *")
        print("*******************************")
        print("")
        import mysql.connector

        db = mysql.connector.connect(
            host='localhost',
            database='iitk_db',
            port=3306,
            user='root',
            password='password'
        )
        mycursor = db.cursor()

        custLoginId = input("Enter the Customer ID of the customer to search: ")
        sql = "SELECT * FROM customer WHERE custLoginId = %s"
        mycursor.execute(sql, (custLoginId,))
        allRows = mycursor.fetchall()

        print("All Customers list:")
        print()
        for row in allRows:
            print("{0:<10s} {1:<15s}{2:<40s}{3:<10s}{4:<15s}{5:<20s}".format(
                str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])
            ))

        print("************************************************************************************")

        mycursor.close()
        db.close()

        LogIn()

    else:
        print("Enetr the valid choice from AdminCutomserService")
        LogIn()


def AdminEmployeeServices():
    print("Admin Employee services Access")
    print("1.Add new(admin/expert)")
    print("2.View all Employee")
    print("3.Search Employee by name")
    print("4.Search Employee by Login id")
    print("5.Search Employee by Employee type")
    print("6.Search Employee by status(Activate/Deactivate)")
    print("7.Change Password")
    print()
    choice = int(input("Enter any one action: "))
    print()
    if choice == 1:
        print("*******************************")
        print("*     Add new(admin/expert    *")
        print("*******************************")
        print("")
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                     database='iitk_db',
                                     port=3306,
                                     user='root',
                                     password='password')
        mycursor = db.cursor()
        empLoginId =input("Enter the NEW employee Id: ")
        empPassword=input("Enter the NEW password: ")
        empType=input("Enter Employee Type(Admin?Expert): ")
        empName=input("Enter NEW Employee Name: ")
        empPhone=input("Enter the NEW Employee phone number: ")
        empEmail=input("Enter the NEW Employee Mail id: ")
        empStatus=input(("Enter the NEW employee status: "))

        sql = "INSERT INTO employee(empLoginId , empPassword , empType , empName , empPhone ,empEmail , empStatus) VALUES( %s, %s,%s, %s,%s, %s,%s ) "
        values = (empLoginId,empPassword,empType,empName,empPhone,empEmail,empStatus)
        mycursor.execute(sql, values)
        print("sql=", sql % values)
        print("Employee data inserted successfully for ",empLoginId," : ",empName )

        mycursor.close()
        db.commit()
        LogIn()

    elif choice == 2:
        print("*******************************")
        print("*     View all Employee       *")
        print("*******************************")
        print("")
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                     database='iitk_db',
                                     port=3306,
                                     user='root',
                                     password='password')
        mycursor = db.cursor()
        sql = "Select * from employee"
        mycursor.execute(sql)
        allRows = mycursor.fetchall()
        print("all Employee list :")
        print()
        for row in allRows:
            # print(str(row[0]),"\t",str(row[1]),"\t\t",str(row[2]))
            print("{0:<10s} {1:<10s}{2:<10s}{3:<30s}{4:<12s}{5:<15s}".format(str(row[0]), str(row[1]), str(row[2]),
                                                                             str(row[3]), str(row[4]), str(row[5])))
        print("************************************")
        mycursor.execute(sql)

        db.close()
        LogIn()


    elif choice == 3:
        print("*******************************")
        print("*  Search Employee by name    *")
        print("*******************************")
        print("")
        import mysql.connector

        db = mysql.connector.connect(
            host='localhost',
            database='iitk_db',
            port=3306,
            user='root',
            password='password'
        )
        mycursor = db.cursor()

        empName = input("Enter the name of the Employee to search: ")
        sql = "SELECT * FROM employee WHERE empName LIKE %s"
        mycursor.execute(sql, ('%' + empName + '%',))
        allRows = mycursor.fetchall()

        print("Employee(s) list:")
        print()
        for row in allRows:
            print("{0:<10s} {1:<15s}{2:<40s}{3:<10s}{4:<15s}{5:<20s}{6:<20s}".format(
                str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]) ))
        print("**************************************************************")
        mycursor.close()
        db.close()
        LogIn()




    elif choice == 4:
        print("*******************************")
        print("* Search Employee by Login id *")
        print("*******************************")
        print("")
        import mysql.connector

        db = mysql.connector.connect(
            host='localhost',
            database='iitk_db',
            port=3306,
            user='root',
            password='password'
        )
        mycursor = db.cursor()

        empLoginId = input("Enter the empLoginId of the Employee to search: ")
        sql = "SELECT * FROM employee WHERE empLoginId LIKE %s"
        mycursor.execute(sql, ('%' + empLoginId + '%',))
        allRows = mycursor.fetchall()

        print("Employee(s) list:")
        print()
        for row in allRows:
            print("{0:<10s} {1:<15s}{2:<10s}{3:<40s}{4:<15s}{5:<20s}{6:<20s}".format(
                str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("***************************")
        mycursor.close()
        db.close()
        LogIn()

    elif choice == 5:
        print("************************************")
        print("* Search Employee by Employee type *")
        print("************************************")
        print("")
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                     database='iitk_db',
                                     port=3306,
                                     user='root',
                                     password='password')
        mycursor = db.cursor()

        empType = input("Enter the empType of the Employee to search(Admin/Expert): ")
        sql = "SELECT * FROM employee WHERE empType LIKE %s"
        mycursor.execute(sql, ('%' + empType + '%',))
        allRows = mycursor.fetchall()

        print("Employee(s) list:")
        print()
        for row in allRows:
            print("{0:<10s} {1:<15s}{2:<10s}{3:<40s}{4:<15s}{5:<20s}{6:<20s}".format(
                str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("*************************")
        mycursor.close()
        db.close()
        LogIn()

    elif choice == 6:
            print("*************************************************")
            print("* Search Employee by status(Activate/Deactivate *")
            print("*************************************************")
            print("")
            import mysql.connector
            db = mysql.connector.connect(host='localhost',
                                         database='iitk_db',
                                         port=3306,
                                         user='root',
                                         password='password')
            mycursor = db.cursor()

            empStatus = input("Enter the empStatus of  Employee (Active/Deactive): ")
            sql = "SELECT * FROM employee WHERE empStatus LIKE %s"
            mycursor.execute(sql, ('%' + empStatus + '%',))
            allRows = mycursor.fetchall()

            print("Employee(s) list:")
            print()
            for row in allRows:
                print("{0:<10s} {1:<15s}{2:<10s}{3:<40s}{4:<15s}{5:<20s}{6:<20s}".format(
                    str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
            print("*******************************************************************")
            mycursor.close()
            db.close()
            LogIn()



    elif choice == 7:
        print("******************")
        print("*Change Password *")
        print("******************")
        print("")
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                 database='iitk_db',
                                 port=3306,
                                 user='root',
                                 password='password')
        mycursor = db.cursor()
        sql = "update employee set empPassword ='%s' where empLoginId='%s'"
        eid = input("Enter empLoginId of employee for password updattion: ")
        eps = input("Enter the new password: ")

        values = (eps, eid)
        mycursor.execute(sql % values)
        db.commit()
        if mycursor.rowcount == 1:
            print("Password Record Updateed sucefully")
        else:
            print("Password Record updattion faield ")
        db.close()
        LogIn()
    else:
        print("Enetr the valid choice from AdminEmployeeServices(")
        LogIn()


def AdminBugServices():
    print("Admin Bug services Access")
    print("1.View all Bugs")
    print("2.Search Bug by BugId")
    print("3.Search Bug by Bugstatus")
    print("4.Search Bug by custloginId")
    print("5.Assigning Expert")
    print("6.Logout")
    print()
    choice = int(input("Enter any one action: "))
    if choice == 1:
        print("*****************")
        print("* View all Bugs *")
        print("*****************")
        print("")
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                     database='iitk_db',
                                     port=3306,
                                     user='root',
                                     password='password')
        mycursor = db.cursor()
        sql = "Select * from bug"
        mycursor.execute(sql)
        allRows = mycursor.fetchall()
        print("Bug(s) list :")
        print()
        for row in allRows:
            # print(str(row[0]),"\t",str(row[1]),"\t\t",str(row[2]))
            print("{0:<5s} {1:<25s}{2:<12s}{3:<10s}{4:<12s}{5:<40s}{6:<25s}{7:<25s}{8:<20s}{9:<40s}".format(str(row[0]), str(row[1]), str(row[2]),
                                                                             str(row[3]), str(row[4]), str(row[5]) , str(row[6]), str(row[7]), str(row[8]), str(row[9])   ))
        print("***************************************************************")
        mycursor.execute(sql)

        db.close()
        LogIn()

    elif choice == 2:
        print("****************************")
        print("* Search Bug by BugId *")
        print("****************************")
        print("")
        import mysql.connector

        db = mysql.connector.connect(
            host='localhost',
            database='iitk_db',
            port=3306,
            user='root',
            password='password'
        )
        mycursor = db.cursor()

        bugId = input("Enter the bugIde to search: ")
        sql = "SELECT * FROM bug WHERE bugId LIKE %s"
        mycursor.execute(sql, ('%' + bugId + '%',))
        allRows = mycursor.fetchall()

        print("Bug(s) list:")
        print()
        for row in allRows:
            print("{0:<5s} {1:<25s}{2:<12s}{3:<10s}{4:<12s}{5:<40s}{6:<25s}{7:<25s}{8:<20s}{9:<40s}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]), str(row[4]), str(row[5]),str(row[6]),str(row[7]), str(row[8]),str(row[9]) ))
        print("*******************************************")
        mycursor.close()
        db.close()
        LogIn()


    elif choice == 3:
        print("****************************")
        print("* Search Bug by status*")
        print("****************************")
        print("")
        import mysql.connector

        db = mysql.connector.connect(
            host='localhost',
            database='iitk_db',
            port=3306,
            user='root',
            password='password'
        )
        mycursor = db.cursor()

        bugStatus = input("Enter the bugStatus to search: ")
        sql = "SELECT * FROM bug WHERE bugStatus LIKE %s"
        mycursor.execute(sql, ('%' + bugStatus+ '%',))
        allRows = mycursor.fetchall()

        print("Bug(s) list:")
        print()
        for row in allRows:
            print("{0:<5s} {1:<25s}{2:<12s}{3:<10s}{4:<12s}{5:<40s}{6:<25s}{7:<25s}{8:<20s}{9:<40s}".format(str(row[0]),
                                                                                                            str(row[1]),
                                                                                                            str(row[2]),
                                                                                                            str(row[3]),
                                                                                                            str(row[4]),
                                                                                                            str(row[5]),
                                                                                                            str(row[6]),
                                                                                                            str(row[7]),
                                                                                                            str(row[8]),
                                                                                                            str(row[
                                                                                                                    9])))
        print("***************************************************")
        mycursor.close()
        db.close()
        LogIn()

    elif choice == 4:
        print("*****************************")
        print("* Search Bug by custLoginId *")
        print("*****************************")
        print("")
        import mysql.connector

        db = mysql.connector.connect(
            host='localhost',
            database='iitk_db',
            port=3306,
            user='root',
            password='password'
        )
        mycursor = db.cursor()

        custLoginId = input("Enter the custLoginId to search: ")
        sql = "SELECT * FROM bug WHERE custLoginId LIKE %s"
        mycursor.execute(sql, ('%' + custLoginId + '%',))
        allRows = mycursor.fetchall()

        print("Bug(s) list:")
        print()
        for row in allRows:
            print("{0:<5s} {1:<25s}{2:<12s}{3:<10s}{4:<12s}{5:<40s}{6:<25s}{7:<25s}{8:<20s}{9:<40s}".format(str(row[0]),
                                                                                                            str(row[1]),
                                                                                                            str(row[2]),
                                                                                                            str(row[3]),
                                                                                                            str(row[4]),
                                                                                                            str(row[5]),
                                                                                                            str(row[6]),
                                                                                                            str(row[7]),
                                                                                                            str(row[8]),
                                                                                                            str(row[
                                                                                                                    9])))
        print("*****************************************************")
        mycursor.close()
        db.close()
        LogIn()

    elif choice == 5:
        print("*********************")
        print("* Assigning Expert  *")
        print("*********************")
        print("")
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                     database='iitk_db',
                                     port=3306,
                                     user='root',
                                     password='password')
        mycursor = db.cursor()
        bug_id = int(input("Enter the bug ID: "))
        expert_login_id = input("Enter the expert login ID: ")
        query = "UPDATE bug SET expertLoginId = %s, bugStatus = 'Assigned', expertAssignedDate = NOW() " \
                "WHERE bugId = %s"
        mycursor.execute(query, (expert_login_id, bug_id))
        db.commit()
        print("Bug assigned to expert successfully.")
        LogIn()

    elif choice == 6:
        print("*************")
        print("* Logout !  *")
        print("*************")
        print("")
        print("Thanku Very Muhc")
        LogIn()


    else:
        print("Enetr the valid choice from AdminEmployeeServices(")
        LogIn()

def Expert():
    print("Expert Access")
    print("1.View assigned Bug")
    print("2.Assigned bug status")
    print("3.Solve the BUg")
    print("4.Change the password")
    print()
    choice = int(input("Enter any one action: "))
    if choice == 1:
        print("*********************")
        print("* View assigned Bug *")
        print("*********************")
        print("")
        import mysql.connector

        db = mysql.connector.connect(
            host='localhost',
            database='iitk_db',
            port=3306,
            user='root',
            password='password'
        )
        mycursor = db.cursor()

        expertLoginId = input("Enter the  expertLoginId to search: ")
        sql = "SELECT * FROM bug WHERE  expertLoginId LIKE %s"
        mycursor.execute(sql, ('%' +  expertLoginId + '%',))
        allRows = mycursor.fetchall()

        print("Bug(s) list:")
        print()
        for row in allRows:
            print("{0:<5s} {1:<25s}{2:<12s}{3:<10s}{4:<12s}{5:<40s}{6:<25s}{7:<25s}{8:<20s}{9:<40s}".format(str(row[0]),
                                                                                                            str(row[1]),
                                                                                                            str(row[2]),
                                                                                                            str(row[3]),
                                                                                                            str(row[4]),
                                                                                                            str(row[5]),
                                                                                                            str(row[6]),
                                                                                                            str(row[7]),
                                                                                                            str(row[8]),
                                                                                                            str(row[
                                                                                                                    9])))
        print("***********************")
        mycursor.close()
        db.close()
        LogIn()

    elif choice == 2:
        print("********************************")
        print("* View status of Assigned bug  *")
        print("********************************")
        print("")
        import mysql.connector

        db = mysql.connector.connect(
            host='localhost',
            database='iitk_db',
            port=3306,
            user='root',
            password='password'
        )
        mycursor = db.cursor()

        expertLoginId = input("Enter the  expertLoginId to search: ")
        sql = "SELECT bugId,bugStatus, bugDesc,solution FROM bug WHERE  expertLoginId LIKE %s"
        mycursor.execute(sql, ('%' + expertLoginId + '%',))
        allRows = mycursor.fetchall()

        print("Bug(s) list:")
        print()
        for row in allRows:
            print("{0:<5s} {1:<25s}{2:<12s}{3:<10s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]),))
        print("**********************************************************")
        mycursor.close()
        db.close()
        LogIn()




    elif choice == 3:
        print("***********************")
        print("*   Solve the BUgs    *")
        print("***********************")
        print("")
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                     database='iitk_db',
                                     port=3306,
                                     user='root',
                                     password='password')
        mycursor = db.cursor()
        bug_id = int(input("Enter the bug ID: "))
        expert_login_id = input("Enter the expert login ID: ")
        query = "UPDATE bug SET expertLoginId = %s, bugStatus = 'Assigned', expertAssignedDate = NOW() " \
                "WHERE bugId = %s"
        mycursor.execute(query, (expert_login_id, bug_id))
        db.commit()
        print("Bug Solution given successfully.")

        LogIn()


    elif choice == 4:
        print("***********************")
        print("* Change the password *")
        print("***********************")
        print("")
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                     database='iitk_db',
                                     port=3306,
                                     user='root',
                                     password='password')
        mycursor = db.cursor()
        sql = "update employee set empPassword ='%s' where empLoginId='%s'"
        eid = input("Enter empLoginId of employee for password updattion: ")
        eps = input("Enter the new password: ")

        values = (eps, eid)
        mycursor.execute(sql % values)
        db.commit()
        if mycursor.rowcount == 1:
            print("Record Updateed sucefully")
        else:
            print("Record updattion faield ")
        db.close()

        LogIn()
    else:
        print("Invalid Expert Credentials")
        LogIn()


def Customer():
    print("Customer Section")
    print("A.Login(Existing user)")
    print("B.Signup(New_User)")
    ch=input("Enter your choice(A/B): ")
    if ch=="a" or ch=="A":
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                     database='iitk_db',
                                     port=3306,
                                     user='root',
                                     password='password')
        mycursor = db.cursor()
        customer_username = input("Enter customer username: ")
        customer_password = input("Enter customer password: ")

        try:
            cursor = db.cursor()
            # Execute the SQL query to check customer credentials
            cursor.execute("SELECT * FROM Customer WHERE custLoginId = %s AND custPassword = %s",
                           (customer_username, customer_password))

            # Fetch the result
            result = cursor.fetchone()

            if result:
                print("Login successful!")
                # Implement customer functionality here
                print("1.Update Account")
                print("2.Post new Bug")
                print("3.View all Bugs")
                print("4.Bug by Status")
                print("5.View Bug Solution")
                print("6.Change Password")
                print()
                choice = int(input("Enter any one action: "))
                if choice == 1:
                    print("******************")
                    print("* Update Account *")
                    print("******************")
                    print("")
                    import mysql.connector

                    db = mysql.connector.connect(
                        host='localhost',
                        database='iitk_db',
                        port=3306,
                        user='root',
                        password='password'
                    )
                    mycursor = db.cursor()

                    custLoginId = input("Enter the Customer Id: ")
                    custPassword = input("Enter the password: ")
                    custName = input("Enter Customer Name: ")
                    custAge = input("Enter Customer Age: ")
                    custPhone = input("Enter Customer phone number: ")
                    custEmail = input("Enter Customer Mail id: ")

                    sql = "UPDATE Customer SET custLoginId = '%s', custPassword = '%s', custName = '%s', custAge = '%s', custPhone = '%s', custEmail = '%s' WHERE custLoginId = '%s'"
                    values = (custLoginId, custPassword, custName, custAge, custPhone, custEmail, custLoginId)
                    mycursor.execute(sql % values)

                    print("SQL:", sql % values)
                    print("Employee data updated successfully: ", custName, " : ", custLoginId)
                    mycursor.close()
                    db.commit()
                    db.close()

                    LogIn()
                elif choice == 2:
                    print("******************")
                    print("* Post new Bug *")
                    print("******************")
                    print("")
                    import mysql.connector
                    db = mysql.connector.connect(host='localhost',
                                                 database='iitk_db',
                                                 port=3306,
                                                 user='root',
                                                 password='password')
                    mycursor = db.cursor()
                    cust_login_id = input("Enter your login ID: ")
                    product_name = input("Enter the product name: ")
                    bug_desc = input("Enter the bug description: ")

                    query = "INSERT INTO bug (custLoginId, productName, bugDesc) VALUES (%s, %s, %s)"
                    values = (cust_login_id, product_name, bug_desc)
                    mycursor.execute(query, values)
                    db.commit()

                    print("Bug posted successfully.")
                    LogIn()
                elif choice == 3:
                    print("******************")
                    print("* View all Bugs  *")
                    print("******************")
                    import mysql.connector
                    db = mysql.connector.connect(host='localhost',
                                                 database='iitk_db',
                                                 port=3306,
                                                 user='root',
                                                 password='password')
                    mycursor = db.cursor()
                    custLoginId= input("Enetr the customer login id")
                    sql = "Select * from bug where custLoginId= %s "
                    mycursor.execute(sql , (custLoginId,))
                    allRows = mycursor.fetchall()
                    print("Bug(s) list :")
                    print()
                    for row in allRows:
                        print(
                            "{0:<5s} {1:<20s}{2:<10s}{3:<10s}{4:<15s}{5:<35s}{6:<20s}{7:<20s}{8:<15s}{9:<15s}".format(
                                str(row[0]), str(row[1]), str(row[2]),
                                str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]),
                                str(row[9])))
                    print("**************************")
                    mycursor.execute(sql)

                    db.close()
                    LogIn()
                elif choice == 4:
                    print("****************************")
                    print("*   Search Bug by Status   *")
                    print("****************************")
                    print("")
                    import mysql.connector

                    db = mysql.connector.connect(
                        host='localhost',
                        database='iitk_db',
                        port=3306,
                        user='root',
                        password='password'
                    )
                    mycursor = db.cursor()

                    status = input("Enter the status of the Bug to search: ")
                    custLoginId = input("Enter the customer login id: ")

                    sql = "SELECT * FROM bug WHERE bugStatus = %s AND custLoginId = %s"
                    mycursor.execute(sql, (status, custLoginId))
                    allRows = mycursor.fetchall()
                    print("Bug(s) list:")
                    print()
                    print(allRows)
                    print("************************")

                    mycursor.close()
                    db.close()

                    LogIn()

                elif choice == 5:
                    print("******************")
                    print("* View Bug solution*")
                    print("******************")
                    print("")
                    import mysql.connector
                    db = mysql.connector.connect(host='localhost',
                                                 database='iitk_db',
                                                 port=3306,
                                                 user='root',
                                                 password='password')
                    mycursor = db.cursor()

                    sol = input("Enter the BUgId of the Bug to ssee soln: ")
                    sql = "Select solution from bug where  bugId =%s "
                    mycursor.execute(sql, (sol,))
                    allRows = mycursor.fetchall()
                    print("Bug(s) soln list :")
                    print()
                    print(allRows)
                    print("**********************************")
                    db.close()
                    LogIn()

                elif choice == 6:
                    print("******************")
                    print("* Change Password*")
                    print("******************")
                    print("")
                    import mysql.connector
                    db = mysql.connector.connect(host='localhost',
                                                 database='iitk_db',
                                                 port=3306,
                                                 user='root',
                                                 password='password')
                    mycursor = db.cursor()
                    sql = "update customer set custPassword ='%s' where custLoginId='%s'"
                    eid = input("Enter empLoginId of employee for password updation: ")
                    eps = input("Enter the new password: ")

                    values = (eps, eid)
                    mycursor.execute(sql % values)
                    db.commit()
                    if mycursor.rowcount == 1:
                        print("Password Updateed sucefully")
                    else:
                        print("Password updattion faield ")
                    db.close()
                    LogIn()


            else:
                print("Invalid customer credentials")
                LogIn()

        except mysql.connector.Error as error:
            print("Error occurred while accessing the database: ", error)


        else:
            print("Enetr the valid choice from AdminEmployeeServices(")
            LogIn()

    if ch=="b" or ch=="B":
            print("******************")
            print("* Create Account *")
            print("******************")
            print("")
            import mysql.connector
            db = mysql.connector.connect(host='localhost',
                                         database='iitk_db',
                                         port=3306,
                                         user='root',
                                         password='password')
            mycursor = db.cursor()
            #custLoginId | custPassword | custName | custAge | custPhone | custEmail
            custLoginId = input("Enter to Create NEW customer Id: ")
            custPassword = input("Enter NEW customer password: ")
            custName = input("Enter NEW customer Name: ")
            custAge=input("Enter the NEW Customer Age")
            custPhone=input("Enter the NEW customer phone number: ")
            custEmail = input("Enter the NEW customer Mail id: ")


            sql = "INSERT INTO customer(custLoginId , custPassword,custName,custAge,custPhone,custEmail) VALUES( %s, %s,%s, %s,%s, %s ) "
            values = (custLoginId , custPassword,custName,custAge,custPhone,custEmail)
            mycursor.execute(sql, values)

            print("sql=", sql % values)
            print("Customer data inserted successfully for ", custLoginId, " : ", custName)
            mycursor.close()
            db.commit()
            LogIn()
    else:
        print("Incoorect credential of Customer")
        LogIn()

print("Execution Started")
print("*****************")
LogIn()

print("Code execution completed")
print(""" !!!!!""")



