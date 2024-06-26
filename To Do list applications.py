def load_tasks():
  try:
    with open("tasks.txt", "r") as f:
      tasks = eval(f.read())  # Assuming simple task format (dictionary)
  except FileNotFoundError:
    tasks = {}
  return tasks
def save_tasks(tasks):
  with open("tasks.txt", "w") as f:
    f.write(str(tasks))
def main_loop():
  tasks = load_tasks()
  while True:
    command = input("Enter command (add, remove, mark, list, exit): ")
    if command == "add":
      description = input("Enter task name : ")
      priority = input("Enter priority (high, medium, low): ")
      due_date = input("Enter due date (YYYY-MM-DD, optional): ")
      tasks[len(tasks)] = {
          "description": description,
          "priority": priority,
          "due_date": due_date,
          "completed": False
      }
      save_tasks(tasks)
    elif command == "remove":
      try:
        index = int(input("Enter task index to remove: "))
        del tasks[index]
        save_tasks(tasks)
      except (ValueError, KeyError):
        print("Invalid task index.")
    elif command == "mark":
      try:
        index = int(input("Enter task index to mark: "))
        tasks[index]["completed"] = not tasks[index]["completed"]
        save_tasks(tasks)
      except (ValueError, KeyError):
        print("Invalid task index.")
    elif command == "list":
      for index, task in tasks.items():
        completion_status = "completed" if task["completed"] else "pending"
        due_date_str = f" (due: {task['due_date']})" if task["due_date"] else ""
        print(f"{index+1}. {completion_status} - {task['priority']}: {task['description']}{due_date_str}")
    elif command == "exit":
      break
    else:
      print("Invalid command. Please try again.")
if __name__ == "__main__":
  main_loop()
