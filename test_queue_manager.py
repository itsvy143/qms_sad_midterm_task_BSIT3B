from queue_manager import add_ticket, list_tickets

queue = []
next_number = 1

next_number = add_ticket(queue, next_number)
next_number = add_ticket(queue, next_number)

list_tickets(queue)