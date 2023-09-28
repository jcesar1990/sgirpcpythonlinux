from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import os
import glob
import shutil

# Ruta del ejecutable del Chrome WebDriver
ruta_webdriver = '/home/cesar/Documents/sgirpcpythonlinux/chromedriver-linux64/chromedriver-exe'


#Se eliminan los archivos .dat que puedan existir en la carpeta de descargas para evitar errores al momento de la compilación.
descargas="/home/cesar/Downloads/"
tipo="*.dat"
delite=glob.glob(descargas + tipo)
for f in delite:
    os.remove(f)
    print("Los archivos .dat fueron eliminados")

#Definimos los PATHS para los archivos.
dircsvsacmex0 = '/home/cesar/Documents/otros/SACMEX0.csv'
dircsvsacmex0_0 = '/home/cesar/Documents/Temporal/SACMEX0.csv'
dircsvsacmex1 = '/home/cesar/Documents/otros/SACMEX1.csv'
dirtxtsacmex1 = '/home/cesar/Documents/otros/SACMEX1.txt'
dircsvsacmex2 = '/home/cesar/Documents/files/SACMEX.csv'
dirscreenshot1= '/home/cesar/Documents/screenshot/menu.png'
dirscreenshot2= '/home/cesar/Documents/screenshot/isoyetas.png'
dirscreenshot3= '/home/cesar/Documents/screenshot/descarga.png'

#Copiar el archivo de SACMEX con la tabla en ceros si es que la hora es entre 6:00 y 6:10 horas.
#Obteniendo la hora actual.
hora_actual=time.strftime("%H:%M")
print("La hora actual es:",hora_actual)
# Se crea un objeto de hora para las 00:00am.
hora_0 = "00:00"
hora_principio = time.strftime(hora_0)
# Se crea un objeto de hora para las 6:00am.
hora_1 = "06:00"
hora_inicio = time.strftime(hora_1)
print(hora_inicio)
# Se crea un objeto de hora para las 6:10am.
hora_2 = "06:10"
hora_final = time.strftime(hora_2)
print(hora_final)

#Comprobando la hora, de ser las 6am, se compiara una tabla con los valores de las estaciones en 0mm para evitar algun valor negativo.
print("Comprobando corte de datos a las 6am")
if hora_inicio <= hora_actual <= hora_final:
    shutil.copy(dircsvsacmex0,dircsvsacmex0_0)
    print("Se reemplazo el archivo SACMEX0 debido al corte de datos")
elif hora_inicio != hora_actual != hora_final:
    print("El corte de datos es a las 06:00 am")

# Se obtiene la fecha con cambio de formato.
fecha_a= date.today()
print(fecha_a)

# Establecemos el parametro de la fecha para despues con el bot colocarla en el datapicker del navegador web.
# Primero verificamos la fecha para asignar la del día en curso, hay que recordar que el corte de datos es a las 6 am
print("Estableciendo fechas para la descarga de los al corte")
now=datetime.now()
fecha_0=(now.strftime("%d/%m/%Y"))
fecha_1=now - timedelta(days=1)
fecha_2=(fecha_1.strftime("%d/%m/%Y"))
print(fecha_0)
print(fecha_2)

# Establecemos el parametro de la fecha de los datos actuales dependiendo de la hora, si la hora actual esta entre las 00:00 y las 06:00 horas, 
# se seguira obteniendo los datos del dia anterior, despues de las 06:00 horas se obtendran los datos de la fecha en curso.
print("Comprobando la fecha para la obtención de los datos de la fecha correspondiente al corte.")
if hora_principio <= hora_actual <= hora_inicio:
    fecha_datapicker=fecha_2
    fecha=fecha_a-timedelta(days=1)
    print("La fecha a colocar en el datapicker de SACMEX es", fecha_datapicker,"debido a que aun no se realiza el corte de los datos")
    print("La fecha del archivo descargado de SACMEX es", fecha,"debido a que aun no se realiza el corte de los datos")
elif hora_principio != hora_actual != hora_inicio:
    fecha_datapicker=fecha_0
    fecha=fecha_a
    print("La fecha a colocar en el datapicker de SACMEX es", fecha_datapicker,"debido a que ya se realizo el corte de los datos")
    print("La fecha del archivo descargado de SACMEX es", fecha,"debido a que ya se realizo el corte de los datos")

