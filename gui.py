import functions
import FreeSimpleGUI as sg
import time

sg.theme("DefaultNoMoreNagging")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="new_todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.read_file(), key="todo_list", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete", key="complete_button")
exit_button = sg.Button("Exit", key="exit_button")

layout = [[clock],
          [label], 
          [input_box, add_button], 
          [list_box, edit_button, complete_button], 
          [exit_button]]

window = sg.Window('My To-Do App', 
                   layout=layout, 
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print("event, values = window.read()")
    # print(f"event = {event}")
    # print(f"values = {values}")
    # print(f"values[todo_list] = {values['todo_list']}")
    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values["new_todo"]
            todos.append(new_todo)
            functions.write_file(todos)
            window["todo_list"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todo_list"][0]
                new_todo = values["new_todo"]
                todos = functions.read_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_file(todos)
                window["todo_list"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "todo_list":
            window["new_todo"].update(value=values["todo_list"][0])
        case "complete_button":
            try:
                todos = functions.read_file()
                todo_to_complete = values["todo_list"][0]
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.write_file(todos)
                window["todo_list"].update(values=todos)
                window["new_todo"].update(value="")
            except:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "exit_button":
            break
        case sg.WIN_CLOSED:
            break

window.close()