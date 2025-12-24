import datetime
from datetime import timedelta 
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_daytime = current_date.strftime("%Y-%m-%d %H: %M: %S")
    print(formatted_daytime)


def calculate_future_date(days_num):
    added_days = timedelta(days= days_num)
    today = datetime.datetime.now()
    future_date = today + added_days
    print("Future date:", future_date.strftime("%Y-%m-%d"))

display_current_datetime()
days = input("Enter the number of days to add to the current date: ")
days_number = int(days)
calculate_future_date(days_number)