# 28-5-24
import pandas as pd
data = {
    "name" : ['Surya','Nandana','Sarjitha'],
    "age" : [24,23,30],
    "place" : ["tvm","tvm","tvm"]
    }
df = pd.DataFrame(data)
# print(df)
# print(df[["name","place"]])
# print(df.iloc[1])
# print(df[df["age"] > 23])

df["stipend"] = [3000,3000,3000]

df = df.drop(columns=["age"])
print(df)
# statistical functions
print(df.describe())