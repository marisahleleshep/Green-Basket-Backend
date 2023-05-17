# Create an instance of the Customer class

customer1 = Customer("Mwangi", "mwangi@gmail.com", "Kasarani", "5234-456-987")
customer1.add_purchase(120)

print(customer1.total_purchase)

print(customer1.preference(8))

print(customer1.discount())  # Print the discount percentage based on total purchases

customer1.remove_purchase(50)

print(customer1.total_purchase)