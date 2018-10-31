from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=100,activation='relu',input_dim=37))