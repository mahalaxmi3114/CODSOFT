tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    if len(tasks)==0:
        print("No tasks to remove")
    else:
        print("Tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        choice = int(input("Enter the task number to remove: "))
        
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task removed successfully.")
        else:
            print("Invalid Task Number.")

def view_tasks():
    if len(tasks)==0:
        print("No Tasks.")
    else:
        print("List of tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

 
print("\n======To-Do-List Application======")

while True:
    print("\nWhat you want to do?(1/2/3/4)")
    print("1. ADD a task")
    print("2. REMOVE a task")
    print("3. VIEW all task")
    print("4. EXIT")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        print("Thankyou for using To-do-List Application!\n")
        break
    else:
        print("Invalid choice!Please try again.")



