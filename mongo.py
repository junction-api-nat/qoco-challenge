import pymongo
import datetime
from pymongo import MongoClient
import os

DB_NAME = "junction-challenge"
DB_HOST = os.environ.get("SECRET")
DB_PORT = 15434
DB_USER = "testuser"
DB_PASS = os.environ.get("PASSWD")

client = MongoClient(DB_HOST, DB_PORT)
db = client[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

# Bookings
def getAllBookings():
  return db.bookings.find({})

def getBooking(booking_id):
  return db.bookings.find_one({"booking_id": booking_id})

def getPriorityBookings():
  return list(db.bookings.find({"high_priority": True}))

def getNonPriorityBookings():
  return list(db.bookings.find({"high_priority": False}))    

def postBookings(bookings):
  db.bookings.insert_many(bookings)

def postBooking(booking):
  db.bookings.insert_one(booking)

def updateBooking(booking):
  db.bookings.update_one(booking)

# Stations
def getAllStations():
  return db.stations.find({})

def postStations(stations):
  db.stations.insert_many(stations)

def postStation(station):
  db.stations.insert_one(station)

def updateStation(station):
  db.stations.update_one(station)

# Transports
def getAllTransports():
  return db.transports.find({})

def getTransport(transport_number):
  return db.transports.find({"transport_number": transport_number})

def getBookingsForTransport(transport_number):
  return db.transports.find_one({"transport_number": transport_number})["bookings"]

def getRemainingTransportCapacity(transport):
  bookings = getBookingsForTransport(transport.transport_number)
  bookings_capacity = {
    total_weight: 0,
    total_volume: 0
  }
  for booking_id in bookings:
    booking = getBooking(booking_id)
    bookings_capacity.total_weight += booking.total_weight
    bookings_capacity.total_volume += booking.total_volume

  return {
    weight: transport.capacity_weight - bookings_capacity.total_weight,
    volume: transport.capacity_volume - bookings_capacity.total_volume
  }

def postTransports(transports):
  return db.transports.insert_many(transports)

def postTransport(transport):
  return db.transports.insert_one(transport)

def updateTransport(transport):
  db.transports.update_one(transport)
