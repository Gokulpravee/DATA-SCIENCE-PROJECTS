#importing libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, find_peaks_cwt


#load csv file
df = pd.read_csv(r"C:\Users\Gokul\OneDrive\Desktop\code1\1 (2) (2).csv",sep = ",")
df.head()


#slice a data
a = df[3:]['average(A)']
print(a)


#ravel the values
a1 = a.values.ravel()
print(a1)


#convert the values into float type
a2 = a1.astype(float)
print(a2)


##plot the data
##plt.plot(a2)
##plt.show()


##start = 14000
##end = 600000
##removed_data = a2[start:end]
##removed_data
##plt.plot(removed_data)
##plt.show()

#signal and peaks 1
start_1 = 11000
end_1 = 50000
sliced_data = a2[start_1:end_1]

print(sliced_data)

#thrsh and height
thresh = 0.09
height = 2.5

#find peaks
peak_idx_1, _ = find_peaks(sliced_data, height = 2.5, distance = 1000)

###plotting the peaks
##plt.plot(sliced_data)
##plt.plot(peak_idx_1, sliced_data[peak_idx_1], 'r.')
##plt.show()


#signal and peaks 2
start_2 = 72000
end_2 = 82000
num_data = a2[start_2:end_2]

print(num_data)

#thresh and height
thresh = 0.09
height = 1.7

#find peaks
peak_idx_2, _ = find_peaks(num_data, height = 1.7, distance = 1000)

###plotting the peaks
##plt.plot(num_data)
##plt.plot(peak_idx_2, num_data[peak_idx_2], 'r.')
##plt.show()


#signal and peaks 3
start_3 = 140000
end_3 = 170000
new_value = a2[start_3:end_3]
print(new_value)

#thresh and height
thresh = 0.09
height = 0.7

#find peaks
peak_idx_3, _ = find_peaks(new_value, height = 0.7, distance = 1000)

###plotting the peaks
##plt.plot(new_value)
##plt.plot(peak_idx_3, new_value[peak_idx_3], 'r.')
##plt.show()


#signal and peaks 4
start_4 = 226000
end_4 = 236000
aaa_data = a2[start_4:end_4]
print(aaa_data)

#thresh and height
thresh = 0.09
height = 0.4

#find peaks 4
peak_idx_4, _ = find_peaks(aaa_data, height = 0.4, distance = 1000)

###plotting the peaks
##plt.plot(aaa_data)
##plt.plot(peak_idx_4, aaa_data[peak_idx_4], 'r.')
##plt.show()


#signal and peaks 5
start_5 = 295000
end_5 = 320000
abc_data = a2[start_5:end_5]
print(abc_data)

#thresh and height
thresh = 0.09
height = 0.25

#find peaks
peak_idx_5, _ = find_peaks(abc_data, height = 0.25, distance = 1000)

###plotting the peaks
##plt.plot(abc_data)
##plt.plot(peak_idx_5, abc_data[peak_idx_5], 'r.')
##plt.show()
## 

plt.plot(a2)
plt.plot(peak_idx_1 + start_1 ,sliced_data[peak_idx_1], 'r.')
plt.plot(peak_idx_2 + start_2 ,num_data[peak_idx_2], 'r.')
plt.plot(peak_idx_3 + start_3 ,new_value[peak_idx_3], 'r.')
plt.plot(peak_idx_4 + start_4 ,aaa_data[peak_idx_4], 'r.')
plt.plot(peak_idx_5 + start_5, abc_data[peak_idx_5], 'r.')
plt.show()


