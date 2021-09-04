import json
import datetime
def create_post (user_id):
    title = input("title:")
    details = input("details:")
    target = input("target:")
    start_date = input("from:")
    end_date = input("to:")
    # val_date ="^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$"
    check_validation =  datetime.datetime.strptime( start_date ,'%Y-%m-%d') and datetime.datetime.strptime(start_date,'%Y-%m-%d')

    if check_validation :
        print("hioiiii")
        post_info = {'post_user_id': user_id,'title': title, 'details': details,'target': target, 'start_date':start_date, 'end_date':end_date}
        with open("posts.json", "a") as info:
                    print("yesss")
                    info.write("\n")
                    json.dump(post_info, info)
    else:
        print("please enter valid data :")    
create_post(1)
create_post(2)
