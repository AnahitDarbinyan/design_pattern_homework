# Travel Agency
class FlightBooking:
    def book_flight(self):
        print("Flight booked successfully.")

class HotelBooking:
    def book_hotel(self):
        print("Hotel booked successfully.")

class TourBooking:
    def book_tour(self):
        print("City tour booked successfully.")

class TravelAgency:
    def __init__(self):
        self.flight = FlightBooking()
        self.hotel = HotelBooking()
        self.tour = TourBooking()

    def book_vacation_package(self):
        print("Starting vacation package booking...")
        self.flight.book_flight()
        self.hotel.book_hotel()
        self.tour.book_tour()
        print("Vacation package booking complete!\n")

if __name__ == "__main__":
    agency = TravelAgency()
    agency.book_vacation_package()