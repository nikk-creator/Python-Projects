#supervised learning algorithm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#1.Create sample dataset 
data={"Age":[22,27,47,52,46,56,55,60,62,38,40,45],
      "Salary":[15000,29000,48000,60000,52000,80000,85000,90000,95000,55000,60000,65000,],
      "Bought":[0,0,1,1,1,1,1,1,1,0,1,1]}
df=pd.DataFrame(data)

#2.Split into features(X), and label(y)
X=df[["Age","Salary"]]
y=df["Bought"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

#3.Train a model 
model=RandomForestClassifier(n_estimators=100)
model.fit(X_train,y_train)

#4.Evaluate
y_pred=model.predict(X_test)
print(f"Accuracy:{accuracy_score(y_test,y_pred)*100:.2f}%")

#5.predict new data
new_customer = pd.DataFrame([[30, 40000]], columns=['Age', 'Salary'])
prediction = model.predict(new_customer)[0]
print(f"prediction of age 30 and salary 40000:{'will buy' if prediction==1 else 'will not buy'}")