#####################################################
######## ENVÍO MASIVO DE MENSAJES DE WHATSAPP #######
#####################################################

# Manejo de la pantalla
import pyautogui as pg
# Manejo del browser
import webbrowser as web
# Retraso del tiempo de ejecución
import time
# Para el manejo del archivo CSV
import pandas as pd


# Se abre y se lee el archivo con los datos
# Los datos se transforman en una lista de diccionarios
# con 2 claves: celular y mensaje

# Es necesario que el archivo csv tenga esas 2 columnas: 
# celular y mensaje
# Se recomienda colocar el mensaje entre "" por los signos 
# de puntuación
data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
mensajes = data_dict['mensaje']

# combo posee tuplas (celular, mensaje)
# es lo que hace la función zip
combo = zip(celulares,mensajes)

for celular,mensaje in combo:
    time.sleep(5)

    # Se envía el mensaje en el browser
    web.open("https://web.whatsapp.com/send?phone="+celular+"&text="+mensaje)

    # Se envía el mensaje a través de la aplicación desktop
    # El problema es que hay que cerrar tanto la pestaña del browser
    # como la aplicación

    # Utilizando la API
    # web.open("https://api.whatsapp.com/send/?phone="+celular+"&text="+mensaje)
    # pg.press('enter')

    # Hay que ajustar el tiempo de espera en función de la velocidad 
    # de la conexión
    time.sleep(20)

    # Nos posicionamos el cursor en la mitad de la pantalla
    width,height = pg.size()
    pg.click(width/2,height/2)

    # Damos tiempo para poder enviar el mensaje
    time.sleep(10)
    pg.press('enter')
    time.sleep(20)

    # Cerramos la pestaña del navegador
    # El 'enter' es para el mensaje que sale
    pg.hotkey('ctrl','w')
    pg.press('enter')
    


