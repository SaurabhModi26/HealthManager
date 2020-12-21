#---------------------------Programmer's Comments----------------------------------------

"""
Health Manager program is the project wherein you can log and retrieve following :
1. Exercises done by user.
2. Food Items Eaten by user.
3. To display time of activity(Taken Automatically From System Clock).
"""

"""
Note :
This Program makes :
1. "username_ex.txt" file for storing Exercises of the user.
2. "username_food.txt" file for storing food items of the user.
3. Time and Date are taken from System clock(Please Sync System Clock to internet 
   before using Health Manager).
"""

"""
Regarding Scope of Program :  
1. There is no Database for this program so cannot find user history.
2. No Validation is done Existing User.
3. If username is not found in Existing User Column then a new record is being
   created by that username to continue.
"""
#----------------------------------------------------------------------------------------

from sys import exit

def gettime() :
    import datetime
    return datetime.datetime.now()

def userlogin() :
    user=int(input("\nPress :\n1. Existing User Signin\n2. New User Signin\n\nEnter : "))
    if user==1 :
        existing()
    elif user==2 :
        new()
    else :
        print("\nGive valid choice.")
        userlogin()

def new():
    username=input("\nEnter Username : ")
    print("\nUsername created Successfully!!")
    work(username)

def existing() :
    username=input("\nEnter Username : ")
    work(username)

def work(username) :
    direction=int(input("\nPress :\n1. Log\n2. Retrieve\nEnter choice : "))
    if direction==1 :
        log(username)
    elif direction==2 :
        retrieve(username)
    else :
        print("\n!!Give valid choice!!")
        work(username)

def log(username) :
    activity=int(input("\nPress :\n1. Enter Exercise\n2. Enter Food\nEnter choice : "))
    if activity==1 :
        enter_ex(username)
    elif activity==2 :
        enter_food(username)
    else :
        print("\n!!Give valid choice!!")
        log(username)

def enter_ex(username) :
    exercise=input("\nEnter Exercise you did : ")

    with open(username+"_ex.txt","a") as p:
        p.write(str([str(gettime())])+" : "+exercise+"\n")
    print("\nYour Exercise and its Time are Successfully added.")

    ender=int(input("\n\nPress :\n1. To Add new Exercise\n2. To Add new Food Item\n3. To view your Exercise History\n4. To view your Food History\n5. To exit\n6. Login as New User\nEnter choice : "))
    
    if ender==1 :
        enter_ex(username)
    elif ender==2 :
        enter_food(username)
    elif ender==3 :
        ret_ex(username)
    elif ender==4 :
        ret_food(username)
    elif ender==5 :
        print("\n\nThanks For Using Health Manager\nVisit again to add more....")
        exit()
    elif ender==6 :
        print("You have Successfully Logged out of",username)
        print("\nThanks For using Health Manager\nVisit Again to Add More....")
        userlogin()
    else :
        print("\n\nAdd valid choice!!\nHealth Manager has Saved your data\nOpen Again to continue....")
        exit()
    
def enter_food(username) :
    food=input("\nEnter food Item's name : ")

    with open(username+"_food.txt","a") as p :
        p.write(str([str(gettime())])+" : "+food+"\n")
    print("\nYour Food Item's Name and Time of Eating are Successfully added.")

    ender=int(input("\n\nPress :\n1. To Add new Exercise\n2. To Add new Food Item\n3. To view your Exercise History\n4. To view your Food History\n5. To exit\n6. Login as New User\nEnter choice : "))
    
    if ender==1 :
        enter_ex(username)
    elif ender==2 :
        enter_food(username)
    elif ender==3 :
        ret_ex(username)
    elif ender==4 :
        ret_food(username)
    elif ender==5 :
        print("\n\nThanks For Using Health Manager\nVisit again to add more....")
        exit()
    elif ender==6 :
        print("You have Successfully Logged out of",username)
        print("\nThanks For using Health Manager\nVisit Again to Add More....")
        userlogin()
    else :
        print("\n\nAdd valid choice!!\nHealth Manager has Saved your data\nOpen Again to continue....")
        exit()
    
def retrieve(username) :
    activity=int(input("\nPress :\n1. Retrieve Exercise\n2. Retrieve Food\nEnter choice : "))
    if activity==1 :
        ret_ex(username)
    elif activity==2 :
        ret_food(username)
    else :
        print("\n!!Give valid choice!!")
        retrieve(username)

def ret_ex(username) :
    print("\nExercises you did are : \n")

    with open(username+"_ex.txt") as p :
        print(p.read())
    
    ender=int(input("\n\nPress :\n1. To Add new Exercise\n2. To Add new Food Item\n3. To view your Exercise History\n4. To view your Food History\n5. To exit\n6. Login as New User\nEnter choice : "))
    
    if ender==1 :
        enter_ex(username)
    elif ender==2 :
        enter_food(username)
    elif ender==3 :
        ret_ex(username)
    elif ender==4 :
        ret_food(username)
    elif ender==5 :
        print("\n\nThanks For Using Health Manager\nVisit again to add more....")
        exit()
    elif ender==6 :
        print("You have Successfully Logged out of",username)
        print("\nThanks For using Health Manager\nVisit Again to Add More....")
        userlogin()
    else :
        print("\n\nAdd valid choice!!\nHealth Manager has Saved your data\nOpen Again to continue....")
        exit()
    
def ret_food(username) :
    print("\nFood Items who have eaten are : \n")

    with open(username+"_food.txt") as p :
        print(p.read())
    
    ender=int(input("\n\nPress :\n1. To Add new Exercise\n2. To Add new Food Item\n3. To view your Exercise History\n4. To view your Food History\n5. To exit\n6. Login as New User\nEnter choice : "))
    
    if ender==1 :
        enter_ex(username)
    elif ender==2 :
        enter_food(username)
    elif ender==3 :
        ret_ex(username)
    elif ender==4 :
        ret_food(username)
    elif ender==5 :
        print("\n\nThanks For Using Health Manager\nVisit again to add more....")
        exit()
    elif ender==6 :
        print("You have Successfully Logged out of",username)
        print("\nThanks For using Health Manager\nVisit Again to Add More....")
        userlogin()
    else :
        print("\n\nAdd valid choice!!\nHealth Manager has Saved your data\nOpen Again to continue....")
        exit()

print("\nHealth Manager")
userlogin()