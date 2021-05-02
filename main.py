import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# data import
data = pd.read_csv("President_Heights.csv")
print(data)

# height extract this information
height = np.array(data["height(cm)"])
print(height)
print("\n")

# variety of summary statistics
print(f"Mean of President Heights: {height.mean()} cm")
print(f"Standard Deviation of President Heights: {height.std()}")
print(f"Maximum of President Heights: {height.max()}")
print(f"Minimum of President Heights: {height.min()}")

#
print("25th percentile =", np.percentile(height, 25))
print("Median =", np.median(height))
print("75th percentile =", np.percentile(height, 75))

#
sns.set()
plt.hist(height)
plt.title("Height Distribution of Presidents of USA")
plt.xlabel("height(cm)")
plt.ylabel("Number")
plt.show()