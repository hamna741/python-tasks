import numpy as np
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)
file_path = sys.argv[1]
data =np.loadtxt(file_path)
print("MEAN = ", np.mean(data))
print("MEDIAN = ", np.median(data))
print("MAXIMUM = ", np.max(data))
print("MINIMUM = ", np.min(data))
print("STANDARD DEVIATION = ", np.std(data))
print("99th PERCENTILE = ", np.percentile(data, 99))
print("99.9th PERCENTILE = ", np.percentile(data, 99.9))
print("99.99th PERCENTILE = ", np.percentile(data, 99.99))
print("99.999th PERCENTILE = ", np.percentile(data, 99.999))