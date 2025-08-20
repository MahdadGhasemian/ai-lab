from sklearn.linear_model import LogisticRegression
import numpy as np

# Training data
X = np.array([[1], [2], [3], [6], [7], [8]])
y = np.array([0, 0, 0, 1, 1, 1])  # 0 = <5, 1 = >5

# Train model
model = LogisticRegression()
model.fit(X, y)

# Test
test_numbers = np.array([[2], [8], [6], [10], [4], [3]])
predictions = model.predict(test_numbers)

for num, pred in zip(test_numbers.flatten(), predictions):
    label = ">5" if pred == 1 else "<5"
    print(f"{num} → {label}")
