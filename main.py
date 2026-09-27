from event import add_event, view_events
from volunteer import add_volunteer, view_volunteers
from assignments import assign_volunteer, view_assignments
from report import generate_report


def main():
    while True:
        print("\n===== HOSTEL EVENT VOLUNTEER MANAGER =====")
        print("1. Add Event")
        print("2. View Events")
        print("3. Add Volunteer")
        print("4. View Volunteers")
        print("5. Assign Volunteer")
        print("6. View Assignments")
        print("7. Generate Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            add_volunteer()
        elif choice == "4":
            view_volunteers()
        elif choice == "5":
            assign_volunteer()
        elif choice == "6":
            view_assignments()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("Thank you for using Hostel Event Volunteer Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
      
    
      
