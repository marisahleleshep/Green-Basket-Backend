# Create an instance of the Mama_Mboga class

vendor = Mama_Mboga("Potatoes", 50, 2.99, "Sell")
print(vendor)

vendor.new_stock("Kales")
print(vendor)

vendor.quantity_products(100)
print(vendor)

vendor.pricing(1.99)
print(vendor)

vendor.update_action("Restock")
print(vendor)