from keras import layers, models

def mlp1(input_shape):
  model = models.Sequential(name='MLP1')
  model.add(layers.Flatten(input_shape=input_shape))
  model.add(layers.Dropout(0.20))
  model.add(layers.Dense(512, activation = 'relu', use_bias = True, kernel_initializer = 'he_uniform'))
  model.add(layers.Dropout(0.10))
  model.add(layers.Dense(10, activation = 'softmax', use_bias = True, kernel_initializer = 'he_uniform'))
  return model
