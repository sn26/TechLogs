import os
from glob import glob
from PIL import Image


class LogImgGenerator: 

    def __init__(self):
        return

    #Function that index all files from one path.
    def get_attack_type_from_all_files_from_given_directory(self, list_files, sender ):
        '''
        Función para indexar los arcchivos
            - Cargamos en tres variables la carpeta origen, las subcarpetas intermedias y los archivos.
            - Recorremos los subdirectorios desde el origen.
            - Leemos los archivos de uno en uno e indexamos el contenido.
        ''' 
        for root, subdirectories, files in os.walk(list_files):
            for subdirectory in subdirectories:
                print(os.path.join(root, subdirectory))
            for file in files:
                self.read_one_file(os.path.join(root, file), sender)

    
    
    #Function that append all info from the files indexed 
    def read_one_file(self, file, sender ):

        #print("Comenzamos")    
        # Abrimos el archivo para leer las líneas
        with open(file) as infile:
            print("Leyendo el fichero:\t" + file)
            contador = 0
            for linea in infile:
                #Para cada línea creamos una imagen y la guardamos
                print( sender.send( linea) )
                #print( "[" + linea + ",\n "+  sender.send( linea) + " ]") #ENVIAMOS LA IMAGEN AL SERVIDOR Y MOSTRAMOS EL RESULTADO POR PANTALLA
            infile.close()
        print("Se ha guardado todo correctamente.")


    