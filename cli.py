# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print('It is: ', now)

while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}-{item.title()}')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new to-do: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            todo_to_removed = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"To-do {todo_to_removed} was removed from the list"
            print(message)
        except ValueError:
            print("There is an error on the number item")
        except IndexError:
            print("Error in the index")

    elif user_action.startswith('exit'):
        break

    else:
        print("command is not found")

print("Goodbye!!!")
