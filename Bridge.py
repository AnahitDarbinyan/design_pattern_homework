#
# from abc import ABC , abstractmethod
#
# # ~ IMPLEMENTOR ~
#
# class Device(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass
#     def turn_off(self):
#         pass
#
# # ~ Concrete implementors ~
# class TV(Device):
#
#     def turn_on(self):
#         print("TV is now ON.")
#
#     def turn_off(self):
#         print("TV is now OFF.")
#
# class Radio(Device):
#     def turn_on(self):
#         print("Radio is now ON.")
#
#     def turn_off(self):
#         print("Radio is now OFF.")
#
# # ~ ABSTRACTION ~
# class RemoteControl:
#     def __init__(self, device: Device):
#         self.device = device
#
#     def press_power(self):
#         print("[Remote] Toggling power: ")
#         self.device.turn_on()
#
# class AdvancedRemoteControl(RemoteControl):
#     def press_power(self):
#         print("[Advanced Remote] Power button pressed.")
#         self.device.turn_on()
#
#     def press_mute(self):
#         print("[Advanced Remote] Muting device.")
#
# if __name__ == "__main__":
#     tv = TV()
#     radio = Radio()
#     basic_remote = RemoteControl(tv)
#     basic_remote.press_power()
#
#     advanced_remote = AdvancedRemoteControl(radio)
#     advanced_remote.press_power()
#     advanced_remote.press_mute()


from abc import ABC, abstractmethod

# ~ Implementor ~
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# ~ Concrete Implementors ~
class PayPalGateway(PaymentGateway):
    def pay(self, amount: float):
        print(f"Paying ${amount} via PayPal.")

class CreditCardGateway(PaymentGateway):
    def pay(self, amount: float):
        print(f"Paying ${amount} via PayPal.")

# ~ Abstraction ~
class Payment:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def process(self, amount: float):
        print("[Payment] Processing one-time payment:")

# ~ Refined Abstraction ~
class ScheduledPayment(Payment):
    def process(self, amount: float):
        print("[ScheduledPayment] Processing scheduled payments:")
        for month in range(1, 4):
            print(f" Month {month}:")
            self.gateway.pay(amount)

# ~ Client ~
if __name__ == "__main__":
    paypal = PayPalGateway()
    card = CreditCardGateway()

    one_time = Payment(paypal)
    one_time.process(100)

    recurring = ScheduledPayment(card)
    recurring.process(50)