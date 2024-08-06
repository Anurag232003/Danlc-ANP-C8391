class OutOfStockError(Exception):
    def __init__(self, item, message="Item is out of stock"):
        self.item = item
        self.message = message
        super().__init__(f"{self.item}: {self.message}")

class InvalidOrderError(Exception):
    def __init__(self, item, quantity, message="Invalid order quantity"):
        self.item = item
        self.quantity = quantity
        self.message = message
        super().__init__(f"{self.item} (Quantity: {self.quantity}): {self.message}")

def process_order(order, stock):
    try:
        for item, quantity in order.items():
            if quantity <= 0:
                raise InvalidOrderError(item, quantity, "Order quantity must be greater than zero")
            if item not in stock:
                raise OutOfStockError(item, "Item not found in stock")
            if stock[item] < quantity:
                raise OutOfStockError(item, "Not enough stock available")

        # If all checks pass, process the order
        for item, quantity in order.items():
            stock[item] -= quantity
        print("Order processed successfully.")
        print("Updated stock:", stock)
    except (OutOfStockError, InvalidOrderError) as e:
        print(f"Order error: {e}")


stock = {
    'apple': 10,
    'banana': 5,
    'orange': 0
}

order_1 = {
    'apple': 3,
    'banana': 6,
}

order_2 = {
    'apple': -1,
    'banana': 2,
}

order_3 = {
    'apple': 5,
    'orange': 1,
}

order_4 = {
    'apple': 10,
    'banana': 5,
}

print("Processing order 1:")
process_order(order_1, stock)

print("\nProcessing order 2:")
process_order(order_2, stock)

print("\nProcessing order 3:")
process_order(order_3, stock)

print("\nProcessing order 4:")
process_order(order_4, stock)

