import os

task_file=os.path.join(os.path.dirname(__file__),'tasks.txt')

def load_task():
    tasks = {}
    if (os.path.exists(task_file)):
        with open(task_file,'r',encoding='utf-8') as f:
            for i in f:
                task,status = i.strip().rsplit("||",1)
                # tasks.append({
                #     task:task,'status':'completed'==status.lower()
                # })
                tasks[task.strip()]=status.strip().lower()=='completed'
    return tasks

def save_tasks(tasks:dict):
    with open(task_file,'w',encoding='utf-8') as file:
        for task,status in tasks.items():
            file.write(f"{task} || {"completed" if status else "not completed"}")



def change_status(tasks:dict,text:str,new_status:bool):
    if text in tasks:
        tasks[text]=new_status
        save_tasks(tasks)
    return tasks

def delete_task(tasks:dict,text:str):
    if text in tasks:
        del tasks[text]
        save_tasks(tasks)
    return tasks

def add_task(tasks:dict,text:str):
    tasks[text]=False
    save_tasks(tasks)
    return tasks


def task_manager():
    tasks:dict= load_task()
    while True:
        print(f"1. Add a task")
        print(f"2. View All task")
        print(f"3. Change task status")
        print(f"4. Delete a task")
        print("5. Exit")

        selected_option=0
        try:
            selected_option = int(input("Enter selected number : "))
        except Exception as e:
            print("Please enter correct inpurt")
            continue
        match selected_option:
            case 5:
                break
            case 1:
                text=input("Enter task name : ")
                add_task(tasks,text)
                print("Updated the tasks ")
                continue
            case 2:
                if len(tasks)>0:
                    print('-'*50)
                    for index,(text,status) in enumerate(tasks.items()):
                        print(f"{index} {text} | {status} {"✅" if status else "❌"}")
                        continue
                    print('-'*50)
                else:
                    print('-'*50)
                    print("No task Found Try adding one")
                    print('-'*50)
                    continue
            case 3:
                text=input("Enter task name : ")
                if text in tasks:
                    status:bool=tasks[text]
                    change_status(tasks=tasks,text=text,new_status=not status)
                    print("Updated the tasks ")
                    continue
            case 4:
                print('-'*50)
                for index,(text,status) in enumerate(tasks.items()):
                    print(f"{index} {text} | {status} {"✅" if status else "❌"}")
                    continue
                print('-'*50)
                text=input("Enter task name : ")
                while text in tasks:
                    delete_task(tasks,text)
                    print("Updated the tasks ")
                    continue
                else:
                    print("Incorrect Option!")
                    continue
            case _:
                continue

task_manager()