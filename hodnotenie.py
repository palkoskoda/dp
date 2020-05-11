# Import potrebných balíčkov
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, KBinsDiscretizer
from sklearn.compose import make_column_transformer
import matplotlib.pyplot as plt
import seaborn as sns

#príprava dát

df = pd.read_csv("kia40_dataframe5n.csv")
df2 = pd.read_csv("kia40_dataframe5s.csv")
#df=df.append(pd.read_csv("data/kia40_dataframe3n.csv"))
#df2=df2.append(pd.read_csv("data/kia40_dataframe3s.csv"))
#df=df.append(df2)
del df["value_1"]
del df2["value_1"]
df.head()

kbins = KBinsDiscretizer(10, encode='ordinal')
y_stratify = kbins.fit_transform(df[["hadzanie"]])
#df_train, df_test = train_test_split(df,test_size=0.3, random_state=4)
df_train=df
df_test=df2
df.columns

numeric_inputs = df.columns[3:]
output = ["hadzanie"]

input_preproc = StandardScaler()
output_preproc = StandardScaler()

X_train_raw = df_train[numeric_inputs]
Y_train_raw = df_train[output]

X_test_raw = df_test[numeric_inputs]
Y_test_raw = df_test[output]

#X_train = input_preproc.fit_transform(X_train_raw)
#X_test = input_preproc.transform(X_test_raw)

#Y_train = output_preproc.fit_transform(Y_train_raw)
#Y_test = output_preproc.transform(Y_test_raw)

X_train =X_train_raw
X_test =X_test_raw

Y_train = Y_train_raw
Y_test=Y_test_raw

import keras
from keras.models import Sequential
from keras.layers import Dropout, Conv1D
from keras.layers import GaussianNoise
from keras.layers import Dense, Input, Activation, Flatten
from keras.callbacks import Callback
from keras.models import Model
import tensorflow as tf

keras.backend.clear_session()
# Neural network
model = Sequential()
#model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(X_train.shape[1], 1)))
#model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
#model.add(Flatten()) #splostiii 2D/3D -> 1D ... 997*64 = 63808
model.add(Dense(100, activation="relu", input_shape=[X_train.shape[1]]))
#model.add(GaussianNoise(2))
model.add(Dense(10, activation="relu"))
model.add(Dropout(0.20))
#model.add(GaussianNoise(2))
model.add(Dense(1, activation="relu"))

model.summary()
  
optimizer = keras.optimizers.adam(lr=0.001, decay=1e-6)
#RMSprop(0.0099)


model.compile(loss='mean_squared_error',optimizer=optimizer)
#model.compile(loss='mean_absolute_error',optimizer=optimizer)
#model.compile(loss='binary_crossentropy',optimizer=optimizer)

 #odtialto to dopasuvavam
#print(X_train.shape)
#X_train = np.expand_dims(X_train, axis=2)
print(X_train.shape)
#Y_train = np.expand_dims(Y_train, axis=2)
#print(Y_train.shape)

#X_train = np.expand_dims(X_train, axis=2)
#Y_train = np.expand_dims(Y_train, axis=2)
model.fit(X_train,Y_train,epochs=50)

model.summary()

y_predict = model.predict(X_train)

# %%
plt.scatter(y=Y_train, x=y_predict, c=df_train['hadzanie'])
plt.ylabel("actual")
plt.xlabel("predict")
plt.show()

#X_test = np.expand_dims(X_test, axis=2) # zvacsit rozmer pre vstup CNN ..!

y_predict = model.predict(X_test)

plt.scatter(y=Y_test, x=y_predict, c=df_test['hadzanie'])
plt.ylabel("actual")
plt.xlabel("predict")
plt.show()

print('Accuracy',mean_squared_error(Y_test,y_predict))

from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
pca = PCA(n_components=3, whiten=True)
X_pca = pca.fit_transform(X_train)
X_pcatest = pca.transform(X_test)

print('Original number of features:', X_train.shape)
print('Reduced number of features:', X_pca.shape)

plt.figure(figsize=(8,6))
plt.scatter(X_pca[:,1], X_pca[:,1], c=df_train['hadzanie'])
plt.show()
#1. - 399
#2. - 166
#plt.bar(pd.DataFrame(pca.components_,columns=X_train.columns,index = ['PC-1','PC-2','PC-3']))

#plt.plot(pca.components_[1,])

explained_variance = pca.explained_variance_ratio_

classifier = RandomForestClassifier(max_depth=3, random_state=0)
classifier.fit(X_pca[:,1:], Y_train)

plt.figure()
y_pred = classifier.predict(X_pcatest[:,1:])
plt.scatter(y=Y_test, x=y_pred, c=df_test['hadzanie'])
plt.ylabel("actual")
plt.xlabel("predict")
plt.show()
print('Presnosť na testovacej množine (',len(y_pred),'položiek ) je ',mean_squared_error(Y_test,y_pred))

plt.figure()
y_pred = classifier.predict(X_pca[:,1:])
plt.scatter(y=Y_train, x=y_pred, c=df_train['hadzanie'])
plt.ylabel("actual")
plt.xlabel("predict")
plt.show()
print('Presnosť na trénovacej množine (',len(y_pred),'položiek ) je ',mean_squared_error(Y_train,y_pred))

