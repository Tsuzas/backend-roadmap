import os
import sys
import json
from datetime import datetime
from InquirerPy import prompt 

################## FUNCTIONS ################# 
def loadJson(TASK_FILE):
    checkJsonExist(TASK_FILE)
    with open(TASK_FILE) as f:
        tasks = json.load(f)
        return tasks
    
def checkJsonExist(TASK_FILE):
    if not os.path.exists(TASK_FILE):
       with open(TASK_FILE, "x" ) as f:
           f.write('[]')

def saveJson(tasks, TASK_FILE):
    
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks,f, indent=3)

def printTask(task):
    for key, value in task.items():
        print(f"{key}: {value}")   
    print("\n")

def editTask(tasks):
    print("Which task you wish to edit?")
    for task in tasks:
        print(f"{task['id']}: {task['title']} - {task['description']}")
    choice = int(input("->"))
    for task in tasks:
        if task["id"] == choice:

            answer = input("Enter new title (if empty, will stay the same ): ")
            if answer != "":
                task["title"] = answer
            answer = input("Enter new Description (if empty, will stay the same ): ")
            if answer != "":
                task["description"] = answer
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            printTask(task)
            break

def addTask(tasks):
    task = {
        "id": len(tasks) + 1,
        "title": input("Enter a new Title: "),
        "description": input("Enter a description: "),
        "status": "Todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    # Clear the console
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')
    
    printTask(task)
    
    tasks.append(task) 

def listTask(tasks):
    for task in tasks:
        print("------------------------------")
        for key, value in task.items():
            print(f"{key}: {value}")

def deleteTask(tasks):
    print("Which task you wish to delete?")
    for task in tasks:
        print(f"{task['id']}: {task['title']} - {task['description']}")
    choice = int(input("->"))
    for task in tasks:
        if task["id"] == choice:

            tasks.remove(task)
            print("\n--Task deleted!--\n")

            break

def updateTask(tasks):
    print("Which task you wish to edit?")
    for task in tasks:
        print(f"{task['id']}: {task['title']} - {task['description']}")
    choice = int(input("->"))
    for task in tasks:

        if task["id"] == choice :
            questions = [
                {
                    "type": "list",
                    "message": "What's the status of the task?",
                    "choices": ["Todo", "In-progress", "Done", "Abandoned"],
                }
                ]
            answers = prompt(questions)

            task["status"] = answers[0]
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            printTask(task)
            break

def runLoop(choice, tasks, TASK_FILE):
    match choice:
        case '1':
            addTask(tasks)
        case '2':
            listTask(tasks)
        case '3':
            editTask(tasks)
        case '4':
            deleteTask(tasks)
        case '5':
            updateTask(tasks)
        case '9':
            print("-- Bye! --")
            sys.exit()
    saveJson(tasks, TASK_FILE)
        

def main():
    
    TASK_FILE = 'begginer/task-interactiveCLI/tasks.json'
    tasks = loadJson(TASK_FILE)
    
    
    #################### MAIN LOOP ####################

    print("\nWelcome to Task Tracker CLI\n")

    while True:
        choice = input("Please choose an option: \n"
        "1. Add a task\n"
        "2. View tasks\n" 
        "3. Edit Task\n"
        "4. Delete Task\n"
        "5. Update Task\n"
        "9. Exit\n"
        "->")
        
        runLoop(choice, tasks, TASK_FILE)

if __name__ == "__main__":
    main()