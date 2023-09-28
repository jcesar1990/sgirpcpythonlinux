import os
from pickle import FALSE, NONE
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import urllib.request
import pandas as pd
import numpy as np
import seaborn as sb
from os import remove
import threading
import shutil
from shutil import copy

def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio "+path+" ha sido creado")
    else:
        print("El directorio "+path+" ya existe")

pathestaciones="../estaciones"  
pathfiles="../files"

def proceso(nombre,id):
    print("Ultima actualizacion del programa el día 13/09/23 a las 15:44")
    
    now = datetime.now()

    yesterday=now-timedelta(days=1)

    yesterdaybefore=now-timedelta(days=2)

    hoy0=datetime.strftime(now,'%d')
    meshoy0=datetime.strftime(now,'%m')
    añohoy0=datetime.strftime(now,'%Y')
    fecha_hoy0= añohoy0 +"/"+ meshoy0 +"/"+ hoy0
    print("fecha_hoy0 yyyy/mm/dd")
    print(fecha_hoy0)

    ayer0=datetime.strftime(yesterday,'%d')
    mesayer0=datetime.strftime(yesterday,'%m')
    añoayer0=datetime.strftime(yesterday,'%Y')
    fecha_ayer0= añoayer0 +"/"+ mesayer0 +"/"+ ayer0
    print("fecha_ayer0 yyyy/mm/dd")
    print(fecha_ayer0)

    anteayer0=datetime.strftime(yesterdaybefore,'%d')
    mesanteayer0=datetime.strftime(yesterdaybefore,'%m')
    añoanteayer0=datetime.strftime(yesterdaybefore,'%Y')
    fecha_anteayer0= añoanteayer0 +"/"+ mesanteayer0 +"/"+ anteayer0
    print("fecha_anteayer0 yyyy/mm/dd")
    print(fecha_anteayer0)



    hoy1=datetime.strftime(now,'%d')
    meshoy1=datetime.strftime(now,'%m')
    añohoy1=datetime.strftime(now,'%y')
    fecha_hoy1= hoy1 +"/"+ meshoy1 +"/"+ añohoy1
    print("fecha_hoy1 dd/mm/yy")
    print(fecha_hoy1)

    ayer1=datetime.strftime(yesterday,'%d')
    mesayer1=datetime.strftime(yesterday,'%m')
    añoayer1=datetime.strftime(yesterday,'%y')
    fecha_ayer1= ayer1 +"/"+ mesayer1 +"/"+ añoayer1
    print("fecha_ayer1 dd/mm/yy")
    print(fecha_ayer1)

    anteayer1=datetime.strftime(yesterdaybefore,'%d')
    mesanteayer1=datetime.strftime(yesterdaybefore,'%m')
    añoanteayer1=datetime.strftime(yesterdaybefore,'%y')
    fecha_anteayer1= anteayer1 +"/"+ mesanteayer1 +"/"+ añoanteayer1
    print("fecha_anteayer1 dd/mm/yy")
    print(fecha_anteayer1)

    hoy3=datetime.strftime(now,'%d')
    meshoy3=datetime.strftime(now,'%m')
    añohoy3=datetime.strftime(now,'%Y')
    fecha_hoy3= hoy3 +"/"+ meshoy3 +"/"+ añohoy3
    print("fecha_hoy3 dd/mm/yyyy")
    print(fecha_hoy3)

    ayer3=datetime.strftime(yesterday,'%d')
    mesayer3=datetime.strftime(yesterday,'%m')
    añoayer3=datetime.strftime(yesterday,'%Y')
    fecha_ayer3= ayer3 +"/"+ mesayer3 +"/"+ añoayer3
    print("fecha_ayer3 dd/mm/yyyy")
    print(fecha_ayer3)

    anteayer3=datetime.strftime(yesterdaybefore,'%d')
    mesanteayer3=datetime.strftime(yesterdaybefore,'%m')
    añoanteayer3=datetime.strftime(yesterdaybefore,'%Y')
    fecha_anteayer3= anteayer3 +"/"+ mesanteayer3 +"/"+ añoanteayer3
    print("fecha_anteayer3 dd/mm/yyyy")
    print(fecha_anteayer3)

    espacio="-------------"

    print(espacio)

    try:
        #Se obtienen los datos del portal de conagua
        url1 = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v2/siveaEsri2/php/get_reporteEstacion.php?tipo=1&estacion='+nombre
        file1 = '../estaciones/'+nombre+'.csv'
        file2 = '../files/'+nombre+'.csv'
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'MyApp/1.0')]
        urllib.request.install_opener(opener)
        r = urllib.request.urlopen(url1)
        f = open(file1,'wb')
        f.write(r.read())
        f.close()
        print("Datos de la estación",nombre,"obtenidos")
        print(file1)
    except:
        print("Ha ocurrido un error con la descarga del archivo")
    else:
        CONAGUA=pd.read_csv(file1, index_col=False, header=8, encoding='latin-1', usecols=(0,2,3,4,5,6,7,8,9,10))
        CONAGUA.to_csv(file1)
        print("Se imprimen datos CONAGUA")
        print(CONAGUA)
        CONAGUA1=open(file1,'r')
        CONAGUA1= ''.join([i for i in CONAGUA1])
        texto1=CONAGUA1.replace('Fecha Local', 'fechaHora')
        texto2=texto1.replace('Dirección del Viento (grados)', 'direccionViento')
        texto3=texto2.replace('Dirección de ráfaga (grados)','direccionRacha')
        texto4=texto3.replace('Rapidez de viento (km/h)', 'velocidadViento')
        texto5=texto4.replace('Rapidez de ráfaga (km/h)', 'velocidadRacha')
        texto6=texto5.replace('Temperatura del Aire (°C)', 'temperatura')
        texto7=texto6.replace('Humedad relativa (%)', 'humedadRelativa')
        texto8=texto7.replace('Presión Atmosférica (hpa)', 'presionBar')
        texto9=texto8.replace('Precipitación (mm)', 'lluvia')
        texto10=texto9.replace('Radiación Solar (W/m²)', 'radiacionSolar')
        texto11=texto10.replace('-','/')
        texto12=texto11.replace(fecha_hoy0,fecha_hoy1)
        texto13=texto12.replace(fecha_ayer0,fecha_ayer1)
        texto14=texto13.replace(fecha_hoy3,fecha_hoy1)
        texto15=texto14.replace(fecha_ayer3,fecha_ayer1)
        texto16=texto15.replace(fecha_anteayer0,fecha_anteayer1)
        texto17=texto16.replace(fecha_anteayer3,fecha_anteayer1)
        print(texto17)
        CONAGUA1=open(file1, 'w')
        CONAGUA1.writelines(texto17)
        CONAGUA1.close()
        CONAGUA=pd.read_csv(file1, index_col=0, header=0, usecols=(1,2,3,4,5,6,7,8,9,10))
        print("primera lectura de datos")
        print(CONAGUA)
        CONAGUA.to_csv(file1)
        try:
            DF=pd.read_csv(file1, index_col=0)
            DF['idEstacion']=np.where(DF['temperatura'] !='[]', id, ' ', )
            print(DF)
            DF.to_csv(file1)
            DF=pd.read_csv(file1, index_col=0)
            DF.fillna(9999, inplace=True)
            DF
            DF.to_csv(file1)
            print("segunda lectura de datos")
            print(DF)
            DF0=pd.read_csv(file1)
            DF=pd.DataFrame(DF0)
            print(DF)
            cols= list(DF.columns.values)
            newcols=['fechaHora', 'direccionViento', 'direccionRacha', 'velocidadViento', 'velocidadRacha', 'temperatura', 'humedadRelativa', 'presionBar', 'lluvia', 'radiacionSolar', 'idEstacion']
            DF=DF.reindex(columns=newcols)
            print("tercera lectura de datos")
            print(DF)
            DF.to_csv(file1)
            CONAGUA=pd.read_csv(file1, index_col=0, header=0, usecols=(1,2,3,4,5,6,7,8,9,10,11))
            print("final")
            print(CONAGUA)
            CONAGUA.to_csv(file2)
            print("Los datos de la estacion",nombre,"estan listos")
            final=datetime.now()
            print("El proceso se completo a las",final,"la proxima ejecución será en 10 minutos")
        except:
            print("La estacion",nombre,"no presenta registros.")
            print("Se presento un error, la próxima ejecición será dentro de 10 minutos a partir de la hora:",final)

test=proceso("ECOGUARDAS","ECOGUARDAS")