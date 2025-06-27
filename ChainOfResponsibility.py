class OrderHandler:

    def __init__(self, successor=None):
        self._next = successor

    def handle(self, order):
        if self._can_handle(order):
            self._process(order)
        elif self._next:
            self._next.handle(order)
        else:
            print(f"Nobody can handle: {order['item']}")

    def _can_handle(self, order):
        raise NotImplementedError

    def _process(self, order):
        raise NotImplementedError


class DrinkStation(OrderHandler):
    def _can_handle(self, order):
        return order["item"] in ["soda", "beer", "water"]

    def _process(self, order):
        print(f"🧊 Drink station preparing {order['item']}")


class GrillStation(OrderHandler):
    def _can_handle(self, order):
        return order["item"] in ["burger", "steak", "chicken"]

    def _process(self, order):
        print(f"Grill cooking {order['item']}")


class SaladStation(OrderHandler):
    def _can_handle(self, order):
        return "salad" in order["item"]

    def _process(self, order):
        print(f"Salad station making {order['item']}")

kitchen = DrinkStation(
    GrillStation(
        SaladStation()))

orders = [
    {"item": "burger", "table": 5},
    {"item": "caesar salad", "table": 3},
    {"item": "beer", "table": 2},
    {"item": "sushi", "table": 1}
]

print("=== Kitchen Orders ===")
for order in orders:
    kitchen.handle(order)