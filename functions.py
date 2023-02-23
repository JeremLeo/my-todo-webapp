FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Get the list of todos saved in the file"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """Write the list of todos in the save file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)

