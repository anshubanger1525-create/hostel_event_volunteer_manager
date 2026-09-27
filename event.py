events = []


def add_event():
    name = input("Enter event name: ")
    date = input("Enter event date: ")
    venue = input("Enter venue: ")

    event = {
        "name": name,
        "date": date,
        "venue": venue
    }

    events.append(event)

    print("Event added successfully!")


def view_events():
    if not events:
        print("No events available.")
        return

    print("\n===== EVENTS =====")

    for i, event in enumerate(events, 1):
        print(f"{i}. {event['name']}")
        print(f"   Date: {event['date']}")
        print(f"   Venue: {event['venue']}")