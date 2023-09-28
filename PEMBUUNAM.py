# Importamos las librerías necesarias
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import ModuloPEMBU
import os


espacio='-------------'
#Creamos las carpetas donde se alojaran los datos
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

try:
    ModuloPEMBU.proceso("ICAyCC")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)

try:
    ModuloPEMBU.proceso("ccha")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)

try:
    ModuloPEMBU.proceso("cchn")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)

try:
    ModuloPEMBU.proceso("ccho")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)

try:
    ModuloPEMBU.proceso("cchs")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("cchv")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("enp1")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("enp2")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("enp3")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("enp4")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("enp5")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("enp6")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("enp7")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("enp8")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)    

try:
    ModuloPEMBU.proceso("enp9")
except:
    print("Hubo un problema al descargar los datos de esta estación")
print(espacio)
    
final=datetime.now()
print(final)