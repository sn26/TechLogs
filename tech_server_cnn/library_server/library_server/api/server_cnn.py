#FOR READING AN IMAGE
from PIL import Image
import json
import numpy as np 
from tensorflow import keras
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img
from tensorflow.keras.models import Sequential
import os
from library_server.api import ImgTooler

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""
#SOCKETS?


from skimage import exposure


#Clase para manejar los logs
class ServerCnn: 
  
  def __init__(self, weights_path, model ):
    #seteamos el modelo que vamos a usar
    self.model_tr = model 
    #Initializing the model
    self.model_tr.model = self.model_tr.model_cp(["relu", "relu", "relu", "relu", "softmax"])
    self.model_tr.load_model_weights(weights_path)
    self.img_tooler = ImgTooler()
    self.labels = {
      "0" : 'buffer_of', 
      "1": 'bwget', 
      "2": 'normal',
      "3": 'traversal'
    }
    return
   
  def set_pred_val(self, res ):
    max = 0 
    lab = 0
    for i in range(0 , len(res)):
      print(res[i])
      print(type(res[i]))
      if max < res[i]: 
        max = res[i]
        lab = i 
    return self.labels[lab]

  #Getting the y val
  def get_predict(self, X):
    return self.model_tr.get_model().predict(X)

  
  #Function to get the predicition of an image
  def get(self, args ):
    X = self.img_tooler.load_image_data(args['data_img'])
    X = X.reshape(-1, self.img_tooler.img_rows , self.img_tooler.img_cols, 3)
    print( self.get_predict(X)[0])
    output = { 'prediction' : self.labels[str( self.get_predict(X).argmax(axis=1)[0] )], 
              'data_img' :  str(args['data_img'])}
    return output
     
      
