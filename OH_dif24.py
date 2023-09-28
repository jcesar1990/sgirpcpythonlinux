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
import shutil
import csv

#Creamos las carpetas donde se alojaran los datos
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio "+path+" ha sido creado")
    else:
        print("El directorio "+path+" ya existe")

pathestaciones="../estaciones"  
pathfiles="../files"
pathtemporal="../temporal"

makedir(pathestaciones)
makedir(pathfiles)
makedir(pathtemporal)

espacio='-------------'
# Insertamos la fecha
now=datetime.now()
fecha=(now.strftime("%d/%m/%y %H:%M"))
dia=now.strftime("%d-%m-%y")
print(fecha)

#Se buscan los datos en la web por medio de un request, así mismo se guarda en un csv
print("OH")
print(espacio)
urlOH='https://www.oh-iiunam.mx/geojson/datospaginadia.txt'
fileOH_df1 = '../temporal/OH1-24.csv'
fileOH_df2 = '../temporal/OH2-24.csv'
fileOH_df3 = '../temporal/OHS-24h.csv'
fileOH_df4 = '../files/OH-24h.csv'
fileOH_df5 = '../save/'+dia+'OH-24h.csv'

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
    os.remove(fileOH_df2)
    print("Se elimino el archivo OH-15m")
elif hora_inicio != hora_actual != hora_final:
    print("El archivo OH-15m sigue en vigencia")


try:  
    r = urllib.request.urlopen(urlOH)
    f = open(fileOH_df1,'wb')
    f.write(r.read())
    f.close()
    print('Datos de OH obtenidos')
except:
    print("Se produjo un error al momento de descargar los datos")


# Se hacen algunos cambios dentro del archivo para darle el formato correspondiente al csv y que la libreria pandas lo pueda leer correctamente
oh=open(fileOH_df1)
texto=oh.read()
texto1=texto.replace(" ", ",")
#print(texto1)
oh1=open(fileOH_df1,"w")
oh1.write(texto1)
oh.close()
oh1.close()

# Este paso de lectura y guardado solo fue para asignar un indice de forma automatica
oh=pd.read_csv(fileOH_df1, index_col=False, header=None)
oh.to_csv(fileOH_df1)

# Se renombran las columnas con ls claves requeridas
oh=pd.read_csv(fileOH_df1, index_col=0, header=0)
texto1=oh.rename({'2': 'idEstacion'}, axis=1)
texto2=texto1.rename({'3': 'lluvia'}, axis=1)
#print(texto2)
texto2.to_csv(fileOH_df1)

# Se filtran las columnas y se dejan los valores de lluvia con 2 decimales
OH = pd.read_csv(fileOH_df1, index_col=0, header=0, usecols=(3,4))
#print(OH)
#print("Se filtran valores")
roundplaces = np.round(OH,decimals=2)
roundplaces.to_csv(fileOH_df1)
print('Datos de OH obtenidos')


# Ordenamos las estaciones alfabeticamente 
oh=pd.read_csv(fileOH_df1, index_col=0, header=0) 
by_name = oh.sort_values('idEstacion')
by_name.head()
#print(by_name)
by_name.to_csv(fileOH_df1)

if not os.path.exists(fileOH_df2):
    shutil.copy(fileOH_df1,fileOH_df2)
   
    print('El archivo',fileOH_df2,'ha sido creado')
else:
    print('El archivo',fileOH_df2,'ya existe')


df00=pd.read_csv(fileOH_df2, index_col=0, header=0)
df01=pd.DataFrame(df00)
print("archivo 1")
print(df01)

df10=pd.read_csv(fileOH_df1, index_col=0, header=0)
df11=pd.DataFrame(df10)
print("archivo 2")
print(df11)

# Operación de resta para obtener el valor del acumulado en deacuerdo al programador de tareas (10 minutos)
dfn=df11.sub(df01)
print("resta")
print(dfn)
dfn.to_csv(fileOH_df2)

# Recorre las filas del csv final y en caso de encontrar valores negativos en la columna de mm, los volverá 0.
print("Se buscan datos negativos a fin de eliminarlos porque debe tratarse de una falla al momento de hacer la resta")
def reemplazar_negativos(valor):
    if valor < 0:
        return (0)
    else:
        return valor

OH=pd.read_csv(fileOH_df2) 
print(OH)
OH["lluvia"] = OH['lluvia'].apply(reemplazar_negativos)
OH.to_csv(fileOH_df2)


with open(fileOH_df2, 'r') as entrada, open(fileOH_df3, 'w', newline='') as salida:
    read_csv = csv.reader(entrada)
    write_csv = csv.writer(salida)
    
    for fila in read_csv:
        fila_modificada = [valor if valor != '' else '0.0' for valor in fila]
        write_csv.writerow(fila_modificada)
 

#Se agrega la columna de fecha y hora

oh=pd.read_csv(fileOH_df3, index_col=False)
oh['fechaHora']=np.where(oh['lluvia'] !='[]', fecha, ' ', )
print(oh)
oh.to_csv(fileOH_df3)

oh=pd.read_csv(fileOH_df3, usecols=(2, 3, 4), index_col=0, header=0) 
print(oh)
oh.to_csv(fileOH_df3)
#Concatenar df3 con df4

ohnew=pd.read_csv(fileOH_df3, index_col=0, header=0)

if not os.path.exists(fileOH_df4):

    # Dataframe de estaciones
    estaciones = []
    nodata=[]
    # Crear un diccionario con los datos
    data = {
    'idEstacion': estaciones,
    'lluvia': nodata,
    }

    # Crear el DataFrame a partir del diccionario
    archivo_origen = pd.DataFrame(data)
    #print(archivo_origen)
    archivo_origen.to_csv(fileOH_df4, index=False)
    print('El archivo',fileOH_df4,'ha sido creado')
else:
    print('El archivo',fileOH_df4,'ya existe')

ohconcat=pd.read_csv(fileOH_df4, index_col=0, header=0) 
# print('el oh descargado es:')
# print(ohdescargado)
# print('y el oh anterior es:')
# print(ohanterior)

nuevooh= pd.concat([ohnew, ohconcat])
print('Archivo contatenado')
print(nuevooh)
nuevooh.to_csv(fileOH_df4)
shutil.copy(fileOH_df4, fileOH_df5)
time.sleep(5)
remove(fileOH_df2)
os.rename(fileOH_df1, fileOH_df2)