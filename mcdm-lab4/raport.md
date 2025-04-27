# MCDM Analysis Report

## Project Overview

This project demonstrates the use of Multi-Criteria Decision Making (MCDM) to select the best laptop based on four criteria:
- **Price**: Minimize
- **Battery Life**: Maximize
- **Performance (Benchmark)**: Maximize
- **Weight**: Minimize

Two methods are used for ranking the alternatives:
1. **TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution)
2. **SPOTIS** (Stable Preference Ordering Towards Ideal Solution)

## Data

The decision matrix for three laptops is given below:

| Laptop | Price (PLN) | Battery Life (h) | Performance (points) | Weight (kg) |
|:------:|:-----------:|:-----------------:|:---------------------:|:----------:|
| A      | 4000        | 8                 | 2500                  | 1.8        |
| B      | 4500        | 10                | 2300                  | 2.0        |
| C      | 4200        | 7                 | 2700                  | 1.6        |

### Weights for criteria:
- Price: 0.3
- Battery Life: 0.2
- Performance: 0.4
- Weight: 0.1

### Criterion Types:
- Price: Minimize
- Battery Life: Maximize
- Performance: Maximize
- Weight: Minimize

## Methods Used

### 1. **TOPSIS**

The **TOPSIS** method was used to rank the laptops based on their closeness to the ideal solution. This method requires normalization of the decision matrix, which is done automatically by the `pymcdm` library.

### 2. **SPOTIS**

The **SPOTIS** method was also applied. It uses the bounds for each criterion, which were defined as follows:

- Price: [3000, 5000]
- Battery Life: [6, 12]
- Performance: [2000, 3000]
- Weight: [1.5, 2.2]

### Normalization
Both methods handle normalization internally and do not require the user to manually normalize the decision matrix.

## Results

### Rankings:

- **TOPSIS Ranking**: [3, 2, 1] (Laptop C is ranked the highest)
- **SPOTIS Ranking**: [3, 2, 1] (Laptop C is ranked the highest)

### Best Laptop according to each method:
- **TOPSIS**: Laptop C
- **SPOTIS**: Laptop C

## Conclusion

Based on the analysis using both **TOPSIS** and **SPOTIS**, **Laptop C** is the best option, as it ranked the highest in both methods. The key factors influencing this result are the balance of price, battery life, performance, and weight.

This analysis highlights the power of MCDM methods for making informed decisions in scenarios where multiple criteria must be considered.

---

This concludes the report for the analysis using **pymcdm** library for Multi-Criteria Decision Making.


