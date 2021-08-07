import json
import reminder
from datetime import datetime, timedelta, date

def login(username, password):
    with open("database.json","r") as f:
        users = json.load(f)

    is_valid_login = False
    user=None
    temp_user = users[username]
    if(temp_user != None):
        wait_period = timedelta(days=reminder.vaccine_second_dose[temp_user["brand"].lower()])
        
        date_second_dose = datetime.strptime(temp_user["first_dose"], "%Y-%m-%d") + wait_period
        str_second_dose = date_second_dose.strftime("%Y-%m-%d")

        if(temp_user["password"]==password):
            is_valid_login=True
            user={"username":username,
                  "first_name":temp_user["first_name"],
                  "last_name":temp_user["last_name"],
                  "org":temp_user["org"],
                  "brand":temp_user["brand"],
                  "first_dose":temp_user["first_dose"],
                  "second_dose": str_second_dose
                  }

    return is_valid_login, user
