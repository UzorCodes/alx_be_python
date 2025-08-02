from datetime import timedelta


def display_current_datetime():

    current_date = datetime.datetime.now()
    time_format = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", time_format)
    number_of_days = input("Enter the number of days to add to the current date: ")


def calculate_future_date():

    future_date.strftime = time_format + number_of_days
    print("Future date: ", future_date)

