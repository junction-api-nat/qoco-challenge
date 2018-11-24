import pymongo
from pymongo import MongoClient
import os

DB_NAME = "junction-challenge"
DB_HOST = os.environ.get("SECRET")
DB_PORT = 15434
DB_USER = "tommi"
DB_PASS = os.environ.get("PASSWD")

client = MongoClient(DB_HOST, DB_PORT)
db = client[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

def getAllBookings():
  return db.bookings.find({})

def postBooking(booking):
  db.booking.insertOne(booking)

def getAllStations():
  return db.stations.find({})

def postStation(station):
  db.stations.insertOne(station)

def getAllTransports():
  return db.transports.find({})

def postTransport(transport):
  return db.transports.insertOne(transport)
