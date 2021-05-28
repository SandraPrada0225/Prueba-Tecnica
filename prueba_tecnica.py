import pandas as pd
import json
import numpy as np
import requests
from time import time
from pandas import json_normalize
import sqlite3
import hashlib



url1 = "https://restcountries-v1.p.rapidapi.com/all"
url2="https://restcountries.eu/rest/v2/region/"

tabla=pd.DataFrame(columns=['Region','Country Name','Language','Time'])

headers = {
    'x-rapidapi-key': "d0a52052d0msh0806b96b400c6ebp15caf5jsn826fbcdbdc3b",
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.coÑm"
    }
response = requests.request("GET", url1, headers=headers)
df= pd.read_json(response.text)
#obtenemos todas las regiones del primer url
df=df.drop_duplicates(subset=['region'])
df.reset_index(inplace=True, drop=False)
df= df["region"]
for i in range(len(df)-1):
    start_time=time()
    response = requests.get(url2+df[i])
    citus_api_data = json.loads(response.text)
    #obtenemos un pais por region del segundo url a partir de la region obtenida en el punto 1
    nombrePais=citus_api_data[0]["name"]
    #obtenemos el nombre del idioma y lo encriptamos en SHA1
    nycphil = json_normalize(citus_api_data[0], record_path = ['languages'])
    m = hashlib.sha1(str(nycphil["name"].head(1).iloc[0]).encode('utf-8'))
    #m = hashlib.sha1(str(citus_api_data[0]["languages"][0]["name"]).encode('utf-8'))
    #generamos el tiempo en el que se tardo en generar la fila usando la libreria time
    tiempo=time()-start_time
    #añadimos las filas a la tabla creada en pandas 
    tabla = tabla.append(pd.Series([df[i], nombrePais, m.hexdigest(),tiempo], index=['Region','Country Name','Language','Time']), ignore_index=True)



#calculamos el tiempo promedio, total, maximo y minimo con la libreria pandas
tiempo_promedio=tabla["Time"].mean()
tiempo_total=tabla["Time"].sum()*1000
tiempo_minimo=tabla["Time"].min()*1000
tiempo_maximo=tabla["Time"].max()*1000

print(tiempo_promedio)

#Creamos una base de datos en sqlite donde almacenamos los datos calculados en la tabla "datos"
conexion=sqlite3.connect("base_de_datos.db")
cur = conexion.cursor()
try: 
    cur.execute('''CREATE TABLE datos (campo text, tiempo real)''')
    print("se creó la tabla datos")
except sqlite3.OperationalError:
    print("la tabla datos ya existe")

cur.execute("INSERT INTO datos VALUES(?, ?)",('Tiempo Promedio',tiempo_promedio))
cur.execute("INSERT INTO datos VALUES(?, ?)",('Tiempo Total',tiempo_total))
cur.execute("INSERT INTO datos VALUES(?, ?)",('Tiempo Minimo',tiempo_minimo))
cur.execute("INSERT INTO datos VALUES(?, ?)",('Tiempo Maximo',tiempo_maximo))
conexion.commit()
conexion.close()

#generamos un archivo llamado data.json de la tabla creada
print(tabla)
data_json=tabla.to_json('data.json')















