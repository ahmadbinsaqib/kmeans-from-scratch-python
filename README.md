# K-Means From Scratch (Python)

A from-scratch implementation of the **K-Means clustering** algorithm for **two-dimensional (x, y)** data points.  
This project focuses on the core K-Means loop: **initial centroid selection**, **distance-based assignment**, **centroid recomputation (mean)**, and **convergence detection** — without using any external machine-learning libraries.

---

## Features

- Accepts **10–100** two-dimensional data points via console input  
- User selects number of clusters **k (1 ≤ k ≤ 5)**  
- Initial centroids are selected as the **first k data points**  
- Uses **squared Euclidean distance** (no square roots required)  
- Iterates until:
  - **30 iterations** are reached, or  
  - **no cluster assignments change** (convergence)  
- Handles **empty clusters** by keeping the centroid unchanged  

---

## Algorithm Overview

K-Means repeatedly performs two steps:

### 1. Assignment Step
For each data point, the squared distance to each centroid is computed:

\[
d^2 = (C_x - x)^2 + (C_y - y)^2
\]

The point is assigned to the cluster with the **smallest distance**.

### 2. Update Step
For each cluster, the centroid is recomputed as the **mean** of all points assigned to that cluster:

\[
\mu_x = \frac{\sum x}{\text{count}}, \quad
\mu_y = \frac{\sum y}{\text{count}}
\]

The new centroid replaces the old one, and the process repeats.

---

## Time and Space Complexity

Let:
- **N** = number of data points (10–100)  
- **k** = number of clusters (1–5)  
- **I** = number of iterations (≤ 30)  

### Time Complexity
- Assignment step: **O(Nk)**  
- Update step: **O(N + k)**  
- Total runtime: **O(I · N · k)** → effectively **O(Nk)** for this project  

### Space Complexity
- Data points, assignments, and centroid accumulators: **O(N + k)**  

---

## Project Structure

```text
.
├── kmeans.py
└── README.md
