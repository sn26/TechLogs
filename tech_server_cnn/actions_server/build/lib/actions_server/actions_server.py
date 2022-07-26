import argparse


def main(): 
    try: 
        args = parse_args()
        script_main_function( args)
    except Exception as e: 
        print(e)
        print("ERROR: Error Initializing the service")

def script_main_function(args): 
    from library_server.model import ModelWeights
    ModelWeights.set_weights(args.cnn_weights_path)
    from library_server.service import ServerEndpoint 
    serverService = serverEndpoint( )
    return
    

#Function to get the entrance arguments from the client
def parse_args(): 
   
    parser = argparse.ArgumentParser()
    parser.add_argument("-cwp", "--cnn-weights-path", action='store', required=True,
                        help="Path where weights are stored. Required")  
    return parser.parse_args()

if __name__ == "__main__":
    main()
