import json
from datetime import datetime

short_now = datetime.now().replace(second=0, microsecond=0)

# For Add Task Feature
def add_to_json(entry):
    with open("tasks.json", "r") as file:
        data = json.load(file)

    data["tasks"].append(entry)

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
        print('Task Added Successfully!')

def add_task():

    user_description = input('Add Task: ')

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

    new_entry = {
        "id":create_id,
        "description":f"{user_description}",
        "status":"Todo",
        "createdAt":f"{short_now}",
        "updatedAt":f"{short_now}"
    }

    return add_to_json(new_entry)

# For delete task feature

def delete_task():

    with open("tasks.json", "r") as file:
        data = json.load(file)

    print("Tasks")
    for items in data["tasks"]:
        print(f"ID: {items["id"]} | Description: {items["description"]} | Status: {items["status"]} | Created at: {items["createdAt"]} | Updated At: {items["updatedAt"]}")

    user_delete = int(input('Please input the ID of the task you wanted to delete: '))
    data["tasks"] = [d for d in data["tasks"] if d.get("id") !=user_delete]

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
    print('Task Deleted Successfully!')

def update_task():

    with open("tasks.json", "r") as file:
        data = json.load(file)

    print("Tasks")
    for items in data["tasks"]:
        print(f"ID: {items["id"]} | Description: {items["description"]} | Status: {items["status"]} | Created at: {items["createdAt"]} | Updated At: {items["updatedAt"]}")
    print('')

    update_status = int(input("Input the ID of the task to Update: "))

    with open("tasks.json", "r") as file:
        data = json.load(file)
        
        print("\nSelected Task: ")
        for item in data["tasks"]:
            if update_status == item["id"]:
                print(f"ID: {item["id"]} | Description: {item["description"]} | Status: {item["status"]} | Created at: {item["createdAt"]} | Updated At: {item["updatedAt"]}")
        print('')

        while True:

            change_status = input("Change into (Done)(In-Progress)(Todo): ")

            


            if change_status.lower() == 'done':
                for item in data["tasks"]:
                    if update_status == item["id"]:
                        item["status"] = 'Done'
                        item["updatedAt"] = f'{short_now}'
                break
                

            elif change_status.lower() == 'in-progress':
                for item in data["tasks"]:
                    if update_status == item["id"]:
                        item["status"] = 'In-Progress'
                        item["updatedAt"] = f'{short_now}'
                break

            elif change_status.lower() == 'todo':
                for item in data["tasks"]:
                    if update_status == item["id"]:
                        item["status"] = 'Todo'
                        item["updatedAt"] = f'{short_now}'
                break

            else:
                print('Invalid Input.')
        
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)


# List tasks
def user_list_tasks():
    user_list = input('\nList done | List Todo | List In-progress | Go Back : ')

    while True:
        if user_list.lower() == 'list done':
            return list_done()
        elif user_list.lower() == 'list todo':
            return list_todo()
        elif user_list.lower() == 'list in-progress':
            return list_in_progress()
        elif user_list.lower() == 'go back':
            return
        else:
            print('Invalid Input')

def list_done():
    with open("tasks.json", "r") as file:
        data = json.load(file)
        
        print('\nDone Tasks: ')
        for items in data["tasks"]:
            if items["status"] == 'Done':
                print(f"ID: {items["id"]} | Description: {items["description"]} | Status: {items["status"]} | Created at: {items["createdAt"]} | Updated At: {items["updatedAt"]}")
            else:
                print("No 'Done' tasks is found.")
    
    return user_list_tasks()

def list_todo():
    with open("tasks.json", "r") as file:
        data = json.load(file)
        
        print('\nTodo Tasks: ')
        for items in data["tasks"]:
            if items["status"] == 'Todo':
                print(f"ID: {items["id"]} | Description: {items["description"]} | Status: {items["status"]} | Created at: {items["createdAt"]} | Updated At: {items["updatedAt"]}")
            else:
                print("No 'Todo' tasks is found.")
    
    return user_list_tasks()

def list_in_progress():
    with open("tasks.json", "r") as file:
        data = json.load(file)
        
        print('\nIn-Progress Tasks: ')
        for items in data["tasks"]:
            if items["status"] == 'In-Progress':
                print(f"ID: {items["id"]} | Description: {items["description"]} | Status: {items["status"]} | Created at: {items["createdAt"]} | Updated At: {items["updatedAt"]}")
            else:
                print("No 'In-Progress' tasks is found.")
    
    return user_list_tasks()
        

def list_tasks():

    with open("tasks.json", "r") as file:
        data = json.load(file)

        print('Listed Tasks: ')
        for items in data["tasks"]:
            print(f"ID: {items["id"]} | Description: {items["description"]} | Status: {items["status"]} | Created at: {items["createdAt"]} | Updated At: {items["updatedAt"]}")

    return user_list_tasks()


def interface():
    print("\n==================")
    print("   TASK TRACKER   ")
    print("==================")
    print('')
    print("1.) See List")
    print("2.) Add Task")
    print("3.) Delete Task")
    print("4.) Update Task")
    print("5.) Quit")
    
while True:
    interface()
    try:
        user_select = int(input('\nSelect an option: '))
        print('')
    except ValueError:
        print('\nInvalid Input')
        continue

    if user_select == 1:
        list_tasks()
    elif user_select == 2:
        add_task()
    elif user_select == 3:
        delete_task()
    elif user_select == 4:
        update_task()
    elif user_select == 5:
        print("Goodbye!")
        break
    else:
        print('\nInvalid Input')