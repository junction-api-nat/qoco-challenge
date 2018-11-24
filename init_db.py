from api import client
import mongo

mongo.postBookings(client.get_all_bookings())
mongo.postStations(client.get_all_stations())
mongo.postTransports(client.get_all_transports().transports)
