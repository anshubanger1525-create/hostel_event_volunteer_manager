assignments = []


def assign_volunteer():
    volunteer = input("Enter volunteer name: ")
    event = input("Enter event name: ")
    role = input("Enter assigned role: ")

    assignment = {
        "volunteer": volunteer,
        "event": event,
        "role": role
    }

    assignments.append(assignment)
    print("Volunteer assigned successfully!")


def view_assignments():
    if not assignments:
        print("No assignments found.")
        return

    print("\n===== ASSIGNMENTS =====")

    for i, assignment in enumerate(assignments, 1):
        print(f"{i}. Volunteer: {assignment['volunteer']}")
        print(f"   Event: {assignment['event']}")
        print(f"   Role: {assignment['role']}")
