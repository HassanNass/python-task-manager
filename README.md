# Python Task Manager

A command-line task management application built in Python, implementing a **priority queue** from scratch without relying on built-in sorting or search libraries.

---

## Features

- Add multiple tasks with a title, duration, and priority number
- Extract the highest-priority task from the queue
- Peek at the top of the queue without removing it
- Complete the next task based on priority
- Search for a task by title using **binary search**
- Sort tasks by title using **selection sort**
- Sort tasks by duration using **selection sort**

---

## How Priority Works

The lower the priority number, the higher the priority.
For example, a task with priority `1` will be completed before a task with priority `3`.

---

## Data Structures & Algorithms

This project was built as a learning exercise to practice implementing core concepts manually:

| Concept | Implementation |
|---|---|
| Queue | Custom queue using a Python list with `append` and `pop(0)` |
| Priority Extraction | Linear scan to find the minimum priority value |
| Binary Search | Used to search tasks by title after sorting |
| Selection Sort | Used twice — sorting by title and by duration |

---

## How to Run

Make sure you have Python 3 installed.

```bash
python task_manager.py
```

You will be prompted to:
1. Enter the number of tasks you want to add
2. Fill in the title, duration (in minutes), and priority number for each task
3. Search for a specific task by title

---

## Example

```
How many tasks do you want to add?: 3

Task 1:
Enter task title: Fix bug
Enter the duration of the task in minutes: 30
Enter priority number (The lower the number, the higher the priority): 2

Task 2:
Enter task title: Write tests
Enter the duration of the task in minutes: 60
Enter priority number (The lower the number, the higher the priority): 1

Task 3:
Enter task title: Update docs
Enter the duration of the task in minutes: 20
Enter priority number (The lower the number, the higher the priority): 3

The Highest Priority Task:
Title   : Write tests
Duration: 60
Priority: 1
```

---

## What I Learned

- How queues work and how to implement queue operations (enqueue, dequeue, peek)
- How to implement selection sort and understand its time complexity O(n²)
- How binary search works and why the list must be sorted first
- Structuring a CLI program with multiple functions in Python

---

## Author

**Hassan Nasrallah**
[github.com/HassanNass](https://github.com/HassanNass)
