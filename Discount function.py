
def apply_discount(price, discount):
    # Check whether price is a number
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    # Check whether discount is a number
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    # Check whether price is positive
    if price <= 0:
        return "The price should be greater than 0"

    # Check whether discount is between 0 and 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    # Calculate the final price
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    return final_price


print(apply_discount('50', 0))
print(apply_discount(0, 8))
print(apply_discount(100, 101))
print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(50, 100))
print(apply_discount(74.5, 20.0))