import requests
from datetime import datetime
import shutil
from PIL import Image
import os
import numpy as np

from handler_s3_images import upload_images,upload_images_color,upload_images_small






url = "https://opendata.aemet.es/opendata/api/red/radar/regional/"
apikey = "/?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmcmFuY2lzY29ncmFuZWxsaGFyb0BnbWFpbC5jb20iLCJqdGkiOiIzMmU3MWJlNS02YjliLTQ4OTctYjFkMi1kOTk0MDRjZDUyMTgiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTY4NTk4MjA3MywidXNlcklkIjoiMzJlNzFiZTUtNmI5Yi00ODk3LWIxZDItZDk5NDA0Y2Q1MjE4Iiwicm9sZSI6IiJ9.4tV4ZV0S7FtDroGaMqzCxwR3cgeIp3mQ57nFLBSZQqU"


region = {"Almería"         :"am",
          "Asturias"        :"sa",
          "Illes Balears"   :"pm",
          "Barcelona"       :"ba",
          "Cáceres"         :"cc",
          "A Coruña"        :"co",
          "Madrid"          :"ma",
          "Málaga"          :"ml",
          "Murcia"          :"mu",
          "Palencia"        :"vd",
          "Las Palmas"      :"ca",
          "Sevilla"         :"se",
          "Valencia"        :"va",
          "Vizcaya"         :"ss",
          "Zaragoza"        :"za"
          }


def captura_gif_de_la_fuente(name_region):

    data = requests.get(url + region[name_region] + apikey)

    if data.status_code == 200:

        try:

            data = data.json()
            
            # Extrae del json la url de la clave "datos:"

            url_imagen_radar = (data["datos"]) 
            
            # Crea y arregla nombre de archivo evitando caracteres prohibidos.

            fecha = datetime.now()

            format = "%Y-%m-%d-%H-%M"

            fecha = fecha.strftime(format)

            fecha = (name_region) + "_" + str(fecha)

            print (fecha)

            # El nombre de las imagenes es la fecha de creación.

            nombre_del_archivo = fecha
            


            data = requests.get(url_imagen_radar)
            if data.status_code == 200:

                try:
                    # obtiene la imagen (.content) contenido
                    imagen_en_crudo = requests.get(url_imagen_radar).content
            
                    # abre archivo con nombre de imglocal y escribe el contenido
                    with open (nombre_del_archivo, 'wb') as handler:
                        handler.write(imagen_en_crudo)


                    # Guarda un copia original (en color)
                    imagen_en_crudo = Image.open(nombre_del_archivo).convert('RGBA')
                    imagen_en_crudo.save(nombre_del_archivo +".png",'png', optimize=True, quality=70)

                    # La manda a la carpeta imagenes color
                    shutil.move(nombre_del_archivo + ".png","images_color")
                    
                    # Y cerramos el objeto imagen 
                    imagen_en_crudo.close()

                    
                    # Pasa la imagen a blanco y negro (.convert'L') y crea .png a través del .gif
                    imagen_en_crudo = Image.open(nombre_del_archivo).convert('L')
                    imagen_en_crudo.save(nombre_del_archivo +".png",'png', optimize=True, quality=70)

                    # mejorar escala de grises dividiendo la escala de colores de la leyenda en tramos equidistantes, para ello:
                    # recorre matriz y sustituye old_color por new_color *nota: Algoritmo mejorable, puede sustituir todos los valores en un recorrido, mejora dos décimas y queda mas sucio.
                    
                    matriz = np.array(imagen_en_crudo)

                    def recorre_y_sustituye(old_color,new_color,matriz):

                        idx_fila = 0
                        for fila in (matriz):

                            idx_columna = 0

                            for columna in (fila):
                                if columna == old_color:
                                    matriz[idx_fila][idx_columna]=new_color
                                idx_columna = idx_columna +1
                            idx_fila = idx_fila +1
                        
                    recorre_y_sustituye(29,12,matriz)
                    recorre_y_sustituye(116,18,matriz)
                    recorre_y_sustituye(177,24,matriz)
                    recorre_y_sustituye(101,30,matriz)
                    recorre_y_sustituye(113,36,matriz)
                    recorre_y_sustituye(150,42,matriz)
                    recorre_y_sustituye(226,48,matriz)
                    recorre_y_sustituye(186,54,matriz)
                    recorre_y_sustituye(151,60,matriz)
                    recorre_y_sustituye(76,66,matriz)
                    recorre_y_sustituye(70,72,matriz)


                    imagen_nueva = Image.fromarray(matriz, 'L')
                    imagen_nueva.save(nombre_del_archivo + ".png")
                             

                    # mueve las imagenes a la carpeta de imagenes
                    shutil.move(nombre_del_archivo + ".png","images")

                    # cerramos el objeto imagen para que no este en uso y poder borrar
                    imagen_en_crudo.close()

                    # y borramos .gif
                    os.remove(nombre_del_archivo)

                    shutil.copy("images/" + nombre_del_archivo + ".png" , "images_small/" + nombre_del_archivo + ".png")
                    imagen = Image.open("images_small/" + nombre_del_archivo + ".png")
                    imagen = imagen.resize((96,106))
                    imagen.save("images_small/" + nombre_del_archivo +'.png')
                    imagen.close()

                except KeyError:
                    print ("error al obtener la imagen y/o radar averiado")

        except KeyError:
            print ("error al obtener la imagen y/o radar averiado") 

    

    try:

        upload_images(nombre_del_archivo)
        upload_images_small(nombre_del_archivo)
        upload_images_color(nombre_del_archivo)

        print ("Guardadas las imagenes de radar y subidas al servidor")

    except:
        print ("Error al subir las imágenes a s3 bucket")


    
 