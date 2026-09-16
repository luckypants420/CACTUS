import datetime

def add_task():
    id = input("what is the id of the task?").lower()
    description = input("what is the task description").lower()
    while True:
        status = input("whats the status of the task").lower()
        if status in ("pending", "done"):
            break
        print("invalid input for the status, it can either be done or pending")
    
    task = {
        "id": id,
        "description": description,
        "status": status,
        "createdAt": datetime.datetime.now(),
    }
    return task

def show_tasks(tasks_list):
    for i, task in enumerate(tasks_list):
        print(i + 1, "- id", task["id"], "|", task["description"],"| status: ", task["status"], "|")






tasks_list = [{
    "id": 1,
    "description": "Complete the project documentation",
    "status": "pending",
    "createdAt": datetime.datetime.now(),
    "updatedAt": datetime.datetime.now(),
}]


print()
print("Welcome to your to do list!")
print()

while True:
    command = input("Would you like to Add, Delete, show, or mark a task? (type q to quit)").lower()
    if(command == "add"):
        new_task = add_task()
        tasks_list.append(new_task)
        print("new task added")
        show_tasks(tasks_list)
    elif(command == "delete"):
        pass
    elif(command == "mark"):
        pass
    elif(command == "show"):
        show_tasks(tasks_list)
    elif(command == "q"):
        print("exited program!")
        break