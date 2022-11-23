name = 'Lucas'
print(name)

price = "$49.99"

if price.startswith("$"):
    price_amount = price[1:]
    print(price_amount)
else:
    print("ops error")
