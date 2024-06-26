# movie_theater.py

class NoSeatsAvailableError(Exception):
    pass

class SeatAlreadyReservedError(Exception):
    pass

class UserAlreadyReservedError(Exception):
    pass

class InvalidCancellationError(Exception):
    pass

class MovieTheater:
    def __init__(self, seats):
        self.seats = seats
        self.reservations = {}

    def reserve_seat(self, seat, user):
        if seat not in self.seats:
            raise ValueError("Invalid seat")
        if not self.seats[seat]:
            raise NoSeatsAvailableError("No seats available for this screening")
        if seat in self.reservations:
            raise SeatAlreadyReservedError("Seat already reserved")
        if user in self.reservations.values():
            raise UserAlreadyReservedError("User already reserved a seat")
        self.reservations[seat] = user
        print(f"Seat {seat} reserved for {user}")

    def cancel_reservation(self, seat, user):
        if seat not in self.reservations:
            raise InvalidCancellationError("Seat not reserved")
        if self.reservations[seat] != user:
            raise InvalidCancellationError("User does not match reservation")
        del self.reservations[seat]
        print(f"Reservation for seat {seat} cancelled")

try:
    #zarezerwujemy miejsca dla 2 osob 
    theater.reserve_seat("A1", "Ania Kania")
    theater.reserve_seat("A2", "Basia Stasia")

    #powinien wyskoczyc blad o rezerwacji osoby ktora juz ma rezerwacje
    theater.reserve_seat("A1", "Ania Kania")
except Exception as e:
    print(f"Error: {e}")

try:
    #usuniecie rezerawacji dla wczesniej zlozonych przez te osoby
    theater.cancel_reservation("A2", "Basia Stasia")
    theater.cancel_reservation("A2", "Ania Kania")
except Exception as e:
    print(f"Error: {e}")