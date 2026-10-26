def add_ticket(queue, next_number):
    """Create a ticket and add it to the queue."""
    ticket = {
        "number": next_number,
        "status": "Waiting"
    }

    queue.append(ticket)

    print(f"Ticket Q{next_number:03d} created successfully.")
    return next_number + 1


def list_tickets(queue):
    """Display all tickets in the queue."""
    print("\nCURRENT QUEUE")
    print("-------------")

    if not queue:
        print("No tickets in the queue.")
        return

    for ticket in queue:
        print(
            f"Ticket Q{ticket['number']:03d} - "
            f"{ticket['status']}"
        )