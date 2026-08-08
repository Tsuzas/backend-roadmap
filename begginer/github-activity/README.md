# Git Hub activity tracker CLI

A simple interactive command-line Github activity tracker built with Python.

This project allows you to easily check the most recent activity of any public account.

## Features

- Checks pushes and repos created

## Requirements
- requests


## Project Structure

```
github-activity/
│
├── main.py
├── README.md
```

## Running the Project

Run the program with:

```bash
python main.py <username>
```

or

```bash
python3 main.py <username>
```

## Activity Format

Activity is showed in plain text

Example:

```
-Tsuzas
        -pushed 8 times, between 2026-07-09T21:55:33Z and 2026-08-05T18:04:06Z
        -created Tsuzas/backend-roadmap on 2026-07-09T21:51:22Z
```

## Technologies

- Python
- requests
- datetime
- sys

## Notes

This project was made as practice while following the Backend Roadmap from roadmap.sh and focuses on learning:

- Command-line arguments via sys.agrv
- JSON handling
- Error handling
- API usage
- Basic CLI application design
