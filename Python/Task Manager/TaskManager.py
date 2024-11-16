'''
Create a List - Store a list of tasks
'''
tasks  = []

# Add tasks
def add_task(title, description, priority = 'low',deadline = None):
    task = {
        'Title' : title,
        'Description' : description,
        'Priority' : priority,
        'Deadline' : deadline,
        'Status' : 'Pending'
    }
    tasks.append(task)
    
# Print Tasks
def list_task():
    if not tasks: #Empty  = True
        print('No tasks available')
    else:
        for i,task in enumerate(tasks,start=1):
            print(f'{task['Title']} - {task['Priority']}')

#Delete Task
# def delete_task(title):
#     for task in tasks:
#         if task['Title'] == title:
#             tasks.remove(task)
#             print(f'Task {title} deleted')

def delete_task(task_index):
    if task_index < 0 or task_index >= len(tasks):
        print('Invalid task index')
        return
    else:
        removed = tasks.pop(task_index)
        print(f'Task {removed["Title"]} deleted')

def change_status(task_index):
    if task_index < 0 or task_index >= len(tasks):
        print('Invalid task index')
        return
    else:
        if tasks[task_index]['Status'] == 'Pending':
            tasks[task_index]['Status'] = "Completed"
        elif tasks[task_index]['Status'] == 'Completed':
            tasks[task_index]['Status'] = "Pending"

# Filter by priority
def filter_by_priority(priority_level):
    # L1 = [task for task in tasks if task['Priority'] == priority_level.title()]
    # print(L1)
    new = list(filter(lambda task:task['Priority']==priority_level,tasks))
    print(new)
    
# Filter  by Date
def filter_by_date():
    pass
add_task('Give lab list','Number of students','High','2024-11-13')
add_task('Give lab list','Number of students','Low','2024-11-13')
list_task()
change_status(0)
filter_by_priority("High")