print(fecha_datapicker)
print(fecha)

# Se modifica el formato de la fecha con el mes en texto.
def current_date_format(date):
    #date tomara la fecha del sistema para despues cambiar las fechas con el formato de message.
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.strftime("%d")
    month = months[date.month - 1]
    year = date.year
    messsage = "{}{}{}".format(day, month, year)
    #Retornamos el nuevo formato de current_date_format, para usar este nuevo formato debemos mencionarlo al momento de mandar a llamar un date
    return messsage

#Ya con el nuevo formato para las fechas actualizamos el formato.
fecha_final_lluvia0=(current_date_format(fecha))
fecha_final_lluvia=str(fecha_final_lluvia0)
print(fecha_final_lluvia)



OP_DRIVER = Options()
#OP_DRIVER.add_argument("--headless")
OP_DRIVER.add_argument("--disable-gpu")  # Necesario en algunos sistemas
OP_DRIVER.add_argument("--window-size=1920,1080")  # Tamaño de ventana
#OP_DRIVER.add_argument("--start-maximized")
OP_DRIVER.add_argument("--no-sandbox")  # Necesario en algunos sistemas

# Ruta de la carpeta de descargas personalizada
OP_DRIVER.add_argument("--disable-software-rasterizer")
OP_DRIVER.add_argument("--disable-extensions")
OP_DRIVER.add_argument("--disable-gpu")
OP_DRIVER.add_argument("--disable-dev-shm-usage")
OP_DRIVER.add_argument("--remote-debugging-port=9222")

# Ruta de la carpeta de descargas personalizada
download_path = "/home/cesar/Documents/temporal"
prefs = {"download.default_directory": download_path}
OP_DRIVER.add_experimental_option("prefs", prefs)


# Configura el servicio del Chrome WebDriver con webdriver_manager, para este caso, ya tenemos descargado un controlador acorde a la versión de chrome 114.0.5735.90
# Para descargar el controlador se debe ingresar la siguiente instrucción en terminal "google-chrome --version", visitar la siguiente página: "https://sites.google.com/chromium.org/driver/downloads" y descargar la versión que corresponde.
driver=webdriver.Chrome(service=Service(executable_path=ruta_webdriver),chrome_options=OP_DRIVER)

# Configura el servicio del Chrome WebDriver con webdriver_manager, este descargara automaticamente el controlador mas apto para la versión de chrome instalada
#driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=OP_DRIVER)


driver.get('http://10.11.11.154/SACMEX/')
driver.implicitly_wait(5)
print("Ya en menu")
# Se toma la captura de pantalla menu
driver.save_screenshot(dirscreenshot1)
#print("Se tomo screenshot menu")

# El bot realizara los pasos o clicks a seguir para descargar los datos de la plataforma
# click en informes
driver.find_element(By.XPATH, '//*[@id="menu"]/ul/li[3]/a')\
    .click()
print("Click en informes")
time.sleep(5)
# click en isoyetas
driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div[1]/ul/li[7]/a")\
    .click()
driver.save_screenshot(dirscreenshot2)
print("Click en isoyetas")
time.sleep(5)

print("Ventana emergente")
span=driver.find_element(By.CSS_SELECTOR, "#tab4_7 > iframe")
print("Cambio de ventana")
driver.switch_to.frame(span)

print("Selecciona la fecha actual")
driver.find_element(By.XPATH,"//*[@id='form:calendar_input']")\
    .clear()\


#Si inserta la fecha actual en el datapicker.
driver.find_element(By.XPATH,"//*[@id='form:calendar_input']")\
.send_keys(fecha_datapicker)

#Selecciona descargar en .DAT
print("Selección del archivo .DAT")
driver.find_element(By.CSS_SELECTOR,"#form\:j_idt20 > span")\
    .click()

#Tiempo de espera para que salga la nueva ventana de descarga.
time.sleep(5)

#Selecciona Descargar
print("Se descarga el archivo")
driver.find_element(By.XPATH,"//*[@id='formDownload:j_idt31']/span").click()
time.sleep(15)
driver.save_screenshot(dirscreenshot3)
driver.close()
print("Se cierra el navegador")

