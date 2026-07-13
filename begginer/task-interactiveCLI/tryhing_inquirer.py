from InquirerPy import prompt

questions = [
    {"type": "input", "message": "What's your name:", "name": "name"},
    {
        "type": "list",
        "message": "What's your favourite programming language:",
        "choices": ["Go", "Python", "Rust", "JavaScript"],
    },
    {"type": "confirm", "message": "Confirm?"},
]
result = prompt(questions)
print(result)
name = result["name"]
print(name)
fav_lang = result[1]
print(fav_lang)
confirm = result[2]
print(confirm)