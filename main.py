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
    
print("\nThe tasks that added to the queue:")
for task in queue:
    print(task)
    
def extract(queue):
    if len(queue) == 0:
        return None
    else:
        return queue.pop(0)
    
def peek(queue):
    if len(queue) == 0:
        return None
    else:
        return queue[0]

def is_empty(queue):
    return len(queue) == 0

print("\nPeek:", peek(queue))
print("Is queue empty?", is_empty(queue))

task = extract(queue)
print("Extracted task:", task)
print("Queue after extract:", queue)

def complete_next_task(queue):
    if len(queue) == 0:
        print("There isn't any tasks.")
        return
    else:
        index = 0
        p = queue[0]["priority"]
        for i in range(len(queue)):
            if queue[i]["priority"] < p:
                p = queue[i]["priority"]
                index = i

        task = queue.pop(index)
        print("\nThe Highest Priority Task:")
        print(f"Title   : {task['title']}")
        print(f"Duration: {task['duration']}")
        print(f"Priority: {task['priority']}")

complete_next_task(queue)

def sort_by_title(queue):
    sorted_queue = queue[:]
    n = len(sorted_queue)
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            if sorted_queue[j]["title"].lower() < sorted_queue[min_i]["title"].lower():
                min_i = j
        sorted_queue[i], sorted_queue[min_i] = sorted_queue[min_i], sorted_queue[i]
    return sorted_queue


def search_for_task(queue, title):
    sorted_queue = sort_by_title(queue)
    
    start = 0
    end = len(sorted_queue) - 1
    
    while start <= end:
        mid = (start + end) // 2
        mid_title = sorted_queue[mid]["title"].lower()
        
        if mid_title == title.lower():
            return sorted_queue[mid]
        elif mid_title < title.lower():
            start = mid + 1
        else:
            end = mid - 1
    return None

title_search = input("Enter the title of the task you want to search for: ")
search = search_for_task(queue, title_search)

if search:
    print(f"Task found: {search}")
else:
    print("Task not found.")
    
