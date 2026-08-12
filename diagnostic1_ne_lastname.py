def calculate_checkout(cart_total, shipping_speed):

    if shipping_speed == "standard" and cart_total>100:
        shipping_cost=0
    elif shipping_speed == "standard":
        shipping_cost=10
    elif shipping_speed == "express":
        shipping_cost=20
    elif shipping_speed == "overnight":
        shipping_cost=35
    else:
        print("Invalid Shopping Speed Inputed")

    final_bill = cart_total + shipping_cost
    return final_bill

print(calculate_checkout(120, "standard"))    