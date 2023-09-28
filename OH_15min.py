from asyncore import read
from os import close, remove, write
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import requests
import urllib.request
import pandas as pd
import numpy as np
from os import remove
import threading

#Creamos las carpetas donde se alojaran los datos
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio "+path+" ha sido creado")
    else:
        print("El directorio "+path+" ya existe")

pathestaciones="../estaciones"  
pathfiles="../files"
pathsave="../save"

makedir(pathestaciones)
makedir(pathfiles)
makedir(pathsave)

espacio='-------------'

# Insertamos la fecha
now=datetime.now()
fecha=(now.strftime("%d/%m/%y %H:%M"))
print(fecha)

#Se buscan los datos en la web por medio de un request, así mismo se guarda en un csv
print("OH")
print(espacio)
urlOH='https://www.oh-iiunam.mx/geojson/datospaginaquince.txt'
fileOH = '../files/OH15.csv'
fileOH_save = '../save/OH.csv'
try:  
    r = urllib.request.urlopen(urlOH)
    f = open(fileOH,'wb')
    f.write(r.read())
    f.close()
    print('Datos de OH obtenidos')
except:
    print("Se produjo un error al momento de descargar los datos")

# Se hacen algunos cambios dentro del archivo para darle el formato correspondiente al csv y que la libreria pandas lo pueda leer correctamente
oh=open(fileOH)
texto=oh.read()
texto1=texto.replace(" ", ",")
#print(texto1)
oh1=open(fileOH,"w")
oh1.write(texto1)
oh.close()
oh1.close()

# Este paso de lectura y guardado solo fue para asignar un indice de forma automatica
oh=pd.read_csv(fileOH, index_col=False, header=None)
oh.to_csv(fileOH)

# Se renombran las columnas con ls claves requeridas
oh=pd.read_csv(fileOH, index_col=0, header=0)
texto1=oh.rename({'2': 'idEstacion'}, axis=1)
texto2=texto1.rename({'3': 'lluvia'}, axis=1)
#print(texto2)
texto2.to_csv(fileOH)

# Se filtran las columnas y se dejan los valores de lluvia con 2 decimales
OH = pd.read_csv(fileOH, index_col=0, header=0, usecols=(3,4))
#print(OH)
roundplaces = np.round(OH,decimals=2)
roundplaces.to_csv(fileOH)
print('Datos de OH obtenidos')


# Ordenamos las estaciones alfabeticamente 
oh=pd.read_csv(fileOH, index_col=0, header=0) 
by_name = oh.sort_values('idEstacion')
by_name.head()
#print(by_name)
by_name.to_csv(fileOH)

# Leemos los archivos csv como dataframes

oh=pd.read_csv(fileOH, index_col=False)
oh['fechaHora']=np.where(oh['lluvia'] !='[]', fecha, ' ', )
#print(oh)
oh.to_csv(fileOH)

oh=pd.read_csv(fileOH, usecols=(1, 2, 3), index_col=0, header=0) 
print(oh)
oh.to_csv(fileOH)

registro=open(fileOH)
texto=registro.read()
texto_r=texto.replace("lluvia", fecha)
print("Reemplazo de lluvia por la fecha y hora")
print(texto_r)
save=open(fileOH_save,"w")
save.write(texto_r)
save.close()


oh=pd.read_csv(fileOH_save, usecols=(0,1),index_col=None, header=0) 
#print(oh)
oht=oh.T
#print(oht)
oht.to_csv(fileOH_save)

oh=pd.read_csv(fileOH_save,index_col=0, header=1) 
print(oh)
oh.to_csv(fileOH_save)



final=datetime.now()
print(final)