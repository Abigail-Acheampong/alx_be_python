from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"The current date and time is {formatted_datetime}.")
    return formatted_datetime, current_date
    

def calculate_future_date(current_date, number_of_days):
    future_date = current_date.date() + timedelta(number_of_days)
    return future_date
    # print(f"The future date is {future_date}.")

def main():
    _, current_date = display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date:  "))
    future_date = calculate_future_date(current_date, number_of_days)
    print(f"The future date is {future_date}.")

if __name__ == "__main__":
    main()
