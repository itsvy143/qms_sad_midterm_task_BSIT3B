from queue_manager import add_ticket, list_tickets
from queue_status import update_ticket_status, show_queue_status

def main():
    queue = []
    next_number = 1

    while True:
        print("\nQUEUE MANAGEMENT SYSTEM")
        print("1. Generate Queue Ticket")
        print("2. View All Tickets")
        print("3. Update Ticket Status")
        print("4. View Queue Status")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            next_number = add_ticket(queue, next_number)

        elif choice == "2":
            list_tickets(queue)

        elif choice == "3":
            try:
                number = int(input("Enter ticket number: "))
                status = input("Enter status (Waiting, Serving, Completed): ").strip().title()

                update_ticket_status(queue,number, status)

            except ValueError:
                print("Please enter a valid ticket number.")

        elif choice == "4":
            show_queue_status(queue)

        elif choice == "5":
            print("Thank you for using QMS.")
            break

        else:
            print("Invalid choice.Please select 1 to 5.")

if __name__ == "__main__":
    main()
        