# Predict
import numpy as np
from scipy.stats import gaussian_kde

def predict_range(data, last_num, k):
    if len(data) < k:
        return "Error: data size must be at least k."
    
    # Compute the threshold value using the last k values in the data
    thresholds = []
    for i in range(len(data)-k, len(data)):
        thresholds.append(abs(data[i]-data[i-1]))
    threshold_value = sum(thresholds) / len(thresholds)

    # Determine the range of the next number based on the threshold value
    next_range = None
    for i in range(len(thresholds)):
        if thresholds[i] <= threshold_value and data[-k+i] > last_num:
            next_range = (last_num, data[-k+i])
            break
    if next_range is None:
        #next_range = (last_num, 100.0)  # or any other upper limit you prefer
        next_range = (last_num, float('inf'))
    
    return next_range
# Example usage
data = [3.08, 1.74, 1.00, 2.99, 4.95, 1.31, 6.33, 1.08, 5.64, 1.94, 1.14, 2.26, 
        1.64, 3.45, 1.00, 7.96, 26.95, 1.48, 1.31, 1.06, 23.12, 2.13, 1.33, 1.29,
        9.67, 1.53, 14.39, 1.23, 8.07, 5.63, 1.80, 1.14, 1.01, 1.39, 2.39, 9.27,
        1.13, 27.18, 1.30, 57.50, 1.11, 1.07, 20.83, 2.10, 1.00, 6.65, 5.85, 4.22,
        2.35, 1.49, 1.50, 1.27, 3.85, 13.64, 3.16, 1.79, 1.24, 2.47, 2.51, 12.11,
        1.01, 1.81, 1.19, 1.49, 1.65, 1.28, 1.00, 1.00, 1.51, 10.12, 1.81, 2.69,
        3.19, 1.26, 3.04, 1.00, 1.01, 1.13, 1.43, 4.46, 39.28, 1.34, 1.96, 2.87,
        53.23, 7.43, 2.02, 1.09, 2.16, 3.93, 11.57, 3.28, 3.80, 4.19, 2.14, 27.83,
        1.12, 2.90, 1.41, 2.81, 1.11, 2.28, 5.98, 1.29, 4.84, 3.12, 2.95, 4.03,
        1.21, 1.04, 8.32, 1.02, 3.53, 1.40, 1.07, 2.14, 1.55, 1.46, 13.57, 2.45,
        3.86, 1.05, 3.63, 2.77, 12.69, 1.24, 1.65, 1.59, 3.55, 1.29, 2.96, 7.11,
        9.30, 15.43, 1.40, 2.67, 1.09, 25.42, 10.71, 1.08, 1.16, 1.22, 1.46, 2.80,
        3.72, 3.46, 6.13, 1.19, 37.03, 1.28, 1.17, 1.69, 1.07, 1.35, 4.39, 14.45,
        2.51, 6.35, 44.38, 3.90, 1.18, 1.14, 2.12, 4.72, 1.23, 4.24, 1.17, 1.82,
        1.20, 1.53, 1.08, 1.64, 1.69, 1.65, 1.05, 3.35, 1.89, 16.34, 2.81, 7.22,
        4.22, 4.64, 1.26, 1.95, 2.60, 1.14, 5.55, 4.72, 11.66, 8.31, 2.17, 1.14,
        1.00, 129.56, 1.23, 1.99, 4.63, 1.34, 32.74, 1.35, 2.01, 1.09, 3.48, 4.56,
        4.61, 1.34, 2.02, 1.71, 1.91, 1.07, 1.00]# Example data

last_num = 1.91 # Example last number
k = len(data) # Example k value
next_range = predict_range(data, last_num, k)
print("Predicted range:", next_range)