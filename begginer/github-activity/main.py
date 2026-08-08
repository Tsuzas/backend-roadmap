import sys
import requests
from datetime import datetime, date

if len(sys.argv) != 2:
    print("Usage: python3 main.py <username>")
    exit(1)

# VARIABLES
username = sys.argv[1]
pushflag = 0
createflag = 0
events = []
print(f"Fetching activity for {username}")  

response = requests.get(f"https://api.github.com/users/{username}/events")


if(response.status_code == 200):
    information = response.json()
    for event in information:

        # LOOPING THROUGH EVENTS AND CHECKING FOR PUSH OR CREATE EVENTS AND ASSIGNING DATES AND REPOS ACCORDINGLY
        if ({event['type']} == {'PushEvent'}):
            pushflag += 1
            if (pushflag == 1):
                initialDatePush = event['created_at']
            latestDatePush = event['created_at']
        elif ({event['type']} == {'CreateEvent'}):
            createflag += 1
            events.append(event['repo']['name'])
            if (createflag == 1):
                initialDateCreate = event['created_at']
            latestDateCreate = event['created_at']

    print(f" -{username}")

    # IN CASE SINGLE PUSH INDIVIDUAL PRINT
    if (pushflag == 1):
        print(f"\t-pushed on {information[0]['repo']['name']} on {initialDatePush}")
    elif(pushflag > 1):
        print(f"\t-pushed {pushflag} times, between {latestDatePush} and {initialDatePush}")

    # IN CASE SINGLE CREATE INDIVIDUAL PRINT
    if (createflag == 1):
        print(f"\t-created {information[0]['repo']['name']} on {initialDateCreate}")
    elif(createflag > 1):
        print(f"\t-created a multiples repos such as {events} between {latestDateCreate} and {initialDateCreate}")

    # IN CASE NO ACTIVITY OR PRIVATE ACCOUNT
    if (pushflag == 0 and createflag == 0):
        print(f"{username} has no recent activity or might be private.")

else: print(f"Error fetching information for {username}")


