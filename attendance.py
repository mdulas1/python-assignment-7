"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    if student_id not in attendance:
        attendance[student_id] = {
            "name":name,
            'present_days':[],
            "absent_days":[]
        }
    else:
        print(f"{student_id} already registered")


def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    # implement logic
    for stu_id in student_ids:
        if stu_id in attendance:
            if today not in attendance[stu_id]["present_days"]:
                attendance[stu_id]["present_days"].append(today)
            if today in attendance[stu_id]["absent_days"]:
                attendance[stu_id]["absent_days"].remove(today)
            else:
                print(f"student {stu_id} not found")

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    #implement logic
    for stu_id in student_ids:
        if stu_id in attendance:
            if today not in attendance[stu_id]["absent_days"]:
                attendance[stu_id]["absent_days"].append(today)
            if today in attendance[stu_id]["present_days"]:
                attendance[stu_id]["absent_days"].remove(today)
            else:
                print(f"student {stu_id} not found")


def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    # implement logic
    for stu_id,data in attendance.items():
        if kwargs.get("only_present") and not data["present_days"]:
            continue
        if kwargs.get("only absent") and not data["absent_days"]:
            continue
        report[stu_id] = data


    return report
register_student(1,"ummi")
register_student(2,"godiya")
register_student(3,"oklo")

mark_present([1,3])
mark_absent([2])
print("report",get_report())
print("only_present",get_report(only_present=True))
print("only_absent",get_report(only_absent=True))
