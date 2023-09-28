import os
import time  
import shutil
import glob
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import urllib.request
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Ruta del ejecutable del Chrome WebDriver
ruta_webdriver = '/home/cesar/Documents/sgirpcpythonlinux/chromedriver-linux64/chromedriver-exe'
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio "+path+" ha sido creado")
    else:
        print("El directorio "+path+" ya existe")
pathscreenshot="../screenshot"
makedir(pathscreenshot)
dirscreenshot1= '/home/cesar/Documents/screenshot/carga_datos.png'


try:
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
    
    # Configura el servicio del Chrome WebDriver con webdriver_manager, para este caso, ya tenemos descargado un controlador acorde a la versión de chrome 114.0.5735.90
    # Para descargar el controlador se debe ingresar la siguiente instrucción en terminal "google-chrome --version", visitar la siguiente página: "https://sites.google.com/chromium.org/driver/downloads" y descargar la versión que corresponde.
    driver=webdriver.Chrome(service=Service(executable_path=ruta_webdriver),chrome_options=OP_DRIVER)


    # Configura el servicio del Chrome WebDriver con webdriver_manager, este descargara automaticamente el controlador mas apto para la versión de chrome instalada
    #driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=OP_DRIVER)

    
    driver.get('http://localhost/estacionesMet/control/cargaSgirpc.php')
    driver.implicitly_wait(60)
    driver.get_screenshot_as_file(os.getcwd()+dirscreenshot1)
    time.sleep(5)
    driver.close()

    # # Se instala de forma automatica el controlador de chrome,
    # # de igual manera de establece el parametro de visualización de la pantalla y establece la dirección web
    # inicio=datetime.now()
    # print(inicio)
    # driver=webdriver.Chrome(ChromeDriverManager().install())
    # driver.maximize_window()
    # driver.get('http://192.168.20.17:8080/estacionesMet/control/cargaSgirpc.php')
    # driver.implicitly_wait(50)
    # time.sleep(5)
    # driver.close()

    print("Se han abierto la pestaña cargaSgirpc.php en el navegador de Chrome para la carga de datos en la base SQL")
except:
    print("No se logro la carga de datos en la base SQL debido a algún fallo, revise la conexión a internet o el programa cargaSgirpc.php ")

final=datetime.now()
print(final)
