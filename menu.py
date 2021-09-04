
def menuf():
    print (" Welcome to Crowd site")
    choice = input ("enter l for login or r for register:")
    if (choice == 'l'):
        import Login 
        Login.loginf()
    elif (choice == 'r'):
        import Registration
        Registration.registerf()
    else:
        input("enter l for login or r for register:")
menuf()
 

