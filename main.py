from functions import read_file, write_file
import time

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        # Load existing items
        todos = read_file()
        todos.append(todo)

        # Load list to a new file
        write_file(todos)

    elif user_action.startswith("show"):
        todos = read_file()
        # remove newline characters from each item
        new_todos = [item.strip('\n') for item in todos]
        # print todos
        for number, item in enumerate(new_todos):
            print(f"{number + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            todos = read_file()

            number = int(user_action[5:])
            number = number - 1

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # Load list to a new file
            write_file(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = read_file()
            number = int(user_action[9:])
            todos.pop(number - 1)
            write_file(todos)
        except IndexError:
            print("That number is out of range. There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        print("bye!")
        break
    else:
        print("Please select add, show, edit, complete or exit")