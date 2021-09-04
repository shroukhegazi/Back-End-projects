import json
def view_posts(user_id):
    with open('posts.json') as view_file:
        list = []
        view_file = open('posts.json')
        for line in view_file:
            dict = json.loads(line)
            if dict['post_user_id'] == user_id:
                print ("hii")
                list.append(dict)
            
        if len(list) == 0:
            print("no posts for you ")
        else:
            print("your projects :")
            for dict in list:
                print(dict['title'])
    
view_posts(1)

    