def read_file(filepath = "todos.txt"):
    """ Reads a text file and return list of to-do items. """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_file(todo_list):
    """ Write the to-do items list in the text file """
    with open("todos.txt", 'w') as file:
        file.writelines(todo_list)
