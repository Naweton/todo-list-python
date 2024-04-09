from datetime import datetime

class Task:
    def __init__(self, name, date=None, hour=None):
        self.name = name
        self.date = date
        self.hour = hour
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        if self.date and self.hour:
            return f"{self.name} {self.date} {self.hour}"
        elif self.date:
            return f"{self.name} {self.date}"
        elif self.hour:
            return f"{self.name} {self.hour}"
        else:
            return self.name

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_info):
        task_parts = task_info.split()
        task_name = task_parts[0]
        date = None
        hour = None

        # Check if there's a date and/or hour
        if len(task_parts) >= 2:
            try:
                date = datetime.strptime(task_parts[-2], "%m/%d").date()
                if len(task_parts) >= 3:
                    hour = task_parts[-1]
            except ValueError:
                hour = task_parts[-1]

        task = Task(task_name, date, hour)
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task.completed else "Not Done"
                print(f"{index}. {task} - {status}")
        else:
            print("No tasks in the list.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].mark_as_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

# Main function
def main():
    todo_list = ToDoList()
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_info = input("Enter task info (e.g., 'Buy coffee 4/9 5pm'): ")
            todo_list.add_task(task_info)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
