from functions import open_file, write_file, show_tasks
import time

print("*** Welcome to your to-do list ***")
print("*** Today is " + time.strftime("%b %d, %Y %H:%M:%S") + " ***")

while True:

    show_tasks()

    user_action = input("What would you like to do? Please type add, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        task = user_action[4:] + "\n"

        tasks = open_file()
        tasks.append(task)

        write_file(tasks)

    elif user_action.startswith('edit'):
        try:
            tasks = open_file()

            task_number = int(user_action[5:])
            print(tasks[task_number - 1])
            new_task = input("Enter a new task: ") + "\n"
            tasks[task_number - 1] = new_task

            write_file(tasks)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("That item does not exist")
            continue

    elif user_action.startswith('complete'):
        try:
            tasks = open_file()

            show_tasks()

            task_number = int(user_action[9:])
            task = tasks[task_number - 1]
            tasks.pop(task_number - 1)
            print('Congratulations on finishing ' + task)

            write_file(tasks)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("That item does not exist")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
        

print("Bye!")
