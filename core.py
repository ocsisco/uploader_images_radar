import time
from datetime import datetime

from extractor_imagenes_radar import captura_gif_de_la_fuente
import remove_temp_files


while 1:
        
    tempus = datetime.now()
    tempus = tempus.minute
    

    if tempus == 1 or tempus == 11 or tempus == 21 or tempus == 31 or tempus == 41 or tempus == 51:
        
        #captura_gif_de_la_fuente("Zaragoza")
        #captura_gif_de_la_fuente("Almería")         
        #captura_gif_de_la_fuente("Asturias")       
        #captura_gif_de_la_fuente("Illes Balears")  
        #captura_gif_de_la_fuente("Barcelona")       
        #captura_gif_de_la_fuente("Cáceres")        
        #captura_gif_de_la_fuente("A Coruña")        
        #captura_gif_de_la_fuente("Madrid")          
        #captura_gif_de_la_fuente("Málaga")     
        #captura_gif_de_la_fuente("Murcia")          
        #captura_gif_de_la_fuente("Palencia")        
        #captura_gif_de_la_fuente("Las Palmas")      
        #captura_gif_de_la_fuente("Sevilla")         
        captura_gif_de_la_fuente("Valencia")        
        #captura_gif_de_la_fuente("Vizcaya")         
        #captura_gif_de_la_fuente("Zaragoza")


        remove_temp_files.remove_temp_files()

                
        time.sleep(60)
