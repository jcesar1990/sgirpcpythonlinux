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
import csv
import shutil

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
fechahora=(now.strftime("%d/%m/%y %H:%M"))
fechadia=(now.strftime("%d-%m-%y"))
print(fechahora)

#Se buscan los datos en la web por medio de un request, así mismo se guarda en un csv
print("OH")
print(espacio)
urlOH='https://www.oh-iiunam.mx/geojson/datospaginaquince.txt'
fileOH_df0 = '../temporal/OH0-15m.csv'
fileOH_df1 = '../files/OH-15m.csv'
fileOH_df2 = '../save/'+fechadia+'OH-15m.csv'

#Corte de los datos al final del día
#Obteniendo la hora actual.
hora_actual=time.strftime("%H:%M")
print("La hora actual es:",hora_actual)
# Se crea un objeto de hora para las 6:00am.
hora_1 = "00:00"
hora_inicio = time.strftime(hora_1)
print(hora_inicio)
# Se crea un objeto de hora para las 6:10am.
hora_2 = "00:20"
hora_final = time.strftime(hora_2)
print(hora_final)

#Comprobando la hora para el corte de los datos, 
print("Comprobando corte de datos a las 00:20 horas")
if hora_inicio <= hora_actual <= hora_final:
    os.remove(fileOH_df1)
    print("Se elimino el archivo OH-15m")
elif hora_inicio != hora_actual != hora_final:
    print("El archivo OH-15m sigue en vigencia")



# Condición para archivo OH0.csv en caso de que este no exista 
if not os.path.exists(fileOH_df1):

    # Dataframe de estaciones
    estaciones = []
    nodata=[]
    fechadf=[]
    # Crear un diccionario con los datos
    data = {
    'idEstacion': estaciones,
    'lluvia': nodata,
    'fechaHora': fechadf
    }

    # Crear el DataFrame a partir del diccionario
    archivo_origen = pd.DataFrame(data)
    #print(archivo_origen)
    archivo_origen.to_csv(fileOH_df1, index=False)
    print('El archivo',fileOH_df1,'ha sido creado')
else:
    print('El archivo',fileOH_df1,'ya existe')



try:  
    r = urllib.request.urlopen(urlOH)
    f = open(fileOH_df0,'wb')
    f.write(r.read())
    f.close()
    print('Datos de OH obtenidos')
except:
    print("Se produjo un error al momento de descargar los datos")

# Se hacen algunos cambios dentro del archivo para darle el formato correspondiente al csv y que la libreria pandas lo pueda leer correctamente
oh=open(fileOH_df0)
texto=oh.read()
texto1=texto.replace(" ", ",")
#print(texto1)
oh1=open(fileOH_df0,"w")
oh1.write(texto1)
oh.close()
oh1.close()

# Este paso de lectura y guardado solo fue para asignar un indice de forma automatica
oh=pd.read_csv(fileOH_df0, index_col=False, header=None)
oh.to_csv(fileOH_df0)

# Se renombran las columnas con ls claves requeridas
oh=pd.read_csv(fileOH_df0, index_col=0, header=0)
texto1=oh.rename({'2': 'idEstacion'}, axis=1)
texto2=texto1.rename({'3': 'lluvia'}, axis=1)
print(texto2)
texto2.to_csv(fileOH_df0)

# Se filtran las columnas y se dejan los valores de lluvia con 5 decimales
OH = pd.read_csv(fileOH_df0, index_col=0, header=0, usecols=(3,4))
#print(OH)
roundplaces = np.round(OH,decimals=5)
roundplaces.to_csv(fileOH_df0)
print('Datos de OH obtenidos')


# Ordenamos las estaciones alfabeticamente 
oh=pd.read_csv(fileOH_df0, index_col=0, header=0) 
by_name = oh.sort_values('idEstacion')
by_name.head()
#print(by_name)
by_name.to_csv(fileOH_df0)


oh=pd.read_csv(fileOH_df0, index_col=False)
oh['fechaHora']=np.where(oh['lluvia'] !='[]', fechahora, ' ', )
#print(oh)
oh.to_csv(fileOH_df0)

oh=pd.read_csv(fileOH_df0, usecols=(1, 2, 3), index_col=0, header=0) 
#print(oh)
oh.to_csv(fileOH_df0)

ohdescargado=pd.read_csv(fileOH_df0, index_col=0, header=0)
ohanterior=pd.read_csv(fileOH_df1, index_col=0, header=0) 
# print('el oh descargado es:')
# print(ohdescargado)
# print('y el oh anterior es:')
# print(ohanterior)

nuevooh= pd.concat([ohdescargado, ohanterior])
print('Archivo contatenado')
print(nuevooh)
nuevooh.to_csv(fileOH_df1)
shutil.copy(fileOH_df1, fileOH_df2)


print("Proceso completado. Se han filtrado las estaciones y guardado en 'files'.")

final=datetime.now()
print(final)
