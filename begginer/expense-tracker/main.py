import argparse
import json 
import datetime

def loadExpense():
    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print("\nJson was not found, creating a new one...\n")
        with open("expenses.json", "w")as file:
            data = []
            file.write(json.dumps(data, indent=4))
        
    except FileExistsError:
        print("\nSomething went wrong reading the Json.\n")

def saveExpense(data, expenses):
    try:
        with open("expenses.json", "w") as file:
            expenses.append(data)
            json.dump(expenses, file, indent = 4)

    except FileNotFoundError:
        print("Json was not found. Command canceled.")
        
    except FileExistsError:
        print("Something went wrong reading the Json.")

expenses = loadExpense()

# No idea what this does
parser = argparse.ArgumentParser()

# Adds arguments to the parser like:



#Adds subparsers for stuff like list and summary which will be added later on
subparsers = parser.add_subparsers(dest = "command")

#Add subparser, can be further enhanced with description and amount for further details on expense list
add_parser = subparsers.add_parser("add" , help = "Add any expense to the list use argument --description and amount for further details")
#Description so user knows what the expense is for
add_parser.add_argument("--description" ,help = "Descriptions of expense")
#Amount so user knows how much the expense is
add_parser.add_argument("--amount" ,help = "Amount of expense", type = float)

# List SubParser, shows entire list for us er 
list_parser = subparsers.add_parser('list' ,help='Shows whole list of expenses')

# Summarty subparser, shows summary of spendage
summary_parser = subparsers.add_parser('summary' ,help = "Shows the spendage across all months, use --month Y, for further details.")
summary_parser.add_argument("--month" ,help = "For a more in depth analys of summary.")

#No idea what this does either
args = parser.parse_args()

if (args.command) == "list":
    print(expenses)
elif (args.command) == "add":
    # Prints for debugging
    print(args.description)
    print(args.amount)

    # Add it into a json with ID, description, amount, and date
    data = {
            "id": len(expenses) +1,
            "description": args.description,
            "amount": args.amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    saveExpense(data, expenses)
elif (args.command) == "summary":
    total = 0
    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spent: {total}€\n")

# TODO 
# XXX DYNAMIZE ID,
# XXX FIX OVERWRITE FOMR SAVEFUNCTUION
# XXX SUMMARY, 
# SUMMARY MONTH SPECIFIC, 
# DELETE ID,
# REFINE PRINT LIST,
# ERROR HANDLE IMPROPER COMMANDS,
# MODULARISE WITH FUNCTIONS, SAME FILE THO I AINT CREAITNG MORE FILES FOR THIS SIZE, NVM JUST CHEKCED THIS IS GETTING KIND ABIG 
