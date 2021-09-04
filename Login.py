# from Registration import email, password
# from CreatePost import create_post
# from edit_post import edit_post
# from view_posts import view_posts
# from search_posts import search_posts
import json
def loginf ():
    list = []
    mail= input ("Enter Your email:")
    your_password = input ("Enter Your Password:")
    
    importusers = open("users.json")
    # print(type(importusers))
    # print(importusers.read())
    users = json.load(importusers)
    print("before loop")
    for line in users:
        print("through the  first loop")
        Dict = json.loads(line)
        list.append(Dict)
   
    for dict in list:
        print("hiii from inside the second loop")
        if (mail == dict ['email'] )and (your_password == dict['password']):
            print("login successful")
            user_id = dict['user_id']
            if (choice == 'c'):
                import CreatePost
                CreatePost.create_post()
            elif (choice == 'v'):
                import view_posts
                view_posts.view_posts()
            elif (choice == 'e'):
                import edit_post
                edit_post.edit_post()
            elif (choice == 'd'):
                import delete_post
                delete_post.delete_post()
            elif (choice == 's'):
                import search_posts
                search_posts.search_posts()  
            else:
                input("enter c for create or v for view or e for edit or d for delet or s for search:")
            
        else:
            print("invalid data ,, please try again")

    print("I didn't get inside loops")
           
                    
loginf()


    
        

   
   