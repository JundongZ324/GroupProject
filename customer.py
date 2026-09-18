from cart import ShoppingCart

class Customer:
    """Customer class which creates Customer objects"""
    def __init__(self, customer_id, name):
        """initializes the class attributes of the customer object"""
        self.customer_id = customer_id
        self.name = name
        self.cart = ShoppingCart()

    def get_id(self):
        """Gets the id of the customer"""
        return self.customer_id

    def get_name(self):
        """Gets the name of the customer object"""
        return self.name

    def get_cart(self):
        """returns the ShoppingCart of the customer"""
        return self.cart