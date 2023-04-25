import numpy as np

# Load preprocessed data and labels
data = np.load('preprocessed_data.npz')
X, y = data['X'], data['y']

# Generate random permutation of indices
idx = np.random.permutation(len(X))

# Shuffle data and labels using the same permutation of indices
X_shuffled, y_shuffled = X[idx], y[idx]

np.savez('shuffle_data.npz', X=X_shuffled, y=y_shuffled)
