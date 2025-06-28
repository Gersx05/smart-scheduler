#SMARTSCHEDULER

import re

# List to store exam schedule entries
exam_schedules = []

# Check if date is in MM-DD-YYYY format
def is_valid_date(date):
    return bool(re.match(r'^\d{2}-\d{2}-\d{4}$', date))

# Check if time is in HH:MM 24-hour format
def is_valid_time(time):
    return bool(re.match(r'^([01]\d|2[0-3]):[0-5]\d$', time))

# Add a new exam to the schedule
def add_exam():
    name = input("Enter exam name: ")

    date = input("Enter exam date (MM-DD-YYYY): ")
    if not is_valid_date(date):
        print("Invalid date format. Please use MM-DD-YYYY.")
        return

    time = input("Enter exam time (HH:MM): ")
    if not is_valid_time(time):
        print("Invalid time format. Please use HH:MM in 24-hour format.")
        return

    room = input("Enter assigned room: ")

    # Store exam as a dictionary inside the list
    exam_schedules.append({
        "name": name,
        "date": date,
        "time": time,
        "room": room
    })
    print("\nExam added successfully.\n")


# Display exams (with numbering using enumerate)
def view_exams():
    if not exam_schedules:
        print("\nNo exams have been scheduled yet.\n")
        return
    print("\nScheduled Exams:")
    for i, exam in enumerate(exam_schedules, start=1):
        print(f"{i}. {exam['name']} - {exam['date']} at {exam['time']} in Room {exam['room']}")
    print()

# Edit an exam (allows partial updates)
def edit_exam():
    view_exams()
    if not exam_schedules:
        return
    try:
        index = int(input("Enter the exam number to edit: ")) - 1
        if 0 <= index < len(exam_schedules):
            print("Leave blank to keep current value.")

            # Update values or keep existing if input is blank
            name = input("New exam name: ") or exam_schedules[index]["name"]

            # Ask for new date.
            date = input("New exam date (MM-DD-YYYY): ")
            if date and not is_valid_date(date):
                print("Invalid date format. Keeping old value.")
                date = exam_schedules[index]["date"]
            elif not date:
                date = exam_schedules[index]["date"]

            # Ask for new time. If it's invalid, keep the old one.
            time = input("New exam time (HH:MM): ")
            if time and not is_valid_time(time):
                print("Invalid time format. Keeping old value.")
                time = exam_schedules[index]["time"]
            elif not time:
                time = exam_schedules[index]["time"]

            # Ask for new room. If blank, keep the old one.
            room = input("New room: ") or exam_schedules[index]["room"]

            # Update dictionary values
            exam_schedules[index] = {
                "name": name,
                "date": date,
                "time": time,
                "room": room
            }
            print("\nExam updated successfully.\n")
        else:
            print("Invalid exam number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# This function allows the user to remove an exam from the list.
def delete_exam():
    view_exams() # Show current exams
    if not exam_schedules:
        return

    try:
        # Ask which exam to delete.
        index = int(input("Enter the exam number to delete: ")) - 1
        if 0 <= index < len(exam_schedules):
            removed = exam_schedules.pop(index)
            print(f"\n'{removed['name']}' has been removed from the schedule.\n")
        else:
            print("Invalid exam number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# This is the main menu that lets the user choose what to do.
def main_menu():
    while True:
        print("==== SMART EXAM SCHEDULER MENU ====")
        print("1. Add Exam")
        print("2. View Exams")
        print("3. Edit Exam")
        print("4. Delete Exam")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        # Depending on the user’s choice.
        if choice == "1":
            add_exam()
        elif choice == "2":
            view_exams()
        elif choice == "3":
            edit_exam()
        elif choice == "4":
            delete_exam()
        elif choice == "5":
            print("\nExiting the program. Thank you for using Smart Exam Scheduler.\n")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.\n")

# This line runs the program by calling the main menu.
if __name__ == "__main__":
    main_menu()
