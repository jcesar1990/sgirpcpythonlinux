from asyncore import read
from os import close, remove, write
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import urllib.request
import pandas as pd
import numpy as np
from os import remove
import threading

#Creamos las carpetas donde se añpjaran los datos
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio "+path+" ha sido creado")
    else:
        print("El directorio "+path+" ya existe")

pathestaciones="../estaciones"  
pathfiles="../files"

makedir(pathestaciones)
makedir(pathfiles)

espacio='-------------'

print(espacio)
print("Descargando datos de SIMAT")

try:
    url1 = 'http://189.204.131.110:8002/webserviceSIMAT.asmx/Alerta_Temprana'
    file1 = '../files/simat.txt' 
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'MyApp/1.0')] 
    urllib.request.install_opener(opener)
    r = urllib.request.urlopen(url1)
    f = open(file1,'wb')
    f.write(r.read())
    f.close()
    print("Datos de calidad del aire obtenidos")
    print(file1)
except:
    print("Ha ocurrido un error con la descarga del archivo")

final=datetime.now()
print(final)
