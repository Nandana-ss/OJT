import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("data.csv")
# print(data.head())

x=data[['loan_id','loan_amount','interest_rate','term','income','credit_score','age','employment_length']]
y=data['loan_repaid']

x_train,x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)

model = DecisionTreeClassifier()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("accuracy: {accuracy:.2f}")
print("classification report:")
print(classification_report(y_test,y_pred))

# print("Confusion matrix:")
# print(confusion_matrix())
