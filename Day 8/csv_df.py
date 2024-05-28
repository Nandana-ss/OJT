import pandas as pd
data = pd.read_csv("data.csv",usecols=["Name","Age","place"],dtype={"Age":int,"salary":float})
print(data)