import os

to_do_file = "to_do_list.txt"

def load_task():
    if not os.path.exists(to_do_file):
        return []
    with open(to_do_file,"r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_task(tasks):
    with open(to_do_file,"w") as file:
        for task in tasks:
            file.write(task+'\n')

def add_task(task):
    tasks = load_task()
    tasks.append(task)
    save_task(tasks)
    print(f"Task{task}added")

def view_task():
    tasks = load_task()
    if not tasks :
        print("No tasks found")

    else:
        print("Your to do list are below")

        for idx, task in enumerate(tasks,start=1):
            print(f"{idx}.{task}")

def del_task(task_number):
    tasks = load_task()
    if 1<=task_number<=len(tasks):
        remove_task = tasks.pop(task_number-1)
        save_task(tasks)
        print(f"task{remove_task} deleted")
    else:
        print ("Invalid task")

def main():
    while True:
        print("\n To Do List Application")
        print("1.Add Task")
        print("2.View Task")
        print("3.Delete Task")
        print("4.Exit")

        choice = input("Choose an Option(1-2-3-4): ")
        if choice =="1":
            task = input("Enter The Task: ")
            add_task(task)
        elif choice == "2":
            view_task()
        elif choice == "3":
            task_number = int(input("Enter The Task Number to Delete: "))
            del_task(task_number)
        elif choice == "4":
            print("Exiting The Application")
            break
        else:
            print("Invalid Choice Please Choose a Valid Option")


if __name__=="__main__":
    main()









