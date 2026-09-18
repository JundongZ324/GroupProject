class ShoppingCart:
    """Creates a shopping cart object"""
    def __init__(self):
        self.items = []
        

    def add_product(self, product):
        """adds a Product object into cart"""
        self.items.append(product)

    def remove_product(self, product_id):
        """removes any specified products from the cart object"""
        for product in self.items:
            if product.get_id() == product_id:
                self.items.remove(product)
                return True
        return False


    def get_items(self):
        """returns all products inside a ShoppingCart object"""
        return self.items

    def calculate_total(self):
        """calculates the total of all products inside a cart object"""
        sum = 0
        for product in self.items:
            sum += product.get_price()
        return sum

    def is_empty(self):
        """Checks if the cart is empty"""
        return len(self.items) == 0