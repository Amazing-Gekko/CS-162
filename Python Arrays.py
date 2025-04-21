import numpy as np

# Generate a 5x5 array of random integers between 0 and 99
array = np.random.randint(0, 100, size=(5, 5))

# Print the entire array
print("Generated 5x5 Array:")
print(array)

# Print the number from the 2nd row, 3rd column (indexing starts at 0)
print("\nElement at 2nd row, 3rd column:")
print(array[1, 2])  # row 1 (2nd), column 2 (3rd)

# Print the sum of all the elements in the array
print("\nSum of all elements:")
print(np.sum(array))

# Print the mean of each row
print("\nMean of each row:")
print(np.mean(array, axis=1))

# Print the maximum value in each column
print("\nMaximum value in each column:")
print(np.max(array, axis=0))
