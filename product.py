# Define a method to remove a purchase amount from the total purchase
def remove_purchase(self, amount):
        if self.total_purchase >= amount:
            self.total_purchase -= amount
        else:
            print("The amount is greater than the total purchase.")
            
            
# Define a method to update the quantity of products

def quantity_products(self, new_quantity):
        self.quantity = new_quantity
        
# Define a method to update the price of the product

def pricing(self, new_price):
        self.price = new_price
        
# Define a method to update the action associated with the product

def update_action(self, needed_action):
        self.action = needed_action
        
# Define a method to display the Mama_Mboga object as a string

def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price},{self.action}"
            