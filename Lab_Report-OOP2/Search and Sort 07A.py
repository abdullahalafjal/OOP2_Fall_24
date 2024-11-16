import numpy as np

scores = np.array([95, 76, 45, 100, 90, 67, 80, 50, 75, 63])

specific_scores = [75, 90]

print("Specific Scores:")
for i in specific_scores:
    indices = np.where(scores == i)
    if indices[0].size > 0:
        print(f"Score {i} found at index {indices[0][0]}.")
    else:
        print(f"Score {i} not found in the array.")    

ascending_score = np.sort(scores)
descending_score = np.sort(scores)[::-1]

print(f"Ascending Order: {ascending_score}")
print(f"Descending Order: {descending_score}")

