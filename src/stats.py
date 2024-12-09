# Basic program to demonstrate statistics calculations like mean, median, mode, standard deviation, variance, etc. 
print("Stats basics program")

import statistics as spt

# data_set = [61,65,71,75,81,85]
data_set = [40, 50, 60, 70, 80, 90]


sorted_data_set = sorted(data_set)

print("Mean:", spt.mean(data_set))
print("Median:", spt.median(data_set))
print("Mode:", spt.mode(data_set))
print("Standard Deviation:", spt.stdev(data_set))
print("Variance:", spt.variance(data_set))
print("Range:", (sorted_data_set[-1] - sorted_data_set[0]))

# ------------------------------------------------
print("\nStats basics program using numpy\n")
import numpy as np

# Step 1: Generate a range of numbers
start = 10
stop = 50
step = 5
# range_of_numbers = np.arange(start, stop + step, step)
range_of_numbers = data_set
print("Range of Numbers:", range_of_numbers)

# Step 2: Calculate various statistical measures
mean_value = np.mean(range_of_numbers)
median_value = np.median(range_of_numbers)
# mode_value = np(range_of_numbers)  # Note: np.mode returns an array of modes and counts
std_deviation = np.std(range_of_numbers)
variance = np.var(range_of_numbers)

print("Mean:", mean_value)
print("Median:", median_value)
# print("Mode:", mode_value[0])  # Access the mode value from the result
print("Standard Deviation:", std_deviation)
print("Variance:", variance)