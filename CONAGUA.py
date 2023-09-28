#Importamos librerias
import ModuloCONAGUA
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
#ModuloCONAGUA.proceso("TACUBAYA","TACUBAYA")   

ModuloCONAGUA.proceso("ECOGUARDAS","ECOGUARDAS")

ModuloCONAGUA.proceso("TEZONTLE","TEZONTLE")

ModuloCONAGUA.proceso("CERROCATEDRAL","ISI")

ModuloCONAGUA.proceso("ALTZOMONI","ALTZOMONI")

ModuloCONAGUA.proceso("PRESAMADINSMN","NAU")

ModuloCONAGUA.proceso("ESCNALCIENCIASBIOLOGICAS","ENCB")
