import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="new_todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.read_file(), 
                      key="todo_list", 
                      enable_events=True, 
                      size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App', 
                   layout=[[label], 
                           [input_box, add_button], 
                           [list_box, edit_button]], 
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print("event, values = window.read()")
    print(f"event = {event}")
    print(f"values = {values}")
    print(f"values[todo_list] = {values['todo_list']}")
    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values["new_todo"]
            todos.append(new_todo)
            functions.write_file(todos)
            window["todo_list"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todo_list"][0]
            new_todo = values["new_todo"]

            todos = functions.read_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            functions.write_file(todos)
            window["todo_list"].update(values=todos)
        case "todo_list":
            window["new_todo"].update(value=values["todo_list"][0])
        case sg.WIN_CLOSED:
            break

window.close()