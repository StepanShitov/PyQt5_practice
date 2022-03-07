import json
import re

import json_editor

def upload_users():
    users = json_editor.get_users()
    if type(users) == str or len(users) == 0:
        return []
    else:
        return users

def create_new_user(user_name):
    existing_users = upload_users()
    status = json_editor.add_new_user(user_name, existing_users)
    status = json_editor.setup_workspace(user_name)
    return(status)
        

def get_number_of_users():
    return len(upload_users())

def get_user_progress(username):
    with open(f"users_logs/{username}_logs.json") as user_data:
        try:
            data = json.load(user_data)
            if data["points"]["previous_added"] == False:
                data = check_last_week_results(data)
            print(data)
            return("")
        except json.decoder.JSONDecodeError:
            return("File is empty")

def check_last_week_results(last_week_data):
    last_week_habits_results = last_week_data["habits"]
    if len(last_week_habits_results) > 0:
        for habit in last_week_habits_results.values():
            # If there are more than 2 free days without any progress - No points
            if (re.search(r"0{2,}", habit) == None and 
                len(re.findall(r"0", habit)) <= 2):
                point_achieved = True
            else:
                point_achieved = False
                break
        if point_achieved == True:
            last_week_data["points"]["balance"] += 1
        # Set weekdays to default value
        for habit in last_week_data["habits"].keys():
            last_week_data["habits"][habit] = "1111111"
        last_week_data["points"]["previous_added"] = True
        return last_week_data