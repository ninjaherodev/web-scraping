from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import os
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
#options.add_argument("--headless")

ruta = r"C:\Users\fabio\Documents\chromedriver.exe"
# Verifica que el archivo existe
if not os.path.isfile(ruta):
    raise FileNotFoundError(f"No se encontró chromedriver en la ruta: {ruta}")
service = Service(ruta)
driver = webdriver.Chrome(service=service, options=options)


driver.get('http://demo-store.seleniumacademy.com/')