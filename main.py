import pandas as pd

df = pd.read_csv('hotels.csv')

df_card = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_card_security = pd.read_csv('card_security.csv', dtype=str)


# If You want to read data in a specific format
# df = pd.read_csv('hotels.csv', dtype={'id':str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def available(self):
        # Checks the availability of a hotel
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

    def book(self):
        # Once booked changes the availability to no
        df.loc[df['id'] == self.hotel_id, 'available'] = "no"
        df.to_csv('hotels.csv', index=False)


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f""" 
        Thank Your For Booking the Hotel :)
        Here are your Details:
        Name : {self.customer_name}
        Hotel Name : {self.hotel_object.name}
        """
        return content


class SpaTicket:
    def __init__(self, hotel_object):
        self.hotel = hotel_object

    def generate_spa(self, name):
        content = f"""
        Thank Your For Booking the Spa Package:)
        Here are your Details:
        Name : {name}
        Hotel Name : {self.hotel.name}  
        """
        return content


class Card:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, cvc, name):
        card_data = {'number': self.number, 'expiration': expiration,
                     'cvc': cvc, 'holder': name}
        if card_data in df_card:
            return True
        else:
            return False


class SecureCreditCard(Card):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security['number'] == self.number, 'password'].squeeze()
        if given_password == password:
            return True
        else:
            return False


print(df)
hotel_id = int(input("Enter the id of the hotel you want to book "))
hotel = Hotel(hotel_id)

if hotel.available():
    card = SecureCreditCard('5678901234567890')
    if card.validate(expiration='12/28', cvc='456', name='JANE SMITH'):
        if card.authenticate(given_password='mypass1'):
            hotel.book()
            name = input("Enter Your Name ")
            ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(ticket.generate())
            spa = input("Do You want Spa package? ").lower()
            if spa == 'yes':
                spa = SpaTicket(hotel)
                print(spa.generate_spa(name))
        else:
            print("Credit card Authentication Failed")
    else:
        print("card not validated")

else:
    print("The hotel is not available ")
