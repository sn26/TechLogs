from requests import get

#Class to send rquest to the cnn server 
class ClientRequestSender():
    
    def __init__(self , host):
        self.host = host
        return
    
    #Function that sends a requests to the server
    def send(self , data ): 
        print("ESTAMOS ENTRANDO EN LA REQUEST")
        print("LA DATA QUE LE ESTAMOS PASANDO ES ")
        print(data)
        prediction = get("http://" + self.host + ":5000/LogDetection", params={'data_img': data }).json()['prediction']
        return str(prediction)

        
