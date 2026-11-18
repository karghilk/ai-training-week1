
# =========================================
# WEEK 1 - DAY 1
# TASK 2: FUNCTIONS AND COMPREHENSIONS
# =========================================

# Product prices
prices = [500, 1200, 800, 2500, 300]


# 1. Function with default parameter

def apply_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return float(final_price)


print("Discount 10%:", apply_discount(1000))
print("Discount 25%:", apply_discount(1000, 25))


# 2. Function using *args

def total(*args):
    return sum(args)


print("Total:", total(5, 10, 15))


# 3. Function using **kwargs

def describe(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


print("Product Description:")
describe(name="Laptop", price=50000, brand="Dell")


# 4. List comprehension
above_1000 = [price for price in prices if price > 1000]

print("Above 1000:", above_1000)


# 5. Map with lambda to add 18% GST

with_gst = list(map(lambda price: round(price * 1.18, 2), prices))

print("With GST:", with_gst)


# 6. Filter to keep prices below 1000

below_1000 = list(filter(lambda price: price < 1000, prices))

print("Below 1000:", below_1000)
