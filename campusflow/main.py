from ticket_create import add
from ticket_list import list_tickets, view_ticket
from assign import assign_ticket

def main():
    while True:
        print("""
        \n_______ CAMPUSFLOW _______"
        
    1. Create Ticket
    2. List All Tickets
    3. View One Ticket
    4. Assign Ticket
    5. Exit""")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add()
        elif choice == "2":
            list_tickets()
        elif choice == "3":
            view_ticket()
        elif choice == "4":
            assign_ticket()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1-5.")



main()