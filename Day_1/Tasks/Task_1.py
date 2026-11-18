
# =====================================
# WEEK 1 - DAY 1
# TASK 1: SALES REPORT BASICS
# =====================================

# 1. Python variables and data types

a = 100                  # Integer
b = 99.5                 # Float
c = "Python"             # String
d = [10, 20, 30]         # List
e = {"name": "Karghil", "age": 29}  # Dictionary
f = {10, 20, 30}         # Set
g = (10, 20, 30)         # Tuple

print("Integer:", a, type(a))
print("Float:", b, type(b))
print("String:", c, type(c))
print("List:", d, type(d))
print("Dictionary:", e, type(e))
print("Set:", f, type(f))
print("Tuple:", g, type(g))


# 2. Sales data

sales = [12000, 0, 8500, 15000, -200, 9800]

total = 0
target = 30000

# 3. Process sales using for loop

for x in sales:

    # Skip zero or negative sales
    if x <= 0:
        print("Skipped invalid value", x)
        continue

    # Add valid sales to total
    total = total + x

    print("Added", x, "total", total)

    # Stop when total exceeds target
    if total > target:
        break


# 4. Check whether target is reached

if total > target:
    print("Target reached. Stopped at", total)

elif total == target:
    print("Target reached exactly at", total)

else:
    print("Target not reached. Final total:", total)
