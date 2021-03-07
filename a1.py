'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''


def show_menu():
        print("=======================================================")
	print("                MY BAZZAR                              ")
	print("=======================================================")
	print("Hello! Welcome to my grocery store!                    ")
	print("Following are the products available in the store :    ")
	print(""
																 "")
	print("-------------------------------------------------------")
	print("Code   | Description  |  Category    | Cost (in Rupees)")
	print("  0    | T-shirt      | Apparel      | 500             ")
	print("  1    | Trousers     | Apparel      | 600             ")
	print("  2    | Scarf        | Apparel      | 250             ")
	print("  3    | Smartphone   | Electronics  | 20,000          ")
	print("  4    | iPad         | Electronics  | 30,000          ")
	print("  5    | Laptop       | Electronics  | 50,000          ")
	print("  6    | Eggs         | Eatables     | 5               ")
	print("  7    | Chocolate    | Eatables     | 10              ")
	print("  8    | Juice        | Eatables     | 100             ")
	print("  9    | Milk         | Eatables     | 45              ")
	print("-------------------------------------------------------")

def menu():
	items = [["Tshirt", 10], ["Trousers", 20], ["Scarf", 40], ["Smartphone", 20000], ["iPad", 30000], ["Laptop", 50000],
			 ["Eggs", 5], ["Chocolate", 10], ["Juice", 100], ["Milk", 45]]
	

def get_regular_input():
	'''
	Description: Takes space separated item codes (only integers allowed). 
	Include appropriate print statements to match the output with the 
	screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i. 
	'''
	pass # Remove this line when you write this function


def get_bulk_input():
	for i in range (0,10):
		
                user_input = input("Enter a two value: ")
                try:
                    x, y = user_input.split()
                    print("Your item Code: ", x)
                    print("Quantity: ", y)
                except:
		    print("Thank You for shopping")
                    break
	
	


def print_order_details(quantities):
	'''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: No return value
	'''
	pass # Remove this line when you write this function


def calculate_category_wise_cost(quantities):
	'''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: A 3-tuple of integers in the following format: 
	(apparels_cost, electronics_cost, eatables_cost)
	'''
	pass # Remove this line when you write this function


def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the discounted category-wise price, if applicable. 
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	
	Returns: A 3-tuple of integers in the following format: 
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
	'''
	pass # Remove this line when you write this function


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables' 
	
	Returns: A 2-tuple of integers in the following format: 
	(total_cost_including_tax, total_tax)
	'''
	pass # Remove this line when you write this function


def apply_coupon_code(total_cost):
	'''
	Description: Takes the coupon code from the user as input (case-sensitive). 
	For details, refer the PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: The total cost (integer) on which the coupon is to be applied.
	
	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
	'''
	pass # Remove this line when you write this function


def main():
	'''
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate 
	print statements to match the output with the screenshots provided in the PDF.
	
	Parameters: No parameters
	
	Returns: No return value
	'''
	pass # Remove this line when you write this function


if __name__ == '__main__':
	main()
