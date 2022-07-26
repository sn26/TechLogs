from library_client.api import LogImgGenerator 
from library_client.api import ClientRequestSender 
import os


class ClientService: 

    def __init__(self, host, path ):
        self.clr_sender = ClientRequestSender(host)
        self.log_img_gen = LogImgGenerator( )
        self.path = path

        return

    def check_log(self ): 
        if os.path.isdir(self.path):
            return self.get_responses_from_all_logs_directory()
        elif os.path.isfile(self.path): 
            return self.get_responses_from_one_log(self.path)
       
        return "ERROR: Incorrect File Format"

    #Getting results from a given dir 
    def get_responses_from_all_logs_directory(self):
        return self.log_img_gen.get_attack_type_from_all_files_from_given_directory(self.path, self.clr_sender)

    #Function that get the results of the attack type from one file 
    def get_responses_from_one_log(self, path_file): 
        return self.log_img_gen.read_one_file(path_file , self.clr_sender )


    