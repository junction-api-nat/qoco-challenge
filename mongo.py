import pymongo
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

def postTransport(transport):
  return db.transports.insert_one(transport)

def postTransport(transport):
  return db.transports.insert_one(transport)

def updateTransport(transport):
  db.transports.update_one(transport)
