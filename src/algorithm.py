from src.graph import get_graph_with_edges


def get_sorted_bookings(bookings):
    return sorted(bookings, key=lambda x: x.booking_date)


def calculate_optimal_transport(g, booking):
    pass


def handle_booking(g, booking, date):
    if date != booking.booking_date:
        date = booking.booking_date
        transports_with_date = []  # mongo.getTransportsWithDate(date)
        g = get_graph_with_edges(g, transports_with_date)
    calculate_optimal_transport(g, booking)
    return date, g


def run(g, priority_bookings, non_priority_bookings):
    high_priority_bookings = get_sorted_bookings(priority_bookings)
    non_priority_bookings = get_sorted_bookings(non_priority_bookings)
    date = None
    for booking in high_priority_bookings:
        date, g = handle_booking(g, booking, date)

    date = None
    for booking in non_priority_bookings:
        date, g = handle_booking(g, booking, date)


if __name__ == '__main__':
    pass
    # priority_bookings = mongo.getHighPriorityBookings()
    # non_priority_bookings = mongo.getNonPriorityBookings()
    # run(g, priority_bookings, non_priority_bookings)
