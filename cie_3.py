# -*- coding: utf-8 -*-
"""cie 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_q1ek6e-liPOALxJzLC5-iKYpvyPnvRZ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data= fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['PRICE'] = data.target
print (df)

df.describe()

df.shape

df.info

df.isnull().sum()

x = df.drop('PRICE', axis=1)
y = df['PRICE']
x
y

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
x_train
y_train

md=LinearRegression()
md.fit(x_train,y_train)
LinearRegression()
yprd=md.predict(x_test)
yprd

mse=mean_squared_error(y_test,yprd)
mse

rscore=r2_score(y_test,yprd)
rscore

