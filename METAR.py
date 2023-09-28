import requests
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import os

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

url="https://www.aviationweather.gov/metar/data?ids=mmmx&format=raw&date=&hours=48"
filehtml= '../estaciones/MMMX.txt'
filein= '../estaciones/MMMX.txt'
fileout= '../files/MMMX.txt'

#Peticion para compiar los datos del html del METAR
try:

    r = requests.get(url)
    soup= BeautifulSoup(r.content, "html.parser")
    tag=soup.find("code")
    datos=tag.text
    print(datos)

    r = urllib.request.urlopen(url)
    f = open(filehtml,'wb')
    f.write(r.read())
    f.close()
    #print(file1)
    print('Datos del html del METAR descargados')

    with open(filehtml,"r") as fr:
        contenido= fr.read()

    soup= BeautifulSoup(contenido,"html.parser")
    tags_code=soup.find_all("code")
    with open(filein,"w") as f:
        for etiqueta in tags_code:
            tags_content=etiqueta.text
            print(tags_content)
            f.write(tags_content + "\n")

    txt=open(filein)
    txt1=txt.read()
    print(txt1)
    txt2=txt1.replace(" ",",")
    csv=open(fileout,"w")
    csv.write(txt2)
    txt.close()
    csv.close()

    final=datetime.now()
    print("El proceso se completo a las",final,"la proxima ejecución será en la próxima hora")
except:
    print("Se presento un error, la próxima ejecición será dentro de una hora a partir de:",final)
