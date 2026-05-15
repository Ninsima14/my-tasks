tasks = ["Buy groceries"]

def show_tasks():
    print("\nMy Tasks")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
    print("")


def add_task(name):
    tasks.append(name)
    print(f"Added: {name}")


def delete_task(index):
    done = tasks.pop(index - 1)
    print(f"Removed: {done}")