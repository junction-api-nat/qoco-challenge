from api import client
from src import mongo
import json

mongo.postBookings(client.get_all_bookings())
mongo.postTransports(client.get_all_transports()["transports"])

""" stations = []
for key, value in client.get_all_stations().items():
  stations.append([key, value])
mongo.postStations(stations) """

