import numpy as np
from scipy.stats import ttest_ind

# Test scores of two groups
traditional_method = [50, 60, 70, 75, 80, 85, 70]
new_method = [70, 80, 82, 78, 88, 92, 85]

# Perform two-sample T-test
t_stat, p_value = ttest_ind(traditional_method, new_method)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Significance level
alpha = 0.1

# Conclusion
if p_value < alpha:
    print("Reject the null hypothesis: The new teaching method is more effective.")
else:
    print("Fail to reject the null hypothesis: The new teaching method is not more effective.")

