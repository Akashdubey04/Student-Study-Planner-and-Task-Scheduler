# Student Study Planner and Task Scheduler
# I made this project to manage my study tasks and track study time.
# Everything is stored in a normal python list, nothing is saved in a file.
# So when the program closes, all data is gone. That is fine for now.

from datetime import datetime, timedelta

tasks = []      # this list will store all my tasks
study_log = []  # this list will store my study sessions




# this function gives a number for priority so i can sort tasks
def priority_number(p):
    if p == "High":
        return 1
    elif p == "Medium":
        return 2
    else:
        return 3






# simple sort by deadline using bubble sort (not the fastest but easy to understand)
def sort_by_deadline(task_list):
    new_list = task_list[:]  # copy the list so original does not change
    n = len(new_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if new_list[j]["deadline"] > new_list[j + 1]["deadline"]:
                temp = new_list[j]
                new_list[j] = new_list[j + 1]
                new_list[j + 1] = temp
    return new_list




def add_task():
    print("\n--- Add New Task ---")
    title = input("Enter task title: ")
    while title.strip() == "":
        print("Title can't be empty")
        title = input("Enter task title: ")

    subject = input("Enter subject: ")
    while subject.strip() == "":
        print("Subject can't be empty")
        subject = input("Enter subject: ")

    # checking date format
    while True:
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except:
            print("Wrong date format, try again like 2026-01-31")

    priority = input("Enter priority (High/Medium/Low): ")
    priority = priority.capitalize()
    while priority != "High" and priority != "Medium" and priority != "Low":
        print("Priority must be High, Medium or Low")
        priority = input("Enter priority: ").capitalize()

    new_task = {
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "priority": priority,
        "done": False
    }
    tasks.append(new_task)
    print("Task added!\n")




def print_task(i, t):
    if t["done"] == True:
        status = "Done"
    else:
        status = "Pending"

    today = datetime.now().strftime("%Y-%m-%d")
    tag = ""
    if t["deadline"] < today and t["done"] == False:
        tag = " (OVERDUE)"

    print(str(i) + ". [" + status + "] " + t["title"] + " | Subject: " + t["subject"] +
          " | Deadline: " + t["deadline"] + tag + " | Priority: " + t["priority"])


def view_all_tasks():
    if len(tasks) == 0:
        print("No tasks yet.\n")
        return

    sorted_tasks = sort_by_deadline(tasks)
    print("\n--- All Tasks ---")
    i = 1
    for t in sorted_tasks:
        print_task(i, t)
        i = i + 1
    print()





def view_pending():
    pending_list = []
    for t in tasks:
        if t["done"] == False:
            pending_list.append(t)

    if len(pending_list) == 0:
        print("No pending tasks.\n")
        return

    pending_list = sort_by_deadline(pending_list)
    print("\n--- Pending Tasks ---")
    i = 1
    for t in pending_list:
        print_task(i, t)
        i = i + 1
    print()


def view_completed():
    done_list = []
    for t in tasks:
        if t["done"] == True:
            done_list.append(t)

    if len(done_list) == 0:
        print("No completed tasks yet.\n")
        return

    print("\n--- Completed Tasks ---")
    i = 1
    for t in done_list:
        print_task(i, t)
        i = i + 1
    print()




def view_overdue():
    today = datetime.now().strftime("%Y-%m-%d")
    overdue_list = []
    for t in tasks:
        if t["done"] == False and t["deadline"] < today:
            overdue_list.append(t)

    if len(overdue_list) == 0:
        print("No overdue tasks. Good job!\n")
        return

    print("\n--- Overdue Tasks ---")
    i = 1
    for t in overdue_list:
        print_task(i, t)
        i = i + 1
    print()


def view_upcoming():
    today = datetime.now().date()
    cutoff = today + timedelta(days=3)
    upcoming_list = []

    for t in tasks:
        task_date = datetime.strptime(t["deadline"], "%Y-%m-%d").date()
        if t["done"] == False and today <= task_date <= cutoff:
            upcoming_list.append(t)

    if len(upcoming_list) == 0:
        print("No tasks due in next 3 days.\n")
        return

    upcoming_list = sort_by_deadline(upcoming_list)
    print("\n--- Upcoming Tasks (next 3 days) ---")
    i = 1
    for t in upcoming_list:
        print_task(i, t)
        i = i + 1
    print()


def view_by_subject():
    if len(tasks) == 0:
        print("No tasks yet.\n")
        return

    # get unique subject list without using set, just for practice
    subject_list = []
    for t in tasks:
        if t["subject"] not in subject_list:
            subject_list.append(t["subject"])

    print("\n--- Tasks by Subject ---")
    for sub in subject_list:
        print("\n" + sub + ":")
        i = 1
        for t in tasks:
            if t["subject"] == sub:
                print("  ", end="")
                print_task(i, t)
                i = i + 1
    print()





def search_task():
    if len(tasks) == 0:
        print("No tasks yet.\n")
        return

    keyword = input("Enter keyword to search: ").lower()
    found = []
    for t in tasks:
        if keyword in t["title"].lower() or keyword in t["subject"].lower():
            found.append(t)

    if len(found) == 0:
        print("No task found with that keyword.\n")
        return

    print("\n--- Search Results ---")
    i = 1
    for t in found:
        print_task(i, t)
        i = i + 1
    print()


def pick_a_task():
    if len(tasks) == 0:
        print("No tasks yet.\n")
        return None

    sorted_tasks = sort_by_deadline(tasks)
    i = 1
    for t in sorted_tasks:
        print_task(i, t)
        i = i + 1

    choice = input("Enter task number: ")
    if choice.isdigit() == False:
        print("Please enter a number.\n")
        return None

    choice = int(choice)
    if choice < 1 or choice > len(sorted_tasks):
        print("Invalid number.\n")
        return None

    return sorted_tasks[choice - 1]




def complete_task():
    print("\n--- Mark Task Complete ---")
    t = pick_a_task()
    if t != None:
        t["done"] = True
        print("Marked as done!\n")


def edit_task():
    print("\n--- Edit Task ---")
    t = pick_a_task()
    if t == None:
        return

    print("Leave blank to keep same value")
    new_title = input("New title (" + t["title"] + "): ")
    if new_title.strip() != "":
        t["title"] = new_title

    new_subject = input("New subject (" + t["subject"] + "): ")
    if new_subject.strip() != "":
        t["subject"] = new_subject

    new_deadline = input("New deadline (" + t["deadline"] + "): ")
    if new_deadline.strip() != "":
        try:
            datetime.strptime(new_deadline, "%Y-%m-%d")
            t["deadline"] = new_deadline
        except:
            print("Bad date format, deadline not changed")

    new_priority = input("New priority (" + t["priority"] + "): ").capitalize()
    if new_priority != "":
        if new_priority == "High" or new_priority == "Medium" or new_priority == "Low":
            t["priority"] = new_priority
        else:
            print("Bad priority, not changed")

    print("Task updated!\n")




def delete_task():
    print("\n--- Delete Task ---")
    t = pick_a_task()
    if t != None:
        tasks.remove(t)
        print("Task deleted!\n")

def log_study():
    print("\n--- Log Study Session ---")
    subject = input("Subject studied: ")
    minutes = input("Minutes studied: ")

    while minutes.isdigit() == False:
        print("Please enter numbers only")
        minutes = input("Minutes studied: ")

    entry = {
        "subject": subject,
        "minutes": int(minutes),
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    study_log.append(entry)
    print("Study session logged!\n")

def view_study_log():
    if len(study_log) == 0:
        print("No study sessions yet.\n")
        return

    print("\n--- Study Log ---")
    i = 1
    for e in study_log:
        print(str(i) + ". " + e["date"] + " | " + e["subject"] + " | " + str(e["minutes"]) + " minutes")
        i = i + 1
    print()

def total_study_time():
    if len(study_log) == 0:
        print("No study sessions yet.\n")
        return

    total = 0
    for e in study_log:
        total = total + e["minutes"]

    hours = total // 60
    minutes = total % 60
    print("\nTotal study time: " + str(hours) + "h " + str(minutes) + "m")

    # total per subject
    subject_totals = {}
    for e in study_log:
        if e["subject"] in subject_totals:
            subject_totals[e["subject"]] = subject_totals[e["subject"]] + e["minutes"]
        else:
            subject_totals[e["subject"]] = e["minutes"]

    print("By subject:")
    for sub in subject_totals:
        print("  " + sub + ": " + str(subject_totals[sub]) + " minutes")
    print()

def show_stats():
    print("\n--- Statistics ---")
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        total = len(tasks)
        done = 0
        for t in tasks:
            if t["done"] == True:
                done = done + 1
        pending = total - done

        today = datetime.now().strftime("%Y-%m-%d")
        overdue = 0
        for t in tasks:
            if t["done"] == False and t["deadline"] < today:
                overdue = overdue + 1

        rate = (done / total) * 100

        print("Total tasks: " + str(total))
        print("Completed: " + str(done))
        print("Pending: " + str(pending))
        print("Overdue: " + str(overdue))
        print("Completion rate: " + str(round(rate, 1)) + "%")

    if len(study_log) > 0:
        total_minutes = 0
        for e in study_log:
            total_minutes = total_minutes + e["minutes"]
        print("\nTotal study sessions: " + str(len(study_log)))
        print("Total minutes studied: " + str(total_minutes))
    else:
        print("\nNo study sessions yet.")
    print()


def make_bar(percent):
    # makes a simple text progress bar like [####------] 40%
    total_blocks = 10
    filled_blocks = int(total_blocks * percent / 100)
    bar = ""
    for i in range(total_blocks):
        if i < filled_blocks:
            bar = bar + "#"
        else:
            bar = bar + "-"
    return "[" + bar + "] " + str(round(percent, 1)) + "%"









def show_report():
    print("\n============================================")
    print("           STUDY PROGRESS REPORT")
    print("============================================")

    if len(tasks) == 0:
        print("No tasks added yet, nothing to report.")
    else:
        total = len(tasks)
        done = 0
        for t in tasks:
            if t["done"] == True:
                done = done + 1
        pending = total - done

        today = datetime.now().strftime("%Y-%m-%d")
        overdue = 0
        for t in tasks:
            if t["done"] == False and t["deadline"] < today:
                overdue = overdue + 1

        rate = (done / total) * 100

        print("\nTotal Tasks: " + str(total))
        print("Completed: " + str(done))
        print("Pending: " + str(pending))
        print("Overdue: " + str(overdue))
        print("Completion: " + make_bar(rate))

        # priority breakdown
        print("\n-- By Priority --")
        for p in ["High", "Medium", "Low"]:
            count = 0
            done_count = 0
            for t in tasks:
                if t["priority"] == p:
                    count = count + 1
                    if t["done"] == True:
                        done_count = done_count + 1
            print(p + " -> Total: " + str(count) + " Completed: " + str(done_count))

        # subject breakdown
        print("\n-- By Subject --")
        subject_list = []
        for t in tasks:
            if t["subject"] not in subject_list:
                subject_list.append(t["subject"])

        for sub in subject_list:
            sub_total = 0
            sub_done = 0
            for t in tasks:
                if t["subject"] == sub:
                    sub_total = sub_total + 1
                    if t["done"] == True:
                        sub_done = sub_done + 1
            sub_rate = (sub_done / sub_total) * 100
            print(sub + " -> " + str(sub_done) + "/" + str(sub_total) + " done  " + make_bar(sub_rate))

    # study time part
    print("\n-- Study Time --")
    if len(study_log) == 0:
        print("No study sessions logged yet.")
    else:
        total_minutes = 0
        for e in study_log:
            total_minutes = total_minutes + e["minutes"]
        hours = total_minutes // 60
        minutes = total_minutes % 60
        print("Total sessions: " + str(len(study_log)))
        print("Total time: " + str(hours) + "h " + str(minutes) + "m")

    print("============================================\n")




def show_menu():
    print("========================================")
    print("   STUDENT STUDY PLANNER & SCHEDULER")
    print("========================================")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. View Completed Tasks")
    print("5. View Overdue Tasks")
    print("6. View Upcoming Tasks (3 days)")
    print("7. View Tasks by Subject")
    print("8. Search Tasks")
    print("9. Edit Task")
    print("10. Mark Task Complete")
    print("11. Delete Task")
    print("12. Log Study Session")
    print("13. View Study Log")
    print("14. Total Study Time")
    print("15. Statistics")
    print("16. Full Report")
    print("17. Exit")




def main():
    print("Welcome to my Study Planner!\n")
    while True:
        show_menu()
        choice = input("Choose an option (1-17): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            view_pending()
        elif choice == "4":
            view_completed()
        elif choice == "5":
            view_overdue()
        elif choice == "6":
            view_upcoming()
        elif choice == "7":
            view_by_subject()
        elif choice == "8":
            search_task()
        elif choice == "9":
            edit_task()
        elif choice == "10":
            complete_task()
        elif choice == "11":
            delete_task()
        elif choice == "12":
            log_study()
        elif choice == "13":
            view_study_log()
        elif choice == "14":
            total_study_time()
        elif choice == "15":
            show_stats()
        elif choice == "16":
            show_report()
        elif choice == "17":
            print("Goodbye! Happy studying!")
            break
        else:
            print("Invalid choice, try again.\n")


main()