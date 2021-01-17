import os
import platform
import mysql.connector

def selection():
    db = mysql.connector.connect(user='roor',password="2759", host="localhost" , database='mysql')
    cursor = db.cursor()
    print('\nWelcome To School Management System\n')
    print('1.Student Management\n2.Employment Management\n3.Fee Management\n4.Exam Managenent')
    ch=int(input("\nEnter choice:[1-4]"))
    if ch==1 :
        print('\nWelcome To Student Management System\n')
        print('a.New admission\nb.Update student details\nc.Issue TC\n')
        c=input("\nEnter choice:[a-c]")
        print("Initial Details:\n")
        display1()
        if c=='a':
            insert1()
            print("\nModified details:\n")
            display1()
        elif c=='b':
            update1()
            print("\nModified details:\n")
            display1()
        elif c=='c':
            delete1()
            print("\nModified details:\n")
            display1()
        else:
            print("Enter correct Choice")
    elif ch==2:
        print('\nWelcome To Employee Management System\n')
        print('a.New employee\nb.Update staff details\nc.Delete employee\n')
        c=input("\nEnter choice:[a-c]")
        if c=='a':
            insert2()
            print("\nModified details:\n")
            display2()
        elif c=='b':
            update2()
            print("\nModified details:\n")
            display2()
        elif c=='c':
            delete2()
            print("\nModified details:\n")
            display2()
        else:
            print("Enter correct Choice")
    elif ch==3:
        print('\nWelcome To FEE Management System\n')
        print('a.New fee\nb.Update fee details\nc.Exempt Fee\n')
        c=input("\nEnter choice:[a-c]")
        if c=='a':
            insert3()
        elif c=='b':
            update3()
        elif c=='c':
            delete3()
        else:
            print("Enter correct Choice")
    elif ch==4:
        print('\nWelcome To Exam Management System\n')
        print('a.Exam Details\nb.Update exam details\nc.Delete Exam Details\n')
        c=input("\nEnter choice:[a-c]")
        if c=='a':
            insert4()
        elif c=='b':
            update4()
        elif c=='c':
            delete4()
        else:
            print("Enter correct Choice")
    else:
            print("Enter correct Choice")

def insert1():
    sname=input("Enter Name:")
    admno=int(input("Enter Admn No :"))
    dob=input("Enter Dob[yyyy-mm-dd]:")
    cls=input("Class of Admission:")
    cty=input("Enter City:")
    db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
    cursor=db.cursor()
    sql="INSERT INTO student(sname,admno,dob,cls,cty)VALUES('%s','%d','%s','%s','%s')"%(sname,admno,dob,cls,cty)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()
        
def display1():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM student"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
            print("(sname=%s,admno=%d,dob=%s,cls=%s,cty=%s)"%(sname,admno,dob,cls,cty))
    except:
        print("Error: Unable to fetch data")
        db.close()

def update1():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM student"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print("Error: Unable to fetch data")
    print()
    tempst=int(input("Enter Admission no.:"))
    temp=input("Enter new class:")
    try:
        sql="UPDATE student set cls=%s where admno=%d" %(temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete1():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM student"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print("Error: Unable to fetch data")
    print()
    temp=int(input("Enter Admission no. to delete:"))
    try:
        sql="DELETE from student where admno=%d" %(temp)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

    
def insert2():
    ename=input("Enter Emp Name:")
    empno=int(input("Enter Emp No :"))
    job=input("Enter Designation:")
    hiredate=input("Enter joining date:")
    db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
    cursor=db.cursor()
    sql="INSERT INTO emp(ename,empno,job,hiredate)VALUES('%s','%d','%s','%s')"%(ename,empno,job,hiredate)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()
        
def display2():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM emp"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            ename=c[0]
            empno=c[1]
            job=c[2]
            hiredate=c[3]
            print("(ename=%s,empno=%d,job=%s,hiredate=%s)"%(ename,empno,job,hiredate))
    except:
        print("Error: Unable to fetch data")
        db.close()

def update2():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM emp"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            ename=c[0]
            empno=c[1]
            job=c[2]
            hiredate=c[3]
    except:
        print("Error: Unable to fetch data")
    print()
    tempst=int(input("Enter Emp no.:"))
    temp=input("Enter new designation:")
    try:
        sql="UPDATE emp set job=%s where empno=%d" %(temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete2():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM emp"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            ename=c[0]
            empno=c[1]
            job=c[2]
            hiredate=c[3]
    except:
        print("Error: Unable to fetch data")
    print()
    temp=int(input("Enter Emp no. to delete:"))
    try:
        sql="DELETE from emp where empno=%d" %(temp)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()


def insert3():
    admno=int(input("Enter Admn No :"))
    fee=float(input("Enter fee amt:"))
    month=input("Enter month:")
    db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
    cursor=db.cursor()
    sql="INSERT INTO fee(admno,fee,month)VALUES('%d','%d','%s')"%(admno,fee,month)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display3():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM fee"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            admno=c[0]
            fee=c[1]
            month=c[2]
            print("(admno=%d,fee=%d,month=%s)"%(admno,fee,month))
    except:
        print("Error: Unable to fetch data")
        db.close()

def update3():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM fee"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            admno=c[0]
            fee=c[1]
            month=c[2]
    except:
        print("Error: Unable to fetch data")
    print()
    tempst=int(input("Enter Admn no.:"))
    temp=input("Enter new cls:")
    try:
        sql="UPDATE fee set month=%s where admno=%d" %(temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete3():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM fee"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            admno=c[0]
            fee=c[1]
            month=c[2]
    except:
        print("Error: Unable to fetch data")
    print()
    temp=int(input("Enter Admn no. to delete:"))
    try:
        sql="DELETE from fee where admno=%d" %(temp)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()


def insert4():
    sname=input("Enter Name:")
    admno=int(input("Enter Admn No :"))
    per=float(input("Enter Percentage:"))
    res=input("Enter Result:")
    db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
    cursor=db.cursor()
    sql="INSERT INTO exam(sname,admno,per,res)VALUES('%s','%d','%d','%s')"%(sname,admno,per,res)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display4():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM exam"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            per=c[2]
            res=c[3]
            print("(sname=%s,admno=%d,per=%d,res=%s)"%(sname,admno,per,res))
    except:
        print("Error: Unable to fetch data")
        db.close()

def update4():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM exam"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            per=c[2]
            res=c[3]
    except:
        print("Error: Unable to fetch data")
    print()
    tempst=int(input("Enter Admission no.:"))
    temp=input("Enter new res:")
    try:
        sql="UPDATE exam set res=%s where admno=%d" %(temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()

def delete4():
    try:
        db=mysql.connector.connect(user='root', password='tiger', host='localhost', database='mysql')
        cursor=db.cursor()
        sql="SELECT * FROM exam"
        cursor.execute(sql)
        results=cursor.fetchall()
        for c in results:
            sname=c[0]
            admno=c[1]
            per=c[2]
            res=c[3]
    except:
        print("Error: Unable to fetch data")
    print()
    temp=int(input("Enter Admission no. to delete:"))
    try:
        sql="DELETE from exam where admno=%d" %(temp)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()
selection()
