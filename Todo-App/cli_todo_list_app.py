from sys import exit

class ToDo:

    def __init__(self, name, task, priority, is_completed):
        self.name = name
        self.task = task
        self.priority = priority
        self.is_completed = is_completed

    def __str__(self):
        return f"Name: {self.name} | Task: {self.task} | Priority: {self.priority} | Completed: {self.is_completed}"


print("Welcome to SmashedFrenzy16's to-do list app! \n")

tasks = []

while True:

    def create_task():

        name = input("Enter in the task name: ")
        task = input("Enter in task details: ")
        priority = input("Enter in task priority (High/Medium/Low): ")
        is_completed = input("Enter in whether the task has been completed or not: ")

        todo_item = ToDo(name, task, priority, is_completed)

        tasks.append(todo_item)

    def delete_task():

        index = input("Enter in the index of the task that you want to delete: ")

        tasks.pop(int(index))

    def update_task():

        name_of_task = input("Enter in the name of the task you want to update: ")
        
        for task in tasks:

            if task.name == name_of_task:

                task.name = input("Enter in the new task name (leave blank to keep the same): ") or task.name
                task.task = input("Enter in the new task description (leave blank to keep the same): ") or task.task
                task.priority = input("Enter in the new task priority (High/Medium/Low) (leave blank to keep the same): ") or task.priority
                task.is_completed = input("Enter in whether the task is completed or not (leave blank to keep the same): ") or task.is_completed

                print("Task has been updated.")

            else:

                print("Task was not found.")    


    def task_list():

        print("This is the list of all of your tasks:")

        count = 0

        for task in tasks:

            print(count, task)

            count = count + 1

    print("These are the following options to choose from: ")
    print("1. Create a task")
    print("2. Delete a task")
    print("3. View all tasks")
    print("4. Exit\n")

    choice = input("Enter in your option (1, 2, 3 or 4): ")

    if choice == "1":

        create_task()

    elif choice == "2":

        delete_task()

    elif choice == "3":

        task_list()
    
    elif choice == "4":

        exit()
