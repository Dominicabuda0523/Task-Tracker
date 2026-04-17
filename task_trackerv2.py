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
        print(f'Task Added Successfully! ID: {create_id}')

def delete_task(id):

    with open("tasks.json", "r") as file:
        data = json.load(file)

    try:
        data["tasks"] = [d for d in data["tasks"] if d.get("id") !=id]
    except Exception as e:
        print(f"Error occurred while deleting task: {e}")
        print("Please ensure you have entered a valid task ID only.")
        return

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f'Task Deleted Successfully! ID: {id}')

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
            print(f"No task found with ID: {id}")
            return

    except Exception as e:
        print(f"Error occurred while updating task: {e}")
        print("Please ensure you have entered a valid task ID and description.")
        return

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f'Task Updated Successfully! ID: {id}')

while True:
    user_input = input('task-cli > ')

    if user_input.lower()[0:3] == 'add':
        add_task(user_input[4:])

    elif user_input.lower()[0:6] == 'delete':
        for id in user_input[7:].split(', '):
            if id.isdigit():
                delete_task(int(id))
            else:
                print(f"Invalid task ID: {id}. Please enter a valid integer ID.")

    elif user_input.lower()[0:6] == 'update':
        try:
            id_str, new_description = user_input[7:].split(', ', 1)
            if id_str.isdigit():
                update_task(int(id_str), new_description)
            else:
                print(f"Invalid task ID: {id_str}. Please enter an existing or valid integer ID.")
        except ValueError:
            print("Invalid input format. Please use: update <id>, <new description>")

    elif user_input.lower()[0:6] == 'update':
        from task_trackerv2 import update_task
        update_task()   
    elif user_input.lower()[0:4] == 'exit':
        print('Exiting the program...')
        break
    else:
        print('Invalid command.')
