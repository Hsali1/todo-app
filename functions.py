FILEPATH = "todos.txt"

def read_file(filepath=FILEPATH):
    """ Reads a text file and return list of to-do items. """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_file(todo_list, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todo_list)
# some random stuff