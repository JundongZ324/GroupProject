class Product:
    """The product class, used to make Product objects"""
    def __init__(self, product_id, name, price):
        """initializes the class attributes for product"""
        self.product_id = product_id
        self.name = name
        self.price = float(price)

    def get_id(self):
        """Gets the id of the product object"""
        return self.product_id

    def get_name(self):
        """Gets the name of the product object"""
        return self.name

    def get_price(self):
        """Gets the price of the Product object"""
        return self.price
