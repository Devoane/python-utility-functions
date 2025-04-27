import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.weights import entropy_weights as entropy

# Decision Matrix Definition: Rows represent alternatives (laptops), columns represent criteria
decision_matrix = np.array([
    [4000, 8, 2500, 1.8],  # Laptop A
    [4500, 10, 2300, 2.0],  # Laptop B
    [4200, 7, 2700, 1.6]    # Laptop C
])

# Weights for each criterion (must sum to 1)
weights = np.array([0.3, 0.2, 0.4, 0.1])  # Example values

# Criteria Types: 1 = maximize, -1 = minimize
criteria_types = np.array([-1, 1, 1, -1])

# Bounds for each criterion (min, max values)
bounds = np.array([
    [3000, 5000],  # Price (min, max)
    [6, 12],       # Battery life (min, max)
    [2000, 3000],  # Performance (min, max)
    [1.5, 2.2]     # Weight (min, max)
])

# TOPSIS Method
# TOPSIS will automatically handle normalization
topsis = TOPSIS()
topsis_ranking = topsis(decision_matrix, weights, criteria_types)

# SPOTIS Method
# SPOTIS requires the bounds for each criterion to perform the calculations
spotis = SPOTIS(bounds=bounds)
spotis_ranking = spotis(decision_matrix, weights, criteria_types)

# Displaying Results
print("TOPSIS Ranking:", topsis_ranking)
print("SPOTIS Ranking:", spotis_ranking)

# Best Laptop according to each method
best_topsis = np.argmax(topsis_ranking) + 1  # +1 because indexing starts from 0
best_spotis = np.argmin(spotis_ranking) + 1

print(f"\nBest laptop according to TOPSIS: Laptop {best_topsis}")
print(f"Best laptop according to SPOTIS: Laptop {best_spotis}")
