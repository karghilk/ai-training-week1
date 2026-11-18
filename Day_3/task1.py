import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

print(marks)
print("Shape:", marks.shape)



print("Dtype:", marks.dtype)
print("Size:", marks.size)

# Slicing
print("First two students:\n", marks[:2])
print("Last subject:", marks[:, -1])
print("Last subject for first two students:", marks[:2, -1])

# Averages and totals
print("Student averages:", np.round(marks.mean(axis=1), 2))
print("Subject averages:", np.round(marks.mean(axis=0), 2))
print("Student totals:", marks.sum(axis=1))

# Broadcasting
print("Marks after adding 5:\n", marks + 5)

# Weighted scores using original marks
weights = np.array([0.3, 0.3, 0.4])
print("Weighted scores:", np.round(np.dot(marks, weights), 2))

# Reshaping
print("Reshaped array:\n", np.arange(12).reshape(3, 4))