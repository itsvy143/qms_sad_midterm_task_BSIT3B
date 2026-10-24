def update_ticket_status(queue, ticket_number, new_status):
    """Update the status of an existing ticket."""
    valid_statuses = ["Waiting", "Serving", "Completed"]

    if new_status not in valid_statuses:
        print("Invalid status.")
        return False

    for ticket in queue:
        if ticket["number"] == ticket_number:
            ticket["status"] = new_status
            print(
                f"Ticket Q{ticket_number:03d} "
                f"updated to {new_status}."
            )
            return True

    print(f"Ticket Q{ticket_number:03d} not found.")
    return False


def show_queue_status(queue):
    """Display the status of every ticket."""
    print("\nQUEUE STATUS")
    print("------------")

    if not queue:
        print("No tickets in the queue.")
        return

    for ticket in queue:
        print(
            f"Ticket Q{ticket['number']:03d}: "
            f"{ticket['status']}"
        )