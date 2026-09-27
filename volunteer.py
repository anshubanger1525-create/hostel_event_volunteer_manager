
volunteers = []


def add_volunteer():
    name = input("Enter volunteer name: ")
    phone = input("Enter phone number: ")
    skill = input("Enter skill: ")

    volunteer = {
        "name": name,
        "phone": phone,
        "skill": skill
    }

    volunteers.append(volunteer)
    print("Volunteer added successfully!")


def view_volunteers():
    if not volunteers:
        print("No volunteers found.")
        return

    print("\n--- Volunteer List ---")

    for i, volunteer in enumerate(volunteers, 1):
        print(f"{i}. Name: {volunteer['name']}")
        print(f"   Phone: {volunteer['phone']}")
        print(f"   Skill: {volunteer['skill']}")



