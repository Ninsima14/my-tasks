tasks = []
 
def show_tasks():
    print("\n My Tasks")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
        print("")

        #Adding a line to the tasks.py

    tasks=["Buy groceries"] #edit this line
    
   #Next line is for delete-tasks branch
def delete_task(index):
    done= tasks.pop(index-1)
    print(f"Removed task: {done}")
