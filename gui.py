import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('BlueMono')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a task")

# when the button is pushed, an event is created and a tuple is returned
# the key argument on the input box is the first value of the tuple (event)
# and the text input by the user is the second value of the tuple (value)

input_box = sg.InputText(tooltip="Enter a task", key="task")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(values=functions.open_file(), key='tasks',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

window = sg.Window('Things I need to do',
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S") )

# here we're checking which event (button) was pushed
# also note, we'd normally use a "match/case" statement here
# but we had to use python 3.9 to get PySimpleGUI to work and
# 3.9 does not have match/case available
    
    if event == 'Add':
        tasks = functions.open_file()
        new_task = values['task'] + "\n"

        tasks.append(new_task)
        functions.write_file(tasks)
        window['tasks'].update(values=tasks)

    elif event == 'Edit':
        try:
            task_to_edit = values['tasks'][0]
            new_task = values['task']
            tasks = functions.open_file()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            functions.write_file(tasks)
            window['tasks'].update(values=tasks)
        except IndexError:
            sg.popup('Please select a task to edit from the list', font=('Helvetica', 20))

    elif event == 'Complete':
        try:
            task_to_complete = values['tasks'][0]
            tasks = functions.open_file()
            tasks.remove(task_to_complete)
            functions.write_file(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value='')
        except IndexError:
            sg.popup('Please select a task to complete from the list', font=('Helvetica', 20))

    elif event == 'Exit':
        break;

    elif event == 'tasks':
        window['task'].update(value=values['tasks'][0])

    elif event == sg.WIN_CLOSED:
        break;


window.close()

