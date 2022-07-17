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

df = pd.read_csv("kia40_dataframe5n.csv").sort_values(by=['hadzanie'])
df2 = pd.read_csv("kia40_dataframe5s.csv").sort_values(by=['hadzanie'])
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
model.add(Dense(10, activation="relu", input_shape=[X_train.shape[1]]))
model.add(GaussianNoise(5))
#model.add(Dense(4, activation="relu"))
model.add(Dropout(0.20))
model.add(Dense(5, activation="relu", input_shape=[X_train.shape[1]]))
#model.add(GaussianNoise(2))
model.add(Dense(1, activation="relu"))

model.summary()
  
optimizer = keras.optimizers.adam(lr=0.03, decay=5e-6)
#optimizer = tf.keras.optimizers.RMSprop(0.0099)#RMSprop(0.0099)


model.compile(loss='mean_squared_error',optimizer=optimizer)
#model.compile(loss='mean_absolute_error',optimizer=optimizer)
#model.compile(loss='binary_crossentropy',optimizer=optimizer)

 #odtialto to dopasuvavam
#print(X_train.shape)
#X_train = np.expand_dims(X_train, axis=2)
print(X_train.shape)
#Y_train = np.expand_dims(Y_train, axis=2)
#print(Y_train.shape)
# %%
#X_train = np.expand_dims(X_train, axis=2)
#Y_train = np.expand_dims(Y_train, axis=2)
model.fit(X_train,Y_train,epochs=2000)

model.summary()

# %%
plt.close('all')

# %%
plt.figure(figsize=(8,6))
y_predtrain = model.predict(X_train)

plt.scatter(x=Y_train, y=y_predtrain, label=u'trenovacia') #c=df_train['hadzanie']
plt.ylabel("actual")
plt.xlabel("predict")
plt.show()

#X_test = np.expand_dims(X_test, axis=2) # zvacsit rozmer pre vstup CNN ..!

y_predtest = model.predict(X_test)

plt.scatter(x=Y_test, y=y_predtest, label=u'testovacia') #c=df_test['hadzanie']
plt.ylabel("actual")
plt.xlabel("predict")
plt.legend()    
plt.show()

print('Accuracy',mean_squared_error(Y_test,y_predtest))

# %%
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
y_predtest = classifier.predict(X_pcatest[:,1:])
plt.scatter(y=Y_test, x=y_predtest, c=df_test['hadzanie'])
plt.ylabel("actual")
plt.xlabel("predict")
plt.show()
print('Presnosť na testovacej množine (',len(y_pred),'položiek ) je ',mean_squared_error(Y_test,y_pred))

plt.figure()
y_predtrain = classifier.predict(X_pca[:,1:])
plt.scatter(y=Y_train, x=y_predtrain, c=df_train['hadzanie'])
plt.ylabel("actual")
plt.xlabel("predict")
plt.show()
print('Presnosť na trénovacej množine (',len(y_pred),'položiek ) je ',mean_squared_error(Y_train,y_pred))

# %%
def quantile_loss(q, y_p, y):
        e = y_p-y
        
        return tf.keras.backend.mean(tf.keras.backend.maximum(q*e, (q-1)*e))
import keras.backend as K  
 
X_train_blur = X_train.T.rolling(10).mean().T.fillna(0)
X_test_blur = X_test.T.rolling(10).mean().T.fillna(0)

print('X_train:', X_train.shape)
print('X_test:', X_test.shape)
print('X_train_blur:', X_train_blur.shape)
print('X_test_blur:', X_test_blur.shape)
    
model.trainable = True
for layer in model.layers[:1]:
        layer.trainable = 0
model.compile(loss='mean_squared_error',optimizer=optimizer)
model.summary()

# %%

def tilted_loss(q,y,f):
    e = (y-f)
    return K.mean(K.maximum(q*e, (q-1)*e), axis=-1)

def mcycleModel():
    model = Sequential()
    model.add(Dense(10, activation="relu", input_shape=[X_train_blur.shape[1]]))
    #model.add(GaussianNoise(0.2))
    model.add(Dense(10, activation="relu"))
    model.add(Dropout(0.20))
    #model.add(GaussianNoise(2))
    model.add(Dense(1, activation="relu"))
    return model

q = [0.1, 0.5, 0.9]

#model = mcycleModel()
model.compile(loss=lambda y,f: tilted_loss(q[0],y,f), optimizer='adadelta')
model.fit(X_train_blur, Y_train, epochs=50)
y_lower = model.predict(X_test_blur)

model.compile(loss=lambda y,f: tilted_loss(q[1],y,f), optimizer='adadelta')
model.fit(X_train_blur, Y_train, epochs=50)
y_predict = model.predict(X_test_blur)

model.compile(loss=lambda y,f: tilted_loss(q[2],y,f), optimizer='adadelta')
model.fit(X_train_blur, Y_train, epochs=50)
y_upper = model.predict(X_test_blur)


# %%
plt.figure()

#plt.scatter(x=Y_test, y=y_predict, label=q) # plot out this quantile
plt.plot(Y_test, Y_test, 'b.', markersize=10, label=u'Skutočné hodnoty')
plt.plot(Y_test, y_predict, 'r.', label=u'Predpovedané hodnoty')
plt.plot(Y_test, y_upper, 'k-')
plt.plot(Y_test, y_lower, 'k-')
plt.fill(np.concatenate([Y_test, Y_test[::-1]]),
         np.concatenate([y_upper, y_lower[::-1]]),
         alpha=.5, fc='b', ec='None', label='predpoveď 80% intervalu')
plt.ylabel("predpovedaná")
plt.xlabel("skutočná")

plt.legend()    
plt.show()
# %%
# %%