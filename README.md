# Student Study Planner & Task Scheduler

A simple command-line program in Python that helps a student keep track of study tasks, deadlines and study time.

I made this project to manage my own study work in one place. You add your tasks, mark them done when you finish, and the program shows what is pending, what is overdue and how much time you have studied.

> **Note:** All data is stored in normal Python lists. Nothing is saved to a file, so when you close the program, everything is gone. That is fine for now.

---

## What it can do

**Task management**
- Add a task with a title, subject, deadline and priority (High / Medium / Low)
- Edit a task (leave a field blank to keep the old value)
- Mark a task as complete
- Delete a task
- Search tasks by keyword (looks in the title and the subject)

**Viewing tasks**
- View all tasks, sorted by deadline
- View only pending tasks
- View only completed tasks
- View overdue tasks (deadline passed and not done)
- View upcoming tasks (due in the next 3 days)
- View tasks grouped by subject

**Study time**
- Log a study session (subject and minutes, the date is added automatically)
- View the full study log
- See total study time, and the total for each subject

**Progress**
- Statistics: total, completed, pending and overdue tasks, and completion rate
- Full report with a text progress bar, breakdown by priority, breakdown by subject and total study time

---

## How to run it

The program only uses the built-in `datetime` module, so you don't need to install anything.

1. Download or clone this repository
2. Open a terminal in the project folder
3. Run:

```
python 1project.py
```

Then choose an option from the menu by typing its number.

---

## Menu

```
========================================
   STUDENT STUDY PLANNER & SCHEDULER
========================================
1. Add Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. View Overdue Tasks
6. View Upcoming Tasks (3 days)
7. View Tasks by Subject
8. Search Tasks
9. Edit Task
10. Mark Task Complete
11. Delete Task
12. Log Study Session
13. View Study Log
14. Total Study Time
15. Statistics
16. Full Report
17. Exit
```

---

## Sample output

Viewing all tasks (option 2):

```
--- All Tasks ---
1. [Pending] Solve worksheet | Subject: Maths | Deadline: 2026-09-25 (OVERDUE) | Priority: High
2. [Pending] Read chapter 3 | Subject: Physics | Deadline: 2026-10-01 | Priority: Medium
3. [Pending] Revise notes | Subject: Maths | Deadline: 2026-11-15 | Priority: Low
```

Full report (option 16):

```
============================================
           STUDY PROGRESS REPORT
============================================

Total Tasks: 3
Completed: 0
Pending: 3
Overdue: 1
Completion: [----------] 0.0%

-- By Priority --
High -> Total: 1 Completed: 0
Medium -> Total: 1 Completed: 0
Low -> Total: 1 Completed: 0

-- By Subject --
Maths -> 0/2 done  [----------] 0.0%
Physics -> 0/1 done  [----------] 0.0%

-- Study Time --
Total sessions: 2
Total time: 1h 15m
============================================
```

---

## Input checking

The program checks what the user types so it doesn't crash on wrong input:
- Title and subject can't be empty
- Deadline must be in `YYYY-MM-DD` format (example: `2026-01-31`)
- Priority must be High, Medium or Low (it doesn't matter if you type it in small letters)
- Minutes studied must be a number
- Task numbers must be valid when choosing a task

---

## How the code is organised

Everything is in one file, `1project.py`. The code is split into small functions, and each menu option has its own function.

| Part | What it does |
|------|--------------|
| `tasks`, `study_log` | Two lists that store all the data. Each task and each study session is a dictionary. |
| `sort_by_deadline()` | Sorts tasks by deadline using bubble sort. |
| `print_task()` | Prints one task in a single line and adds `(OVERDUE)` when needed. |
| `add_task()`, `edit_task()`, `delete_task()`, `complete_task()` | Change the task list. |
| `view_*()` functions | Show tasks in different ways (all, pending, completed, overdue, upcoming, by subject). |
| `log_study()`, `view_study_log()`, `total_study_time()` | Study time tracking. |
| `show_stats()`, `make_bar()`, `show_report()` | Statistics and the progress report. |
| `main()` | Shows the menu and calls the right function in a loop. |

---

## What I practised in this project

- Functions
- Lists and dictionaries
- Loops and if / elif / else
- Taking user input and checking it
- `try` / `except` for wrong date formats
- The `datetime` module (`strptime`, `strftime`, `timedelta`)
- Writing a sorting algorithm myself (bubble sort) instead of using `sort()`
- Making a menu-driven program

---

## Limitations

- Data is not saved, it is lost when the program closes
- Bubble sort is simple but slow for a very large number of tasks
- Study sessions can be added and viewed, but not edited or deleted
- It is only a command-line program, there is no graphical interface

---

## Project files

```
1project.py     the full program
README.md       this file
REPORT.md       the project report
DESCRIPTION.md  short GitHub "About" text
```
