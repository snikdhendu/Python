import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate some example data points
n_samples = 300
n_features = 2
n_clusters = 3

# Create synthetic data with normal distributions
data, labels = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=42)

# Create and fit a K-means clustering model
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(data)

# Get cluster centers and labels
cluster_centers = kmeans.cluster_centers_
cluster_labels = kmeans.labels_

# Plot the data points and cluster centers
plt.scatter(data[:, 0], data[:, 1], c=cluster_labels, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='x', s=200, label='Cluster Centers')
plt.title('K-means Clustering')
plt.legend()
plt.show()
