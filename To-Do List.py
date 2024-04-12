def save_tasks(tasks, filename):
    try:
        with open(filename, 'w') as f:
            for task in tasks:
                f.write(task['task'] + ',' + str(task['done']) + '\n')
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                task, done = line.strip().split(',')
                tasks.append({"task": task, "done": done == 'True'})
        print("Tasks loaded successfully.")
        return tasks
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
        return tasks
    except Exception as e:
        print(f"Error loading tasks: {e}")

def main():
    tasks = []
    filename = "todo_list.txt"  # Default filename

    while True:
        print("\n===== Command-line based To-Do List Application using Python =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Track Lists")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks, start=1):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                print("Task deleted!")
            else:
                print("Invalid task number.")

        elif choice == '5':
            print("1. Save Tasks")
            print("2. Load Tasks")
            track_choice = input("Enter your choice: ")
            if track_choice == '1':
                save_tasks(tasks, filename)
            elif track_choice == '2':
                tasks = load_tasks(filename)

        elif choice == '6':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
