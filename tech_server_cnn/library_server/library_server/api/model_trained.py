from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Activation, Input, Flatten, MaxPooling2D
from keras.layers.convolutional import Conv2D


class ModelTrained:
  
  def __init__(self):
    self.num_classes = 4
    self.model = None
  
  def get_model(self):
    return self.model

  def load_model_weights(self , wg):
    print("READING WEIGHTS...")
    self.model.load_weights(wg)
    return self.model

  #Modelo que vamos a usar para la red
  def model_cp(self ,  activation_functions ): 
    v = Input(shape=(32,32,3),name='img')
    #FIRST BRANCH
    conv = Conv2D(50,(5,5), padding='same')(v)
    activation_layer_1 = Activation(activation_functions[0])(conv)
    max_pooling_2d_1 = MaxPooling2D(pool_size=(2,2))(activation_layer_1)
    #SECOND BRANCH
    conv2 = Conv2D(90,(5,5), padding='valid')(max_pooling_2d_1)
    activation_layer_2 = Activation(activation_functions[1]) (conv2)
    max_pooling_2d_2 = MaxPooling2D(pool_size=(2,2)) (activation_layer_2)
    #THIRD BRANCH
    conv3 = Conv2D(120,(1,1), padding='valid')(max_pooling_2d_2)
    activation_layer_3 = Activation(activation_functions[1]) (conv3)
    max_pooling_2d_3 = MaxPooling2D(pool_size=(2,2)) (activation_layer_3)
    flatten = Flatten()(max_pooling_2d_3)
    #FOURTH BRANCH
    layer_dense_1 = Dense(120)(flatten)
    activation_layer_3 = Activation(activation_functions[2]) (layer_dense_1 )
    #LAST BRANCH 
    layer_dense_2 = Dense(84)(activation_layer_3)
    activation_layer_4 = Activation(activation_functions[3]) (layer_dense_2)
    layer_dense_3 = Dense(4)(activation_layer_4)
    activation_layer_5 = Activation(activation_functions[4]) (layer_dense_3)
    return Model(inputs=v , outputs=activation_layer_5)


 