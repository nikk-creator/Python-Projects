import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

#1. sample dataset 
X=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y=np.array([[30000],[40000],[50000],[60000],[65000],[70000],[75000],[80000],[90000],[100000]])

#2.split the data 
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2,random_state=42)

#3.create and train model
model=LinearRegression()
model.fit(X_train,y_train)

#4.check model
print(f"slope(m):{model.coef_[0]}")
print(f"intercept(c):{model.intercept_}")
print(f"accuracy(r2 score):{model.score(X_test,y_test)*100:.2f}%")

#5.predict new value 
exp=12
predicted_salary=model.predict([[exp]])
print(f"Predicted salary for {exp} years experience: {predicted_salary[0][0]:.2f}")
#plot the line
plt.scatter(X,y, color='blue',label="Actual Data")
plt.plot(X,model.predict(X),color='red',label=' Regression line')
plt.xlabel("years of experience")
plt.ylabel("salary")
plt.title("Linear Regression")
plt.legend()
plt.show()