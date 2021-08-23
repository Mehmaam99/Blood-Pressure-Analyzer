from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
df = pd.read_csv("FinalData.csv")
df.head()

df.drop(['History','Patient','ControlledDiet','TakeMedication'], axis = 'columns', inplace=True)
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

df2=(df.apply(le.fit_transform))
target=df2['Stages']
inputs=df2.drop(['Stages'],axis='columns')

x_train, x_test, y_train, y_test = train_test_split(inputs,target,test_size=0.2)
from sklearn.linear_model import LogisticRegression

model=LogisticRegression()

model.fit(x_train,y_train)

print(model.score(x_test,y_test)*100)

y_pred = model.predict(x_test)
print(y_pred)


print(model.predict([[1,0,1,0,0,0,1,1,3]]))

import pickle
with open('model_pickle','wb') as file:
    pickle.dump(model,file)
    

with open('model_pickle','rb') as file:
    mp= pickle.load(file)
    

print(mp.score(x_test,y_test))

