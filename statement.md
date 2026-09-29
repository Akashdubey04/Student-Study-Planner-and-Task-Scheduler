# Statement

## Project title

Student Study Planner & Task Scheduler

## Problem statement

Students usually have many things to do at the same time, like assignments, revision and exam preparation. When everything is only in our head or on random pieces of paper, it is easy to forget a deadline, miss an important task, or not know how much time we actually spend studying each subject.

There should be one simple place where a student can write down all study tasks, see which ones are urgent, and keep track of study time. This project is my attempt to solve that problem.

## Scope of the project

**What the project covers**
- A command-line (terminal) program written in Python
- Adding, viewing, editing, searching, completing and deleting study tasks
- Each task has a title, subject, deadline (`YYYY-MM-DD`) and priority (High / Medium / Low)
- Finding overdue tasks and tasks due in the next 3 days
- Logging study sessions and calculating total study time (overall and per subject)
- Showing statistics and a progress report with a text progress bar
- Checking user input so that wrong values are not accepted

**What the project does not cover**
- Saving data to a file or database. Data is kept in Python lists, so it is lost when the program closes.
- A graphical interface. It works only in the terminal.
- Editing or deleting study sessions after they are logged.
- Multiple users or login. The program is used by one person at a time.

## Target users

- Students (school or college) who want a simple way to plan their study tasks and deadlines
- Anyone who wants to track how many minutes or hours they study for each subject

## High-level features

The program has three main parts (modules):

1. **Task management:** add, edit, delete, search and mark tasks as complete, with input checking for title, subject, date and priority.
2. **Task views:** see all, pending, completed, overdue and upcoming (next 3 days) tasks, sorted by deadline, or grouped by subject.
3. **Study tracking and reports:** log study sessions, see the study log and total time, and view statistics and a full progress report.

All of these are used through one menu with 17 options.
