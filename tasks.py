tasks = []
 
def show_tasks():
    print("\n My Tasks")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
        print("")

        #Adding a line to the tasks.py

    tasks=["Buy groceries"] #edit this line

    def add_task(name):
        tasks.append(name)
        print(f"Added: {name}")

def delete_task(index):
    done = tasks.pop(index - 1)
    print(f"Removed: {done}")