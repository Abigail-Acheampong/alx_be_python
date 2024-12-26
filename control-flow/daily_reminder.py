task_variable = input("Enter your task: ")
priority_level = input("Priority (high/medium/low): ").lower()
time_bound_variable = input("Is it time_bound? (yes/no): ").lower()

match priority_level:
  case "high":
    reminder = f"{task_variable} is a high priority task"
  case "medium":
    reminder = f"{task_variable} is a medium priority task."
  case "low":
    reminder = f"{task_variable} is a low priority task."

# Modify the reminder if the task is time-bound
if time_bound_variable == "yes":
  reminder += " that requires immediate attention today!"
else:
  if priority_level == "low":
    reminder += " Consider completing it when you have free time."
  elif priority_level == "medium":
    reminder += " Plan to complete it soon."

# Provide a Customized Reminder
print(f"Reminder: {reminder}")
