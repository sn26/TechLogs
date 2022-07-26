import argparse
from library_client.services import ClientService

def main(): 
    try: 
        args = parse_args()
        script_main_function( args)
    except Exception as e: 
        print(e)
        print("ERROR: Error sending the request")

def script_main_function(args): 
    clsr = ClientService( args.server_host, args.image_path )
    return clsr.check_log()
    

#Function to get the entrance arguments from the client
def parse_args(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("-sh", "--server-host", action='store', required=True,
                        help="Server Host. Required")
    parser.add_argument("-imp", "--image-path", action='store', required=True,
                        help="Image path or Dir path. Required")
    
    return parser.parse_args( )

if __name__ == "__main__":
    main()
