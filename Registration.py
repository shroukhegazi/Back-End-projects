import re 
import json
def registerf(user_id):
    user_id =+1
    fname =input ("Enter Your First Name:")
    lname =input ("Enter Your last Name:")
    email =input ("Enter Your mail:")
    val = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matchi= re.fullmatch(val , email)
    if matchi :
        print ('valid mail!')
        password =input ("Enter Your password:")
        confirm= input ("Enter Your password again:")
        if password == confirm:
            print ('correct password!')
            phone = input ("Enter Your phone number:")
            if (re.fullmatch("^01[0125][0-9]{8}$", phone)):
                userinfo = {'fname': fname, 'lname': lname,'email': email, 'password':password, 'confirm':confirm, 'phone' : phone  }
                print ('valid phone number!')
                with open("users.json", "a") as data:
                    print("yesss")
                    data.write("\n")
                    json.dump(userinfo, data)
                
            else:
                input("enter a valid phone number:")
                registerf(user_id)   
        else:
            input("Doesn't match! Re-enter your password:")
            registerf(user_id)   

    else:
        input("enter a valid email:") 
        registerf(user_id)   



registerf(1)              