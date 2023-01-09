FILEPATH = "files/tasks.txt"

def open_file():
    with open(FILEPATH, 'r') as file:
        tasks = file.readlines()

    return tasks


def write_file(tasks):
    with open(FILEPATH, 'w') as file:
        file.writelines(tasks)


def show_tasks():
    tasks = open_file()

    if len(tasks) == 0:
        print("You have nothing to do today, go outside and play!!")
    else:
        i = 1
        for task in tasks:
            print(str(i) + '. ' + task.strip('\n'))
            i += 1
