import pandas as pd

df = pd.read_csv('hotels.csv')


class Hotel:
    def __init__(self, hotel_id):
        pass

    def available(self):
        pass

    def book(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
hotel_id = int(input("Enter the hotel_id of the hotel you want to book "))
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter Your Name ")
    ticket = ReservationTicket(name,hotel)
    print(ticket.generate())
else:
    print("THe hotel is not available ")