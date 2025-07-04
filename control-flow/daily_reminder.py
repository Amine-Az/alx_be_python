# daily_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority entered. Please choose from high, medium, or low.")
            return

    if time_bound == "yes":
        print(f"Reminder: {base_message} that requires immediate attention today!")
    else:
        print(f"Reminder: {base_message}. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()
