from event import events
from volunteer import volunteers
from assignments import assignments


def generate_report():
    print("\n===== PROJECT REPORT =====")

    print(f"Total Events: {len(events)}")
    print(f"Total Volunteers: {len(volunteers)}")
    print(f"Total Assignments: {len(assignments)}")

    print("\n--- Events ---")
    for event in events:
        print(event)

    print("\n--- Volunteers ---")
    for volunteer in volunteers:
        print(volunteer)

    print("\n--- Assignments ---")
    for assignment in assignments:
        print(assignment)