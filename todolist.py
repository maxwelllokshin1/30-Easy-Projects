import time

tasks = []

def menu():
    print("===== TO-DO =====")
    print("1. View Tasks" \
        "\n2. Add Task" \
        "\n3. Completed Task" \
        "\n4. Remove Task" \
        "\n5. Quit")

def view():
    if not tasks:
        print("=================")
        print("EMPTY tasks")
        return True
    else:
        print("===== Tasks =====")
        for index, task in enumerate(tasks, 1):
            status = "✓" if task["Status"] else "✗"
            print(f"{index}. [{status}] {task['Title']}")

def add():
    print("=================")
    task = input("Task: ")
    tasks.append({"Title": task, "Status": False})
    print("Added")

def comp():
    if view(): return
    task = input("Task completed: ")
    if task.isdigit():
        task = int(task) - 1
        if 0 <= task < len(tasks):
            tasks[task]['Status'] = True
        else:
            print("INVALID")
    else:
        check, index = inTasks(task)
        if check:
            tasks[index]['Status'] = True
            print(f"Completed: [{tasks[index]['Title']}]")
        else:
            print("INVALID")
        

def remove():
    if view(): return
    task = input("Task to remove: ")
    if task.isdigit():
        task = int(task) - 1
        if 0 <= task < len(tasks):
            removed = tasks.pop(task)
            print(f"Removed: {removed['Title']}")
        else:
            print("INVALID")
    else:
        check, index = inTasks(task)
        if check:
            removed = tasks.pop(index)
            print(f"Removed: {removed['Title']}")
        else:
            print("INVALID")

def inTasks(task):
    for index, item in enumerate(tasks):
        if item["Title"].lower() == task.lower():
            return True, index
    return False, -1

def main():
    while True:
        menu()
        user = input("Choice: ").lower()

        if user in ("1", "1.", "view tasks", "view"):
            view()
        elif user in ("2", "2.", "add task", "add"):
            add()
        elif user in ("3", "3.", "completed tasks", "completed", "complete"):
            comp()
        elif user in ("4", "4.", "remove task", "remove"):
            remove()
        elif user in ("5", "5.", "quit"):
            break
        else:
            print("INVALID")
        print("=================")
        time.sleep(1)

if __name__ == "__main__":
    main()