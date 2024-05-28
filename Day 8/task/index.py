import pandas as pd
# convert to dataframe
data = pd.read_csv("air-pollution.csv")

# Create fiters based on the country
filter_country = data[data['Code'] == 'ALB']
# print(filter_country)

# find mean, median, standard deviation for the respective columns and store into a new column
describe = data.describe()
# data["MEAN"] = describe["mean"]
print(describe)

# delete the depeated entries
df_clean = data.dropna(how="all")
df_clean_col = df_clean.dropna(axis=1,how="all")
print(df_clean_col)
# Change null values to 0
df_filled = data.fillna(0)
# print(df_filled)
filter_country = data[data['Entity'] == 'Africa']
print(filter_country)