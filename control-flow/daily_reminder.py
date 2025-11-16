task =input("Enter your task")
task_Priority =input("Priority (high/medium/low) ")
time_bound =input("Is it time-bound? (yes/no): ")

match task_Priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_Priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {task_Priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_Priority} priority task that should be addressed soon.")      
        else:
            print(f"Note: '{task}' is a {task_Priority} priority task. You can schedule it for later this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_Priority} priority task. Try to get to it when possible.")      
        else:
            print(f"Note: '{task}' is a {task_Priority} priority task. It can be done at your convenience.")    