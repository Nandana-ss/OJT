# 28-5-24
import pandas as pd
# dict = {"name":"anu","mark":10}
# series = pd.Series(dict)
# print(series)
data = [10,45,65,5,6]
series = pd.Series(data)
print(series[3])
 
#arithematical operation
 
series_add = series + 10
 
print(series_add)
 
# filter elemnts in the series.
 
filtered_series = series[series > 20]
print(filtered_series)
 
 
#statical method
#data = [10,2,3,45,65]
 
mean = series.mean()
print (f"the mean value of the series is {mean}")