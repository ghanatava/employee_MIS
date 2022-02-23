from datetime import *
from mysql.connector import *
mydb=connect(host='localhost',user='root',passwd='kali',database='company')
c=mydb.cursor()
def check_employee():
    employee_id= int(input('enter the id of employee:'))
    c.execute('select emp_id,first_name from employee')
    exist=dict(c.fetchall())
    if employee_id in exist.keys():
        print('employee exist')
        return True
    else:
        print('employee does not exist')
    return False
def add_employee():
    employee_id= int(input('enter the id of employee:'))
    print('checking if employee id already exist')
    if check_employee():
        c.execute('select emp_id,first_name from employee')
        exist=dict(c.fetchall())
        lst=exist.keys()
        print('chose emp_id ',max(lst)+1)
        menu()
    else:
        first_name=input('enter first_name of employee:')
        last_name=input('enter last_name of employee:')
        birth_day=input("enter date of birth,yyyy-mm-dd:")
        year,month,day = map(int,birth_day.split('-'))
        dob= date(year,month,day)
        sex=input('enter sex M,F or O:')
        salary=int(input('enter salary:'))
        sup_id=int(input('enter supervisor id 100,102 or 106:'))
        branch_id=int(input('enter branch id:'))
        data = (employee_id,first_name,last_name,birth_day,sex,salary,sup_id,branch_id)
        c.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s)",data)
        mydb.commit()
        print('employee added successfully')
        menu()
def remove_employee():
     employee_id= int(input('enter the id of employee:'))
     if check_employee() == False:
         print('employee does not exist,try again' )
         menu()
     else:
         data=(employee_id,)
         c.execute('delete from employee where emp_id=%s',data)
         mydb.commit()
         print('employee removed sucessfully')
         menu()
def promote_employee():
    employee_id= int(input('enter the id of employee:'))
    if check_employee()==False:
        print('employee does not exist,try again' )
        menu()
    else:
        amount=int(input('enter increase in salary:'))
        c.execute('select salary from employee where emp_id=%s',(employee_id,))
        r=c.fetchone()
        t=r[0]+amount
        data=(t,employee_id)
        c.execute('update employee set salary=%s where emp_id =%s',data)
        mydb.commit()
        print('employee promoted successfully')
        menu()
def display_employees():
    c.execute('select * from employee')
    data=c.fetchall()
    for i in data:
        print('emp_id:',i[0])
        print('first_name',i[1])
        print('last_name',i[2])
        print('date of birth',i[3])
        print('sex',i[4])
        print('salary',i[5])
        print('supervisor_id',i[6])
        print('branch_id',i[7])
        print('--------------------\\')
    menu()
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Check Branch of employee")
    print("6 to check branch manager id")
    print("7 to exit")
     
    # Taking choice from user
    choice = int(input("Enter your Choice "))
    if choice == 1:
        add_employee()
         
    elif choice == 2:
        remove_employee()
         
    elif choice == 3:
        promote_employee()
         
    elif choice == 4:
        display_employees()
        
    elif choice == 5:
        check_branch()
        
    elif choice == 6:
        check_branch_manager()
         
    elif choice == 7:
        exit(0)
         
    else:
        print("Invalid Choice")
        menu()
def check_branch():
    employee_id= int(input('enter the id of employee:'))
    if check_employee()==False:
        print('employee does not exist,try again' )
        menu()
    else:
        c.execute('select branch_id from employee where emp_id=%s',(employee_id,))
        r=c.fetchone()
        print('branch_id:',r[0])
        c.execute('select branch_name from branch where branch_id=%s',r)
        d=c.fetchone()
        print('branch_name:',d[0])
        menu()
def check_branch_manager():
    branch=int(input('enter branch id:'))
    if branch not in [1,2,3,4]:
        print('invalid branch id ,choose from 1,2,3,4 only.')
        menu()
    else:
        c.execute('select mgr_id from branch where branch_id=%s',(branch,))
        r=c.fetchone()
        print('Branch manager id:',r[0])
        menu()
menu()