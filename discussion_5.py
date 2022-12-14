import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in sentence:
		if i == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		items_dict = {}
		num_most_stock = 0
		most_stock = 'none'
		for item in self.items:
			items_dict[item] = items_dict.get(items_dict[item, 0]) + 1
			if items_dict[item] > num_most_stock:
				most_stock = items_dict[item]
		return most_stock
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		items_dict = {}
		num_most_stock = 0
		most_stock = ''
		for item in self.items:
			items_dict[item] = items_dict.get(items_dict[item, 0]) + 1
			if items_dict[item] > num_most_stock:
				num_most_stock = item
		return most_stock
	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)
		self.warehouseitem1 = Warehouse([self.item1, self.item2, self.item3])
		self.warehouseitem2 = Warehouse([self.item2, self.item3, self.item4])

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("sentence here"), 0, "sentence with no a's" )
		self.assertEqual(count_a("", 0, "Testing an empty string"))
		self.assertEqual(count_a("a is in this 3 times a a"), 0, "Testing my own sentece with 3 a's")
		self.assertEqual(count_a(self.item5.name, 2 ,"Testing CocaCola"))

		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.warehouseitem1.add_item(self.item4)
		self.assertEqual(len(self.warehouseitem1.items), 4)
		self.warehouseitem2.add_item(self.item1)
		self.warehouseitem2.add_item(self.item5)
		self.assertEqual(len(self.warehouseitem2.items), 5)

		pass


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.warehouseitem1.get_max_stock()
		self.assertEqual(self.warehouseitem1.stock, 60)


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.warehouseitem2.get_max_price()
		self.assertEqual(self.warehouseitem2.get_max_price(), 6)
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()