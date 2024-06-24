import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# 1.Load the dataset from a CSV file named sample_dataset.csv into a Pandas DataFrame. Display the first few rows of the dataset.
data = pd.read_csv("sepal_data.csv")
print(data.head())

# 2.Generate summary statistics for this dataset. What are the mean and standard deviation of the Sepal Length?
print(data.describe())

# 3.Check for any missing values in the dataset. How would you handle them if there were any?
print("null values: ",data.isnull().sum())

# 4.Convert the species labels to numerical values using a mapping dictionary. For example, map 'FlowerA' to 0, 'FlowerB' to 1, and 'FlowerC' to 2.
species_mapping = {'FlowerA': 0, 'FlowerB': 1, 'FlowerC': 2}

data['Species'] = data['Species'].map(species_mapping)
print(data.head())
print(data.tail())

# 5.Split the dataset into training and testing sets with 70% training data and 30% testing data. Ensure that the split is stratified based on the species.
x = ['Sepal Length (cm)','Sepal Width (cm)','Petal Length (cm)','Petal Width (cm)']
y = ['Species']
x_train, x_test,y_train,y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# 6.Train a decision tree classifier on the training data. What parameters would you use for the decision tree?
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# 7.Visualize the trained decision tree.
import matplotlib.pyplot as plt
from sklearn import tree
plt.figure(figsize=(10,8))
tree.plot_tree(model, filled=True)
plt.show()

# 8.Predict the species for the testing data and compute the accuracy.
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
accuracy = model.accuracy_score(y_test,y_pred)
print("Accuracy:", accuracy)

# 9.Generate a classification report and a confusion matrix for the predictions.
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))