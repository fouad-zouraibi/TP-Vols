# This is a sample Python script.
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Airport:
    def __init__(self, name: str, code: str, lat: float, long: float):
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long

class Flight:
    def __init__(self, src_code: str, dst_code: str, duration: float):
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration

class FlightMap:
    def __init__(self):
        self.airports = []
        self.flights = []

    def import_airports(self, csv_file):
        with open(csv_file) as csvfile:
            list = csv.reader(csvfile)

            for row in list:
                print(row)
    def import_flights(self, csv_file):
        with open(csv_file) as csvfile:
            list = csv.reader(csvfile)

            for row in list:
                print(row)


flight_map = FlightMap()
flight_map.import_airports('/home/fouadzrb/PycharmProjects/vol app/aeroports.csv')
flight_map.import_flights('/home/fouadzrb/PycharmProjects/vol app/flights.csv')
