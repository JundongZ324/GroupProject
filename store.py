class Store:
    """The Store class used to make Store objects"""
    def __init__(self):
        """initializes the class attributes of the Store"""
        self.products = []
        self.customers = []
    
    def add_product(self, product):
        """Adds a product into the store if it doesn't already exist inside the store object"""
        for prod in self.products:
            if prod.get_id() == product.get_id():
                return False       
        self.products.append(product)
        return True

    def find_product(self, product_id):
        """Finds the product object using the product id"""
        for product in self.products:
            if product.get_id() == product_id:
                return product
        return None

    def add_customer(self, customer):
        """Adds a customer into the store if ti doesn't already exist inside the store object"""
        for cust in self.customers:
            if cust.get_id() == customer.get_id():
                return False       
        self.customers.append(customer)
        return True

    def find_customer(self, customer_id):
        """Finds the customer object using the customer id"""
        for customer in self.customers:
            if customer.get_id() == customer_id:
                return customer
        return None