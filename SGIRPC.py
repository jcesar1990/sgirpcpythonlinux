# Importamos las librerías necesarias
import ModuloSGIRPCV
import ModuloSGIRPCN
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
    ModuloSGIRPCN.proceso("Marín Carrera", "GAM2S")
    print("Se han filtrado los datos de la nueva estación en GAM")
except:
    print("Hubo un problema al filtrar los datos de la nueva estación en GAM")

try:
    ModuloSGIRPCN.proceso("DelMar","TLAS")
    print("Se han filtrado los  datos de la nueva estacion en Tlahuac")
except:
    print("Hubo un problema al filtrar los datos de la nueva estación en Tlahuac")

try:
    ModuloSGIRPCN.proceso("Cuajimal","STFS")
    print("Se han filtrado los  datos de la nueva estacion en Santa Fe")
except:
    print("Hubo un problema al filtrar los datos de la nueva estación en Santa Fe")

try:
    ModuloSGIRPCN.proceso("Tezonco","TEZS")
    print("Se han filtrado los  datos de la nueva estacion en Iztapalapa II")
except:
    print("Hubo un problema al filtrar los datos de la nueva estación en Iztapalapa II")

try:
    ModuloSGIRPCN.proceso("Lomas","LOMS")
    print("Se han filtrado los  datos de la nueva estacion en Iztapalapa1")
except:
    print("Hubo un problema al filtrar los datos de la nueva estación en Iztapalapa1")

try:
    ModuloSGIRPCN.proceso("Belveder","BELVS")
    print("Se han filtrado los  datos de la nueva estacion en Ajusco")
except:
    print("Hubo un problema al filtrar los datos de la nueva estación en Ajusco")

try:
    ModuloSGIRPCN.proceso("SanJeron", "SJEROS")
    print("Se han filtrado los datos de la nueva estación en San Jeronimo")
except:
    print("Hubo un problema al filtrar los datos de la nueva estación en San Jeronimo")

try:
    ModuloSGIRPCV.proceso("iztacalco","AGOS")
except:
    print("Hubo un problema con la descarga de datos de esta estación")

try:
    ModuloSGIRPCV.proceso("azcapotzalco","FERS")
except:
    print("Hubo un problema con la descarga de datos de esta estación")

try:
    ModuloSGIRPCV.proceso("cuautepec","CUAUS")
except:
    print("Hubo un problema con la descarga de datos de esta estación")

try:
    ModuloSGIRPCV.proceso("juarez", "SGIRPC")
except:
    print("Hubo un problema con la descarga de datos de esta estación")

try:
    ModuloSGIRPCV.proceso("miguelhidalgo","LEGS")
except:
    print("Hubo un problema con la descarga de datos de esta estación")

try:
    ModuloSGIRPCN.proceso("milpaalta","MPAS")
except:
    print("Hubo un problema con la descarga de datos de esta estación")

try:
    ModuloSGIRPCV.proceso("topilejo","TPJS")
except:
    print("Hubo un problema con la descarga de datos de esta estación")

try:
    ModuloSGIRPCV.proceso("coyoacan","SURS")
except:
    print("Hubo un problema con la descarga de datos de esta estación")

try:
    ModuloSGIRPCV.proceso("xochimilco","TLHS")
except:
    print("Hubo un problema con la descarga de datos de esta estación")
