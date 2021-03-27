import mysql.connector

def clear():
    for i in range(60):
        print()

        

def newtaxi():
    print('_________CALL TAXI BOOKING_________\n')
    mydb=mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234567890",
      database="DatabaseName")
    c=mydb.cursor()
    n=str(input('\nName: '))
    e=int(input('Earn: '))
    t=int(input('Last drop time: '))
    p=str(input('Position: '))
    c.execute("INSERT INTO TAXI(NAME,EARN,LASTDROPTIME,POSITION) VALUES('{}',{},{},'{}')".format(n,e,t,p))
    mydb.commit()
    mydb.close()
    print('\nSuccessfully Added The New Taxi!')
    c=int(input('\n1.Repeat \n2.Go back to Admin menu \n3.Exit\nChoose your option: '))
    if c==1:
        clear()
        newtaxi()
    elif c==2:
        clear()
        adminmenu()
    elif c==3:
        clear()
        choosemenu()


    
def removetaxi():
    print('_________CALL TAXI BOOKING_________')
    mydb=mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234567890",
      database="DatabaseName")
    c=mydb.cursor()
    i=int(input('ID:'))
    c.execute("SELECT COUNT(*) FROM TAXI WHERE ID={}".format(i))
    d=c.fetchall()
    if d[0][0]!=0:
        c.execute("DELETE FROM TAXI WHERE ID={}".format(i))
        
    else:
        print('No results')
    mydb.commit()
    print('\nSuccessfully Removed The Taxi!')
    mydb.close()
    c=int(input('\n1.Repeat \n2.Go back to Admin menu \n3.Exit\nChoose your option: '))
    if c==1:
        clear()
        removetaxi()
    elif c==2:
        clear()
        adminmenu()
    elif c==3:
        clear()
        choosemenu() 


    
def update():
    print('_________CALL TAXI BOOKING_________')
    mydb=mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234567890",
      database="DatabaseName")
    c=mydb.cursor()
    i=int(input('Taxi ID:'))
    c.execute("SELECT COUNT(*) FROM TAXI WHERE TID={}".format(i))
    d=c.fetchall()
    if d[0][0]!=0:
        n=str(input('Taxi Driver Name: '))
        e=int(input('Earnings: '))
        t=int(input('Last DROP Time: '))
        p=str(input('Position: '))
        c.execute("UPDATE TAXI SET NAME='{}', EARN={}, LASTDROPTIME={}, POSITION='{} WHERE TID={}'".format(n,e,t,p,i))
    else:
        print('No results')
    mydb.commit()
    mydb.close()
    print('Succesfully Altered The Taxi details!')
    c=int(input('\n1.Repeat \n2.Go back to Admin menu \n3.Exit\nChoose your option: '))
    if c==1:
        clear()
        update()
    elif c==2:
        clear()
        adminmenu()
    elif c==3:
        clear()
        choosemenu() 



    
def taxidetails():
    print('_________CALL TAXI BOOKING_________\n'.center(55))
    mydb=mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234567890",
      database="DatabaseName")
    c=mydb.cursor()
    c.execute("SELECT * FROM TAXI")
    d=c.fetchall()
    print('Taxi ID'.center(8)+'Driver Name'.center(16)+'Earnings'.center(10)+'LastDropTime'.center(16)+'Position'.center(10))
              
    for i in d:
        print(str(i[0]).center(8)+str(i[1]).center(16)+str(i[2]).center(10)+str(i[3]).center(16)+str(i[4]).center(10))
    y=str(input('\nDo you want to search individual taxi details?...(y/n): '))
    while y=='y':
        i=int(input('Id:'))
        c.execute("SELECT COUNT(*) FROM TAXI WHERE TID={}".format(i))
        d=c.fetchall()
        if d[0][0]!=0:
            c.execute("SELECT * FROM TAXI WHERE TID={}".format(i))
            d=c.fetchall()
            print("\n\nID:{} \nNAME:'{}' \nEARN:{} \nLASTDROPTIME:{} \nPOSITION:'{}'".format(d[0][0],d[0][1],d[0][2],d[0][3],d[0][4]))
        else:
            print('No results')
        y=str(input('Do you want to search MORE individual taxi details?...(y/n): '))
    mydb.commit()
    mydb.close()
    c=int(input('1.Repeat \n2.Go back to Admin menu \n3.Exit\nChoose your option: '))
    if c==1:
        clear()
        taxidetails()
    elif c==2:
        clear()
        adminmenu()
    elif c==3:
        clear()
        choosemenu() 




