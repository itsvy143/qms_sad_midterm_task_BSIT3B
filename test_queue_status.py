from queue_status import (
    update_ticket_status,
    show_queue_status
)

queue = [
    {"number": 1, "status": "Waiting"},
    {"number": 2, "status": "Waiting"}
]

update_ticket_status(queue, 1, "Serving")
update_ticket_status(queue, 2, "Completed")

show_queue_status(queue)