FILEPATH = "todolist.txt"


def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns the list
    of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes the to-do list to a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)