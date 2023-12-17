def read_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file:
        todos_arg = file.readlines()
    return todos_arg


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
