import numpy as np 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
    # Sample dataset ,
X = np.array([[2.5,2.4],[0.5,0.7],[2.2,2.9],[1.9,2.2],[3.1,3.0]])
    # Standardize the data,
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) 
pca = PCA(n_components=1)
X_pca = pca.fit_transform(X_scaled)
print("Reduced Data:", X_pca)