def bookingdetails():
    print('_________CALL TAXI BOOKING_________\n'.center(65))
    mydb=mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234567890",
      database="DatabaseName")
    c=mydb.cursor()
    c.execute("SELECT * FROM BOOKINGS")
    d=c.fetchall()
    print('Booking ID'.center(12)+'Taxi ID'.center(9)+'User ID'.center(9)+'PickUp'.center(7)+'Drop'.center(5)+'PickTime'.center(9)+'DropTime'.center(9)+'Pay'.center(5))
    for i in d:
        print(str(i[0]).center(12)+str(i[1]).center(9)+str(i[2]).center(9)+str(i[3]).center(7)+str(i[4]).center(5)+str(i[5]).center(9)+str(i[6]).center(9)+str(i[7]).center(5))
    y=str(input('Do you want to search individual taxi details?...(y/n): '))
    while y=='y':
        i=int(input('BId:'))
        c.execute("SELECT COUNT(*) FROM BOOKINGS WHERE BID={}".format(i))
        d=c.fetchall()
        if d[0][0]!=0:
            c.execute("SELECT * FROM BOOKINGS WHERE BID={}".format(i))
            d=c.fetchall()
            print("BID={} \nTID={} \nUID={} \nPICKUP='{}' \nDROPP='{}' \nPICKUP TIME={} \nDROPTIME={} \n PAY={}".format(d[0][0],d[0][1],d[0][2],d[0][3],d[0][4],d[0][5],d[0][6],d[0][7]))
        else:
            print('No Results')
        y=str(input('Do you want to search MORE individual taxi details?...(y/n): '))
    mydb.commit()
    mydb.close()
    c=int(input('1.Repeat \n2.Go back to Admin menu \n3.Exit\nChoose your option: '))
    if c==1:
        clear()
        bookingdetails()
    elif c==2:
        clear()
        adminmenu()
    elif c==3:
        clear()
        choosemenu() 



    
def user(i,n):
    print('_________CALL TAXI BOOKING_________')
    mydb=mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234567890",
      database="DatabaseName")
    c=mydb.cursor()
    t=int(input('Booking hour (24 hours format): '))
    st=['a','b','c','d','e']
    while True:
        pi=str(input('Pick up point (a-e):'))
        di=str(input('Drop point (a-e):'))
        if pi==di:
            print('Pick up and drop points are too close!')
        elif pi not in st:
            print('Service not available in the given pick up point')
        elif di not in st:
            print('Service not available in the given drop point')
        else:
            break
    if st.index(pi)==0:
        l=[pi,st[1]]
    elif st.index(pi)==len(st)-1:
        l=[pi,st[-2]]
    else:
        l=[pi,st[st.index(pi)-1],st[st.index(pi)+1]]
    c.execute("SELECT TID, NAME, EARN, LASTDROPTIME, POSITION FROM TAXI WHERE LASTDROPTIME<{} AND POSITION=('{}') ORDER BY EARN".format(t,*l))
    d=c.fetchall()
    if len(d)==0:
        print('No Taxi Available')
        c=int(input('1.Repeat \n2.Exit \nChoose your option: '))
        clear()
        if c==1:
            user(i,n)
        elif c==2:
            clear()
            choosemenu()
            
    L=[d[0][0],d[0][1],d[0][4]]
    T=int(L[0])
    DNAME=L[1]
    UNAME=n
    pickuptime=(sum([1 for i in range(abs(st.index(pi)-st.index(L[2])))]))+t
    droptime=sum([1 for i in range(abs(st.index(pi)-st.index(di)))])+t
    dist=20*sum([1 for i in range(abs(st.index(pi)-st.index(di)))])
    pay=100+(10*(dist-5))
    c.execute('INSERT INTO BOOKINGS(TID, UID, PICKUP, DROPP, PICKUPTIME, DROPTIME, PAY) VALUES({}, {}, "{}", "{}", {}, {}, {});'.format(T, i, pi, di,pickuptime,droptime,pay))
    mydb.commit()
    c.execute("UPDATE TAXI SET POSITION='{}',EARN=EARN+{}, LASTDROPTIME={} WHERE TID={}".format(di,pay,droptime,T))
    mydb.commit()
    print("Your ride has been booked and assigned to '{}', taxi no. {}".format(DNAME,T))

