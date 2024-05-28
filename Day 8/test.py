import pandas as pd
data = pd.read_csv("data.csv")
df_clean = data.dropna(how="all")
df_clean_col = df_clean.dropna(axis=1,how="all")
# print(df_clean_col)
df_filled = data.fillna(0)
print(df_filled)