from library_server.api import ServerCnn
from library_server.api import ModelTrained
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from library_server.model import ModelWeights
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('data_img' )


  
class ServerEndpoint(Resource): 

    def __init__(self ) :
        self.model = ModelTrained() 
        self.srvCnn = ServerCnn(ModelWeights.weights, self.model  )
        return

    #Function that recieves an image and get the response from the model trained
    def get( self  ):
        try: 
            args =  parser.parse_args()
            print("LOS ARGUMENTOS DE ENTRADA SON ")
            print(args)
            return self.srvCnn.get( args)
        except Exception as e: 
            print(e)
            abort(404, message="ERROR: Input Image Error"   )


##
## Setting up the resource routing
api.add_resource(ServerEndpoint , '/LogDetection')
app.run( debug =True )

    