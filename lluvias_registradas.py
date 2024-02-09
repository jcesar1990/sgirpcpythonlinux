import pandas as pd
import csv
from datetime import date, time, datetime, timedelta
import os


# print("script para datos de lluvia de 6:00 a 5:55")

def lluviasgirpc(clave, estacion, longitud, latitud):
    print("Se obtendra el resgistro de la estacion "+estacion+" con clave "+clave+" para la elaboracion del mapa de lluvias del dia")

    # Determinamos la fecha de adquisición de los datos para el mapa de lluvia acumulada en 24 horas de 06:00 a 05:55 horas
    hoy = date(2023, 11, 23)
    #hoy = date.today()
    print(hoy)
    ayer = hoy - timedelta(days=1)
    ayer_srt = ayer.strftime("%d/%m/%y")
    ayer_csv = ayer.strftime("%d-%m-%y")

    # Convertir la cadena de hora a objeto datetime.time
    horai = "06:00"
    horaf = "05:55"

    hora_objetoi = datetime.strptime(horai, "%H:%M").time()
    print(hora_objetoi)
    hora_objetof = datetime.strptime(horaf, "%H:%M").time()
    print(hora_objetof)

    horaoi = hora_objetoi.strftime("%H:%M")
    horaof = hora_objetof.strftime("%H:%M")

    # Combinar la fecha y la hora inicial para obtener la fecha y hora de inicio completa
    fechai = datetime.combine(ayer, hora_objetoi)
    fechaf = datetime.combine(hoy, hora_objetof)

    # startdate = fechai.strftime("%d/%m/%y %H:%M")
    # enddate = fechaf.strftime("%d/%m/%y %H:%M")

    print("La fecha de ayer es:", ayer)
    print("La fecha de hoy es:", hoy)
    print("Hora de inicio:", horaoi)
    print("Hora de finalización:", horaof)
    print("La toma de datos inicia desde:", fechai)
    print("El final de la toma de datos es desde:", fechaf)
    
    # rango = startdate <= enddate
    # print("El rango es:",rango)

    # Ubicacion del archivo csv
    print("Los datos de la estacion se encuentran en:")

    csvfile_in = "C:/Users/meteorologia/Desktop/files/"+clave+".csv"
    print(csvfile_in)

    print("Los datos de la estacion ya filtrados se encuentran en: ")
    csvfile_out = "C:/Users/meteorologia/Desktop/files/lluvia.csv"
    print(csvfile_out)

    print("Los datos de cada estacion se guardaran en un unico csv correspondiente a si es temperatura o lluvia, se almacenaran en:")
    cvssave = "C:/Users/meteorologia/Desktop/files/lluvia/lluvia-"+ayer_csv+".csv"
    print(cvssave)

    # Con la libreria pandas manipularemos el archivo
    print("Los datos a usar para lluvia son:")
    DF= pd.read_csv(csvfile_in,  index_col=False, header=0, usecols=(8,9,10), parse_dates=["fechaHora"], dayfirst=True)
    #print(DF)

    print("Filtrando los datos por hora de inicio y hora de termino")
    DF_filtro = DF[(DF['fechaHora'] >= fechai) & (DF['fechaHora'] <= fechaf)]
    #print(DF_filtro)

    DF_filtro.to_csv(csvfile_out)
    print("El csv con los datos de las lluvias registradas del dia de",ayer_srt,"estan listos")
    
    DF = pd.read_csv(csvfile_out, index_col=False, header=0)
    print(DF)

    # Intenta obtener la suma de la columna lluvia con un valor redondeado a 1 decima, en caso de error se espedifican detalles 
    # con el KeyError
    try:
        suma_lluvia =round (DF_filtro['lluvia'].sum(), 1)
        print("La suma de los valores de la columna 'lluvia' es:", suma_lluvia)
    except KeyError as e:
        print(f"Error: La columna 'lluvia' no está presente en el DataFrame. Detalles del error: {e}")

    DF_acumulado= pd.DataFrame({
        'ID':[clave],
        'Estacion':[estacion],
        'Latitud':[latitud],
        'Longitud':[longitud],
        'Lluvia':[suma_lluvia]
    })
    print(DF_acumulado)
    DF_acumulado.to_csv(csvfile_out, index=False)
    print('El archivo',csvfile_out,'ha sido creado')
    
    # Verificamos si existe el archivo save del dia y si no, lo creamos con los datos del acumulado de
    # la primera estacion evaluada

    if not os.path.exists(cvssave):
       
        # Salvamos el acumulado en el archivo csvsave
        DF_acumulado.to_csv(cvssave, index=False)
        print('El archivo',cvssave,'ha sido creado')
    
    else:
    
        print('El archivo',cvssave,'ya existe, se procede a concatenar la temperatura maxima de la siguiente estacion evaluada')
        
        csv1=pd.read_csv(cvssave, index_col=0, header=0)
        print("Imprimiendo tabla save")
        print(type(csv1))
        print(csv1)
        csv2=pd.read_csv(csvfile_out, index_col=0, header=0)
        print("Imprimiendo el acumulado de lluvia")
        print(type(csv2))
        print(csv2) 
        csvconcat=pd.concat([csv1, csv2])
        print("Archivo concatenado")
        csvconcat.to_csv(cvssave)
        print(csvconcat)
        print("Se concateno el datos de la estación al archivo")
    
# Funcion,id,nombre,longitud,latitud
lluviasgirpc("BELVS", "Belvedere Ajusco. TLP", "-99.226113", "19.266637")
lluviasgirpc("GAM2S", "Martin Carrera. GAM", "-99.103701", "19.483556")
lluviasgirpc("LOMS", "Lomas Zaragoza. IZP", "-99.000071", "19.358041")
lluviasgirpc("SJEROS", "San Jeronimo. MAC", "-99.215116", "19.325168")
lluviasgirpc("STFS", "Sta. Fe. CUJ", "-99.285309", "19.361708")
lluviasgirpc("SURS", "Sta. Ursula. COY", "-99.146655", "19.301357")
lluviasgirpc("TEZS", "Tezonco. IZP", "-99.065118", "19.314968")

