import json
from datetime import datetime
import os
from InquirerPy import prompt 

################## FUNCTIONS ################# 
def loadJson():
    checkJsonExist()
    with open('begginer/task-interactiveCLI/tasks.json') as f:
        tasks = json.load(f)
        return tasks
    
def checkJsonExist():
    if not os.path.exists('begginer/task-interactiveCLI/tasks.json'):
       with open('begginer/task-interactiveCLI/tasks.json', "x" ) as f:
           f.write('[]')

def saveJson(tasks):
    
    with open('begginer/task-interactiveCLI/tasks.json', 'w') as f:
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
            saveJson(tasks)
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

    saveJson(tasks)    

def listTask(tasks):
    for task in tasks:
        print("------------------------------")
        for key, value in task.items():
            print(f"{key}: {value}")

def deleteTask(tasks):
    print("Which task you wish to delete?")
    print("RAW Tasks:", tasks)
    for task in tasks:
        print(f"{task['id']}: {task['title']} - {task['description']}")
    choice = int(input("->"))
    for task in tasks:
        if task["id"] == choice:

            tasks.pop(choice - 1)
            saveJson(tasks)

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
                    "choices": ["Pending", "Doing", "Done", "Abandoned"],
                }
                ]
            answers = prompt(questions)

            task["status"] = answers[0]
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            printTask(task)
            saveJson(tasks)
            break

def runLoop(choice, tasks):
     
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
            print("Bye.")
            return

def main():

    #################### MAIN LOOP ####################
    tasks = loadJson()

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
        
        runLoop(choice, tasks)

if __name__ == "__main__":
    main()