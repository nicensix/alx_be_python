task = input("Enter your task for today: ")
priority = input("Enter the priority of your task (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task. Please complete it as soon as possible."
    case "medium":
        reminder = f"'{task}' is a medium priority task. Please complete it today."
    case "low":
        reminder = f"'{task}' is a low priority task. You can complete it at your convenience."
    case _:
        reminder = f"'{task}' has an unknown priority. Please clarify."
if time_bound == "yes":
    reminder += " This task is time-bound, so please ensure it is completed on time."
elif time_bound == "no":
    reminder += "Consider completing this task when you have time."
else:
    reminder += " The time-bound status of this task is unclear."
print("Reminder:", reminder)