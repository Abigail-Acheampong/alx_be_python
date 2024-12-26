task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time_bound? (yes/no): ").lower()

match priority:
  case "high":
    reminder = f"{task} is a high priority task"
  case "medium":
    reminder = f"{task} is a medium priority task."
  case "low":
    reminder = f"{task} is a low priority task."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
  reminder += " that requires immediate attention today!"
else:
  if priority == "low":
    reminder += " Consider completing it when you have free time."
  elif priority == "medium":
    reminder += " Plan to complete it soon."

# Provide a Customized Reminder
print(f"Reminder: {reminder}")
