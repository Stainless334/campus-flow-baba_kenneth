
from campusflow.tickets import create_ticket
from campusflow.workflow import (
    assign_ticket,
    change_ticket_status,
    get_unresolved_queue,
    reopen_ticket,
)
from campusflow.reports import print_report
from campusflow.storage import load_tickets, save_tickets

tickets = []

def save_current_tickets():
    """Save the current tickets to the JSON file."""
    try:
        save_tickets(tickets)

    except ValueError as error:
        print(f"\nWarning: Changes could not be saved: {error}")


def display_ticket(ticket):

    print("\n" + "-" * 45)

    print(f"Ticket ID:       {ticket['id']}")

    print(f"Title:           {ticket['title']}")

    print(f"Category:        {ticket['category']}")

    print(f"Urgency:         {ticket['urgency'].title()}")

    print(f"Affected users:  {ticket['affected_users']}")

    print(f"Priority:        {ticket['priority'].upper()}")

    print(f"Status:           {ticket['status'].replace('_', ' ').title()}")

    print(f"Assigned to:     {ticket['assigned_to'] or 'Unassigned'}")

    print("-" * 45)

def create_new_ticket():

    print("\n--- CREATE NEW TICKET ---")

    title = input("Enter ticket title: ")
    category = input("Enter category (Network/Hardware/Software/Other): ")
    urgency = input("Enter urgency (Low/Medium/High): ")

    try:
        affected_users = int(input("Enter number of affected users: "))

        ticket = create_ticket(
            title,
            category,
            urgency,
            affected_users,
            tickets,
        )

        tickets.append(ticket)

        save_current_ticket

        print("\nTicket created successfully!")
        display_ticket(ticket)

    except ValueError as error:
        print(f"\nError: {error}") 

def list_tickets():
    print("\n--- ALL TICKETS ---")

    if not tickets:
        print("No tickets have been created yet.")
        return

    for ticket in tickets:
        display_ticket(ticket) 

def view_ticket():
    ticket_id = input("Enter ticket ID (e.g. T001): ").strip().upper()

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            display_ticket(ticket)
            return

    print(f"Ticket {ticket_id} was not found.")  

def assign_existing_ticket():

    print("\n--- ASSIGN TICKET ---")

    ticket_id = input("Enter ticket ID: ").strip().upper()
    staff_name = input("Enter staff member's name: ")

    try:
        ticket = assign_ticket(tickets, ticket_id, staff_name)
        save_current_tickets()

        print(f"\nTicket {ticket_id} assigned successfully.")
        display_ticket(ticket)

    except ValueError as error:
        print(f"\nError: {error}")

def update_ticket_status():
    print("\n--- UPDATE TICKET STATUS ---")

    ticket_id = input("Enter ticket ID: ").strip().upper()

    print("Available statuses:")
    print("1. Open")
    print("2. In Progress")
    print("3. Resolved")

    status_choices = {
        "1": "open",
        "2": "in_progress",
        "3": "resolved",
    }

    choice = input("Choose a status (1-3): ").strip()

    if choice not in status_choices:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    try:
        ticket = change_ticket_status(
            tickets,
            ticket_id,
            status_choices[choice],
        )

        save_current_tickets()

        print("\nTicket status updated successfully.")
        display_ticket(ticket)

    except ValueError as error:
        print(f"\nError: {error}")

def reopen_existing_ticket():
    ticket_id = input("Enter the resolved ticket ID to reopen: ").strip().upper()

    try:
        ticket = reopen_ticket(tickets, ticket_id)

        save_current_tickets()

        print(f"\nTicket {ticket_id} has been reopened.")
        display_ticket(ticket)

    except ValueError as error:
        print(f"\nError: {error}")


def show_unresolved_queue():
    print("\n--- UNRESOLVED TICKET QUEUE ---")

    queue = get_unresolved_queue(tickets)

    if not queue:
        print("There are no unresolved tickets.")
        return

    for ticket in queue:
        display_ticket(ticket)


def show_reports():
    print_report(tickets)


def main():

    global tickets

    try:
        tickets = load_tickets()
        print(f"Loaded {len(tickets)} saved ticket(s).")

    except ValueError as error:
        print(f"\nStorage error: {error}")
        print("CampusFlow cannot start safely until this is fixed.")
        return

    while True:
        print("\n===================================")
        print("       CAMPUSFLOW HELPDESK")
        print("===================================")
        print("1. Create a ticket")
        print("2. List all tickets")
        print("3. View one ticket")
        print("4. Assign a ticket")
        print("5. Update ticket status")
        print("6. Reopen a resolved ticket")
        print("7. View unresolved queue")
        print("8. View reports")
        print("9. Exit")
        print("===================================")

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            create_new_ticket()

        elif choice == "2":
            list_tickets()

        elif choice == "3":
            view_ticket()

        elif choice == "4":
            assign_existing_ticket()

        elif choice == "5":
            update_ticket_status()

        elif choice == "6":
            reopen_existing_ticket()

        elif choice == "7":
            show_unresolved_queue()

        elif choice == "8":
            show_reports()

        elif choice == "9":
            print("Thank you for using CampusFlow. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()   