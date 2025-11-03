FILEPATH = "todos.txt"

def read_file(filepath=FILEPATH):
    try:
        with open(filepath, 'r') as file:
            # remove the trailing newline for clean display
            return [line.strip('\n') for line in file.readlines()]
    except FileNotFoundError:
        return []

def write_file(todo_list, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        # re-add newline for each todo before writing
        file.writelines(f"{todo}\n" for todo in todo_list)

        