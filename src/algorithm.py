from . import graph
from .api import client


def sort_bookings(bookings):
    bookings.sort(key=lambda x: x.booking_date)


def calculate_optimal_transport(g, booking):
    pass


def divide_bookings_priority(bookings):
    high_priority_bookings = []
    non_priority_bookings = []
    for booking in bookings:
        if booking.high_priority == "True":
            high_priority_bookings.append(booking)
        else:
            non_priority_bookings.append(booking)
    return high_priority_bookings, non_priority_bookings


def handle_booking(g, booking, date):
    if date != booking.booking_date:
        date = booking.booking_date
        transports_with_date = []  # mongo.getTransportsWithDate(date)
        g = get_graph_with_edges(g, transports_with_date)
    calculate_optimal_transport(g, booking)
    return date, g


def run():
    g = graph.create_graph(client.get_all_stations(),
                           client.get_all_transports())

    bookings = client.get_all_bookings()
    high_priority_bookings, non_priority_bookings = divide_bookings_priority(bookings)

    sort_bookings(high_priority_bookings)
    sort_bookings(non_priority_bookings)

    date = None
    for booking in high_priority_bookings:
        date, g = handle_booking(g, booking, date)

    date = None
    for booking in non_priority_bookings:
        date, g = handle_booking(g, booking, date)


if __name__ == '__main__':
    run()



    # priority_bookings = mongo.getHighPriorityBookings()
    # non_priority_bookings = mongo.getNonPriorityBookings()
    # run(g, priority_bookings, non_priority_bookings)
