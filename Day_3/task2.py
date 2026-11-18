import pandas as pd
import numpy as np

# 1. Create employees.csv
data = """id,name,department,salary,city
1,Arun,Sales,30000,Chennai
2,Priya,HR,45000,Chennai
3,Rahul,IT,60000,Bangalore
4,Divya,IT,75000,Chennai
5,Karthik,Finance,90000,Mumbai
6,Meena,Sales,52000,Bangalore
7,Suresh,IT,68000,Chennai
8,Anitha,HR,48000,Mumbai
"""

with open("employees.csv", "w", encoding="utf-8") as file:
    file.write(data)

# 2. Load the CSV into a DataFrame
df = pd.read_csv("employees.csv")

# 3. Explore the DataFrame
print("First five rows:")
print(df.head())

print("\nDataFrame information:")
df.info()

print("\nNumeric summary:")
print(df.describe())

# 4. Select columns
print("\nName column:")
print(df["name"])

print("\nName and salary columns:")
print(df[["name", "salary"]])

# 5. Select using loc and iloc
chennai_names = df.loc[df["city"] == "Chennai", "name"]
print("\nChennai:", ", ".join(chennai_names))

print("\nFirst three rows, name and department columns:")
print(df.iloc[0:3, 1:3])

# 6. Filter employees and print counts
high_salary = df[df["salary"] > 50000]
print("\nEmployees with salary above 50000:")
print(high_salary)
print(f"Salary above 50000: {len(high_salary)} employees")

it_employees = df[df["department"] == "IT"]
print("\nIT department:", ", ".join(it_employees["name"]))
print(f"IT department count: {len(it_employees)} employees")

# Bonus: Reshape 24 values into a 2 × 3 × 4 array
array_1d = np.arange(1, 25)
array_3d = array_1d.reshape(2, 3, 4)

print("\nReshaped array:")
print(array_3d)
print("Array shape:", array_3d.shape)

for index, array_slice in enumerate(array_3d):
    print(f"Axis 0 slice {index} shape: {array_slice.shape}")