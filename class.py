# Define a class called Customer
class Customer:
    # Define the constructor method to initialize the Customer object
    def __init__(self, name, email, location, phoneNumber):
        self.name = name
        self.email = email
        self.location = location
        self.phoneNumber = phoneNumber
        self.total_purchase = 0

    # Define a method to calculate the discount based on total purchases
    def discount(self):
        if self.total_purchase >= 100:
            return 0.1
        else:
            return 0