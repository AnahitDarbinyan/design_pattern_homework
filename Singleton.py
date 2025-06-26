# Wi-Fi Manager
class WiFiConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Connecting to Wi-Fi...")
            cls._instance = super().__new__(cls)
            cls._instance.connected = True
        return cls._instance

    def disconnect(self):
        self.connected = False
        print("Disconnected from Wi-Fi.")

    def status(self):
        print("Connected" if self.connected else "Not Connected")

wifi1 = WiFiConnection()
wifi1.status()

wifi2 = WiFiConnection()
wifi2.disconnect()

wifi1.status()
print(wifi1 is wifi2)