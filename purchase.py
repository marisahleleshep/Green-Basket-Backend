# Define a method to add a purchase amount to the total purchase
def add_purchase(self, amount):
        self.total_purchase += amount
          # Define a method to remove a purchase amount from the total purchase
def remove_purchase(self, amount):
        if self.total_purchase >= amount:
            self.total_purchase -= amount
        else:
            print("The amount is greater than the total purchase.")
    # Define a method to calculate preference based on a given number
def preference(self, num):
        return num ** 2