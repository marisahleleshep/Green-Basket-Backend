# Define a class called Mama_Mboga
class Mama_Mboga:
    
    # Define the constructor method to initialize the Mama_Mboga object

    def __init__(self, product_name, quantity, price, action):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.action = action

    # Define a method to update the product name

    def new_stock(self, new_product):
        self.product_name = new_product