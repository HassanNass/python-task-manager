def insert(queue, task):
    queue.append(task)

queue = []

num_of_tasks = int(input("How many tasks do you want to add?: "))

for i in range(num_of_tasks):
    print(f"\nTask {i+1}:")
    title = input("Enter task title: ")
    duration = int(input("Enter the duration of the task in minutes: "))
    priority = int(input("Enter priority number (The lower the number, the higher the priority): "))
    
    task = {
        "title": title,
        "duration": duration,
        "priority": priority
    }
    
    insert(queue, task)
    
