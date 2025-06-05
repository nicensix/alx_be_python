from datetime import datetime, timedelta  # Import necessary components

def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it as YYYY-MM-DD HH:MM:SS
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: ").strip())  # Get user input
    current_date = datetime.now()  # Get the current date
    future_date = current_date + timedelta(days=number_of_days)  # Calculate future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format it as YYYY-MM-DD
    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()