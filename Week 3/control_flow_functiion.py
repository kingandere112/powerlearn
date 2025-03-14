def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display the result
final_price = calculate_discount(price, discount_percent)
print("Final Price:", final_price)