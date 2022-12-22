# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 14:03:59 2022

@author: fouad
"""
from Airport import Airport
from Flight import Flight


class Flightmap:
    def __init__(self, src_code, dst_code, duration):
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration

    def import_airports(self, csv_file: str) -> None:
        with open(csv_file, mode='r') as f:
            s = f.read()
            lines = map(lambda x: x.split(','), s.split('\n')[:-1])
            airports = map(lambda x: Airport(x[0], x[1], x[2], x[3]), lines)

            return list(airports)

    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, mode='r') as f:
            s = f.read()
            lines = map(lambda x: x.split(','), s.split('\n')[:-1])
            flights = map(lambda x: Flight(x[0], x[1], x[2]), lines)

            return list(flights)

    def airports(self) -> list[Airport]:
        return self.import_airports('/home/fouadzrb/Documents/tp/aeroports.csv')

    def flights(self) -> list[Flight]:
        return self.import_flights('/home/fouadzrb/Documents/tp/flights.csv')

    def airport_find(self, airport_code: str) -> Airport:
        airport = list(filter(lambda x: x.code == airport_code, self.airports()))
        if len(airport) > 0:
            return airport[0]
        return None

    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        flight = list(
            filter(lambda x: x.src_code == src_airport_code and x.dst_code == dst_airport_code, self.flights()))
        if len(flight) > 0:
            return True
        return False
