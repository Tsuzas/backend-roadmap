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
            if data != None:
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
summary_parser.add_argument("--month" ,help = "For a more in depth analys of summary.", type = int)

# Delete subparser, deletes certain grocery
delete_parser = subparsers.add_parser('delete', help ="Remove a certain expense, usage:. python <program> delete [number]")
delete_parser.add_argument("id", type = int)


#No idea what this does either
args = parser.parse_args()

if (args.command) == "list":
    print(f"{"ID":<8}{"Date":<16}{"Description":<20}Amount")
    for expense in expenses:
        print(f"{expense["id"]:<8}{expense["date"][0:10]:<16}{expense["description"]:<20}{expense["amount"]}")
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

    # Initializes Total for calculations
    total = 0

    # If month argument is not used it will always return None, so using if not null is a good way to use in case theres a month to check first

    if (args.month)!= None:
        print(args.month)
        for expense in expenses:
            if expense["date"][5:7] == args.month or expense["date"][5:7] == "0" + str(args.month):
                total += expense["amount"]
        print(f"\nTotal Spent: {round(total,2)}€\n")

        # Exits early to avoid the general summary
        exit()

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spent: {round(total,2)}€\n")

elif (args.command) == "delete":
    print(f"working? {args.command} and {args.id}")

    # Data as None so n Save expenses it can fail check and proceed
    data = None

    #Remove dic associated with ID
    del expenses[args.id - 1]
    for i, expense in enumerate(expenses, start=1):
        expense["id"] = i
    saveExpense(data, expenses)

# TODO 
# XXX DYNAMIZE ID,
# XXX FIX OVERWRITE FOMR SAVEFUNCTUION
# XXX SUMMARY, 
# XXX SUMMARY MONTH SPECIFIC, 
# XXX DELETE ID,
# XXX REFINE PRINT LIST,
# ERROR HANDLE IMPROPER COMMANDS,
# MODULARISE WITH FUNCTIONS, SAME FILE THO I AINT CREAITNG MORE FILES FOR THIS SIZE, NVM JUST CHEKCED THIS IS GETTING KIND ABIG 
