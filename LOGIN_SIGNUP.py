import json,os
b = []
user_input=input("enter what you want..login or signup = ")
if user_input=="signup":
    username=input("Enter user name for signup = ")
    def mainfun():
        global username
        password1=input("Enter your password for signup = ")
        password2=input("Re-enter conform your password for signup = ")
        for num in password1:
            if num.isdigit():
                break
        if password1==password2:
            if len(password1)>=6 and len(password1)<=10:
                print("Your both password are matching ")
                if num in password1:
                    if "#" in password1 or "@" in password1 or "$" in password1:
                        if(os.path.isfile('Signup_page.json')):
                            op=open("Signup_page.json","r")
                            a=json.load(op)
                            for i in a["User"]:
                                if i["username"]==username:
                                    print("This user is Already Exists")
                                    break
                            else:
                                dic,d={},{}
                                dic["username"]=username
                                dic["password"]=password1
                                d["description"]=input("Enter what you like = ")
                                d["Dob"]=input("Enter your date of birth = ")
                                d["Gender"]=input("Enter your gender = ")
                                d["Hobbies"]=input("Enter tour Hobbies = ")
                                dic["Profile"]=d
                                v=a["User"]
                                v.append(dic)
                                f=open("Signup_page.json","w+")
                                json.dump(a,f,indent=4)  
                                f.close()
                                print("Signup Succesfully....")
                                   
                        else:
                            
                            dic,li,d,di={},[],{},{}
                            dic["username"]=username
                            dic["password"]=password1
                            d["description"]=input("enter what you like = ")
                            d["Dob"]=input("enter your date of birth = ")
                            d["Gender"]=input("enter your gender = ")
                            d["Hobbies"]=input("enter tour Hobbies =")
                            dic["Profile"]=d
                            li.append(dic)
                            di["User"]=li
                            f=open("Signup_page.json","w+")
                            json.dump(di,f ,indent=4)
                            f.close()
                            print("Signup Succesfully....")

                    else:
                        print("At least password should contain one special character")
                else:
                    print("At least password should contain one number")
            else:
                print("your password is not valid")
        else:
            print("both password are not same")
    mainfun()

elif user_input=="login":
    c=0
    a=open("Signup_page.json","r")
    f=json.load(a)
    d=input("Enter your user name for login = ")
    v=input("Enter your password for login =         ")
    for i in f["User"]:
        if i["username"]==d:
            if d==i['username']:
                if v==i['password']:
                    print("Login successful")
                    print(i)
                    break
                else:
                    print("Check your username")
            else:
                print("Check your password")
else:
    print("Your enter worng input ")
    print("before entering anything you can check first ")