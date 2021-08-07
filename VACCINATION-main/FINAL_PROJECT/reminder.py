import time 
from datetime import datetime, timedelta, date

#database = {"jaira@example.com": {"password": "yeung", "first_name": "Jaira", "last_name": "Yeung", "org": "MedGrocer", "brand": "sinovac", "first_dose": "2021-08-06"}, "janna@example.com": {"password": "tan", "first_name": "Janna", "last_name": "Tan", "org": "MedGrocer", "brand": "sinovac", "first_dose": "2021-07-09"}, "patricia@example.com": {"password": "hong", "first_name": "Patricia", "last_name": "Hong", "org": "LGU", "brand": "sinovac", "first_dose": "2021-06-15"}}


vaccine_second_dose= {"sinovac" : 28, 
                     "astrazeneca" : 84,
                    "gamaleya sputnik v" : 21,
                    "janssen" :1 ,
                    "bharat biotech" : 28,
                    "pfizer-biontech": 21,
                    "moderna": 28,
                    "johnson and johnson": 0,
                    "novavax" :28}



def countdown(current_user):
    today = datetime.today() - timedelta(days=1)
    days_till_second_dose = vaccine_second_dose[current_user["brand"].lower()]

    str_first_dose_date = current_user["first_dose"]
    first_dose_date = datetime.strptime(str_first_dose_date, "%Y-%m-%d")
    print("first_dose = " + str(first_dose_date)) 

    second_dose_date = first_dose_date + timedelta(days=days_till_second_dose)
    print("second_dose_date = " + str(second_dose_date))
    
    days_to_first_dose = first_dose_date - today
    print("days_to_first_dose = " + str(days_to_first_dose))

    days_to_second_dose = second_dose_date - today
    print("days_to_second_dose = " + str(days_to_second_dose))
    
    return days_to_first_dose.days, days_to_second_dose.days
    