def adminmenu():
    print('_________CALL TAXI BOOKING_________ \n1.Add New Taxi \n2.Alter Taxi Details \n3.Get Taxi Details \n4.Get Booking Details \n5.Remove Taxi \n6.Exit')
    choose=int(input('Enter your choice: '))
    if choose==1:
        clear()
        newtaxi()
    elif choose==2:
        clear()
        update()
    elif choose==3:
        clear()
        taxidetails()
    elif choose==4:
        clear()
        bookingdetails()
    elif choose==5:
        clear()
        removetaxi()
    elif choose==6:
        clear()
        return 3


def signin():
    print('_________CALL TAXI BOOKING_________')
    i=int(input('Id:'))
    n=str(input('Name: '))
    p=str(input('Password:'))
    mydb=mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234567890",
      database="DatabaseName")
    c=mydb.cursor()
    if i==1 and n=='Admin' and p=='Admin':
        print('Signed In')
        i=input()
        clear()
        adminmenu()
    else:
        c.execute("SELECT * FROM USER WHERE UID={} AND PASSWORD='{}'".format(i,p))
        d=c.fetchall()
        if len(d)>0:
            print('Succesfully Signed In!')
            ipu=input()
            clear()
            user(i,n)
        else:
            print('Wrong Credentials!')
            clear()
            signin()
def reg():
    print('_________CALL TAXI BOOKING_________')
    n=str(input('Name:'))
    print('''Password must follow the criteria
                    1.Contains atleast 6 characters
                    2.Contains atleast 1 digit
                    3.Contains atleast 1 upper and lower case alphabets
                    4.Contains atleast 1 symbol''')
    while True:
        upass=str(input('Password :'))
        count = 0
        if len(upass)<6:
            count+=1
        if any(i.isdigit() for i in upass)==False:
            count+=1
        if any(i.islower() for i in upass)==False:
            count+=1
        if any(i.isupper() for i in upass)==False:
            count+=1
        if any(i in '!@#$%^&*()-+' for i in upass)==False:
            count+=1
        if count>0:
            print('Password not strong enough!')
        elif count==0:
            print('Password is strong!..')
            break
    mydb=mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234567890",
      database="DatabaseName")
    c=mydb.cursor()
    c.execute("INSERT INTO USER(NAME,PASSWORD) VALUES('{}','{}')".format(n,upass))
    mydb.commit()
    c.execute("SELECT MAX(UID) FROM USER ")
    d=c.fetchall()
    print('ID: {}'.format(d[0][0]))
    mydb.close()
    print('Succesfully Registered!')
    i=input()
    clear()
    signin()



def choosemenu():
    print('''_________CALL TAXI BOOKING_________

    Already an user?...''')
    choice=str(input('Yes/No ?....(y/n): '))
    if choice=='y':
        clear()
        signin()
    elif choice=='n':
        clear()
        reg()
    else:
        print('Invalid option')
        clear()
        choosemenu()
    
choosemenu()






    

            
          
    

    
    
        
     
    
    
        
        
    
    
    
    

    
    
    
            
    
    
    

