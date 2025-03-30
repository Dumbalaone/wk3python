def calculate_discount(price, discount_percent):
     result = price - (price * discount_percent/100)
     if    discount_percent >= 20:
        return result
     else:
          return price
      
price = float(input("Enter original price: "))
discount_percent = float(input("Enter percentage discount: "))
final_price = calculate_discount(price, discount_percent)
print(f'Original price:{price}')#print results:
print(f'Discount percent:{discount_percent}%')
print(f'Final price: {final_price}')
