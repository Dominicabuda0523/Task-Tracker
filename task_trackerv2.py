import json
from datetime import datetime

short_now = datetime.now().replace(second=0, microsecond=0)
created_id = 0


def add_task(add_entry):

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {"tasks": []}
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)

    for items in data["tasks"]:
        items = items["id"]

    try:
        create_id = items + 1
    except UnboundLocalError:
        create_id = 1

    formatted_entry = {
        "id":create_id,
        "description":f"{add_entry}",
        "status":"Todo",
        "createdAt":f"{short_now}",
        "updatedAt":f"{short_now}"
    }

    data["tasks"].append(formatted_entry)

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f'\nTask Added Successfully! ID: {create_id}\nDescription: {add_entry}\nStatus: Todo\nCreated At: {short_now}\nUpdated At: {short_now}\n')

def delete_task(id):

    with open("tasks.json", "r") as file:
        data = json.load(file)

    for task in data["tasks"]:
        if task.get("id") == id:
            data["tasks"].remove(task)
            break
    else:
        print(f"\nNo task found with ID: {id}\n")
        return

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f'\nTask Deleted Successfully! ID: {id}\n')

def update_task(id, new_description):

    with open("tasks.json", "r") as file:
        data = json.load(file)

    try:
        for task in data["tasks"]:
            if task.get("id") == id:
                task["description"] = new_description
                task["updatedAt"] = f"{short_now}"
                break
        else:
            print(f"\nNo task found with ID: {id}\n")
            return

    except Exception as e:
        print(f"Error occurred while updating task: {e}")
        print("Please ensure you have entered a valid task ID and description.\n")
        return

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f'\nTask Updated Successfully! ID: {id}\nDescription: {new_description}\nUpdated At: {short_now}\n')

def mark_task(id, status):

    with open("tasks.json", "r") as file:
        data = json.load(file)

    try:
        for task in data["tasks"]:
            if task.get("id") == id:
                task["status"] = status.capitalize()
                task["updatedAt"] = f"{short_now}"
                break
        else:
            print(f"\nNo task found with ID: {id}\n")
            return

    except Exception as e:
        print(f"Error occurred while marking task: {e}")
        print("\nPlease ensure you have entered a valid task ID and status.\n")
        return

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f'\nTask Marked Successfully! ID: {id}, Status: {status}\n')

def list_tasks():

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

        if not data["tasks"]:
            print("\nNo tasks found. Please add a task first.\n")
            return

        print("\nAll Tasks:")
        for task in data["tasks"]:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
        print("")

    except FileNotFoundError:
        print("\nNo tasks found. Please add a task first.\n")

def list_todo():

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

        todo_tasks = [task for task in data["tasks"] if task["status"].lower() == "todo"]

        if not todo_tasks:
            print("\nNo Todo tasks found. Please add a task first.\n")
            return
        
        print("\nTodo Tasks:")
        for task in todo_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
        print("")

    except FileNotFoundError:
        print("\nNo tasks found. Please add a task first.\n")

def list_in_progress():

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

        in_progress_tasks = [task for task in data["tasks"] if task["status"].lower() == "in-progress"]

        if not in_progress_tasks:
            print("\nNo 'In-Progress' tasks found. Please add a task first.\n")
            return
        
        print("\nIn-Progress Tasks:")
        for task in in_progress_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
        print("")

    except FileNotFoundError:
        print("\nNo tasks found. Please add a task first.\n")

def list_done():

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

        done_tasks = [task for task in data["tasks"] if task["status"].lower() == "done"]

        if not done_tasks:
            print("\nNo Done tasks found.\n")
            return

        print("\nDone Tasks:")
        for task in done_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
        print("")

    except FileNotFoundError:
        print("\nNo tasks found. Please add a task first.\n")

def help_navigate():
    print("\nWelcome to the Task Tracker CLI!\n")
    print("Available commands:")
    print("1. add <description> - Add a new task with the given description.")
    print("2. delete <id1>, <id2>, ... - Delete tasks by their IDs (comma-separated).")
    print("3. update <id>, <new description> - Update the description of a task by its ID.")
    print("4. mark <id>, <status> - Mark a task with a new status (Todo, In-Progress, Done).")
    print("5. list <status> - List tasks by status (Todo, In-Progress, Done) or list all tasks with 'list all'.")
    print("6. exit - Exit the program.\n")

def main():
    while True:
        
        user_input = input('task-cli > ')

        if user_input.lower()[0:3] == 'add':
            if user_input[4:].strip() == "":
                print("\nTask description cannot be empty. Please provide a valid description.\n")
            else:
                add_task(user_input[4:])

        elif user_input.lower()[0:6] == 'delete':
            for id in user_input[7:].split(', '):
                if id.isdigit():
                    delete_task(int(id))
                else:
                    print(f"\nInvalid task ID: {id}. Please enter a valid integer ID.\n")

        elif user_input.lower()[0:6] == 'update':
            try:
                id_str, new_description = user_input[7:].split(', ', 1)
                if id_str.isdigit():
                    update_task(int(id_str), new_description)
                else:
                    print(f"\nInvalid task ID: {id_str}. Please enter an existing or valid integer ID.\n")
            except ValueError:
                print("\nInvalid input format. Please use: update <id>, <new description>\n")

        elif user_input.lower()[0:4] == 'mark':
            try:
                id_str, status = user_input[5:].split(', ', 1)

                if not id_str.isdigit():
                    print(f"\nInvalid task ID: {id_str}. Please enter an existing or valid integer ID.\n")
                    continue

                if status.lower() not in ['todo', 'in-progress', 'done']:
                    print(f"\nInvalid status: {status}. Please enter one of the following: Todo, In-Progress, Done.\n")

                mark_task(int(id_str), status)
            except ValueError:
                print("\nInvalid input format. Please use: mark <id>, <new status>\n")

        elif user_input.lower()[0:4] == 'list':
            try:
                list, status = user_input[0:].split(' ', 1)
                if status.lower() == 'todo':
                    list_todo()
                elif status.lower() == 'in-progress':
                    list_in_progress()
                elif status.lower() == 'done':
                    list_done()
                elif status.lower() == 'all':
                    list_tasks()
                else:
                    print(f"\nInvalid status: {status}. Please enter one of the following: Todo, In-Progress, Done.\n")

            except ValueError:
                print("\nInvalid input format. Please use: list <status> or list all\n")

        elif user_input.lower()[0:8] == 'list todo':
            list_todo()
        elif user_input.lower()[0:11] == 'list in-progress':
            list_in_progress()
        elif user_input.lower()[0:8] == 'list done':
            list_done()

        elif user_input.lower()[0:4] == 'help':
            help_navigate()

        elif user_input.lower()[0:4] == 'exit':
            print('\nExiting the program...\n')
            break
        else:
            print('\nInvalid command.\n')

if __name__ == "__main__":
    main()