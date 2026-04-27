tasks = []
 
def show_tasks():
    print("\n My Tasks")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
        print("")
        
