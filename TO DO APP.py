#TO DO APP
tasks=[]
total_task=int(input("enter total no. of tasks"))
for i in range(1,total_task+1):
    print("choose operations \n 1 = add tasks \n 2 = update tasks \n 3 = delete tasks \n 4 = view  tasks")
    operation =int(input("enter number"))
    if operation==1:
        task=input("enter task")
        tasks.append(task)
        print("your task has been added")
    elif operation==2:
        old_task=input("enter task you want to update")
        
        if old_task in tasks:
                updated_task=input("enter new task  ")
                index=tasks.index(old_task)
                tasks[index]=updated_task
        else:
            print("task not found")
    elif operation==3:
        task=input("enter task you want to update")   
        if task in tasks:
            tasks.remove(task)
        else:
            print("task not found")
            
    elif operation==4:
        print("total tasks are", tasks)
    else:
        exit


    

