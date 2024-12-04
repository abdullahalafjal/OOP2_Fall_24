import numpy as np

Score = [85, 90, 78, 92, 88]

# a) Convert the data type into float
score_array = np.array(Score, dtype=float)
print("Score as float:", score_array)

# b) Create a copy of 'score' named 'a_score' and add 5 prints on it
a_score = score_array.copy()

# Adding 5 prints
print("Original Score:", Score)
print("a_score (Copy of Score):", a_score)

# Adding 5 to each element in 'a_score'
a_score += 5
print("a_score after adding 5:", a_score)

# c) Find shape, ndim, size, itemsize, dtype, and sort
print("Shape of a_score:", a_score.shape)
print("Number of dimensions (ndim):", a_score.ndim)
print("Size of a_score:", a_score.size)
print("Itemsize of a_score:", a_score.itemsize)
print("Datatype of a_score:", a_score.dtype)

# Sorting the array
a_score.sort()
print("Sorted a_score:", a_score)

# d) Find the index of who got 80+
indices = np.where(a_score >= 80)
print("Indices of students who got 80+: ", indices)

# e) Find min, max, std, var, sum, mean, axis wise mean
print("Min:", a_score.min())
print("Max:", a_score.max())
print("Standard Deviation:", a_score.std())
print("Variance:", a_score.var())
print("Sum:", a_score.sum())
print("Mean:", a_score.mean())


print("Axis-wise Mean (same for 1D array):", a_score.mean(axis=0))

# f) Print Score [::2], Score[-3:-1], and Score[1:4]
print("Score [::2]:", score_array[::2])
print("Score [-3:-1]:", score_array[-3:-1])
print("Score [1:4]:", score_array[1:4])
