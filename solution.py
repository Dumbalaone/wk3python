def calculate_discount(price, discount_percent):
     result = price - (price * discount_percent/100)
     if    discount_percent >= 20:
        return result #returns original price after applied discount
     else:
          return price #returns the original price
final_price =calculate_discount(price=1000,discount_percent=40)
print('finalprice after discount:',final_price)
