import pandas as pd

df = pd.read_csv('hotels.csv')


# If You want to read data in a specific format
# df = pd.read_csv('hotels.csv', dtype={'id':str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def available(self):
        # Checks the availability of a hotel
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        print(availability)
        if availability == 'yes':
            return True
        else:
            return False

    def book(self):
        # Once booked changes the availability to no
        df.loc[df['id'] == self.hotel_id, 'available'] = "no"
        df.to_csv('hotels.csv', index=False)
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
hotel_id = int(input("Enter the id of the hotel you want to book "))
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter Your Name ")
    ticket = ReservationTicket(name, hotel)
    print(ticket.generate())
else:
    print("The hotel is not available ")
