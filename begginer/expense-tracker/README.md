# Expense Tracker CLI

A simple interactive command-line expense tracker built with Python.

This project allows you to easily add, remove, and see all expenses present in json.

## Features

- Adds expense with Id, description, amount and date created 
- Delete expense with Id

## Requirements
- None, all present withi Python library


## Project Structure

```
expense-tracker/
│
├── main.py
├── expenses.json
├── README.md
```

## Running the Project

Run the program with:

```bash
python main.py add --decription <decription> --amount <amount>
```

or

```bash
python3 main.py add --decription <decription> --amount <amount>
```

## Summary Format

Run the program with :

```bash
python3 main.py summary
```
or in case you specify month with the addition of --month <month>

Summary is showed in plain text

Example:

```
Total Spent: 1501.49€
```
## Delete expense

Run the program with:

```bash
python3 main.py delete <id>
```
Nothing will show but the whole task will disappear and the Id's will be readjusted with that in mind, so no gaps are created.
Expense IDs start at 1, while Python arrays start at index 0. The delete command takes this into account by using "id - 1" to access the correct expense.


## Technologies

- Python

## Notes

This project was made as practice while following the Backend Roadmap from roadmap.sh and focuses on learning:

- Command-line arguments via agrparse
- JSON handling
- Error handling
- Basic CLI application design
