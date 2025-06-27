class EuropeanSocket:
    def provide_electricity(self):
        return "220V from European socket"

class Laptop:
    def charge(self, socket: EuropeanSocket):
        print(f"Laptop charging using: {socket.provide_electricity()}")

class Phone:
    def charge_with_usb_c(self):
        return "Charging phone with USB-C"


class PhoneAdapter:
    def __init__(self, phone: Phone):
        self.phone = phone

    def provide_electricity(self):
        return self.phone.charge_with_usb_c() + " via Adapter"


socket = EuropeanSocket()
laptop = Laptop()
phone = Phone()

laptop.charge(socket)

adapter = PhoneAdapter(phone)
laptop.charge(adapter)