def calculate_discount(price, discount_percent):
     result = price - (price * discount_percent/100)
     if    discount_percent >= 20:
        return result
     else:
          return price
print(calculate_discount(1000,30))
