# Prueba-Tecnica

### Prueba tecnica ZINOBE

##Desarrollo

**1. De https://rapidapi.com/apilayernet/api/rest-countries-v1, obtenga todas las regiones existentes:**
- Registro en  rapidapi.com para tener acceso a los datos.
- Cargamos los datos en un dataframe de la biblioteca pandas.
- Extraemos las regiones existentes eliminando los datos duplicados de la columna 'region' en un nuevo dataFrame.

|Indice          | Region  |
| ------------ | ------------ |
| 0  |  Asia            |
| 1  |  Europe       |
| 2 |  Africa          |
| 3 |  Oceania      |
| 4 |   Americas   |
| 5 |  Polar          |



** 2. De https://restcountries.eu/ Obtenga un pais por region apartir de la region optenida del punto 1:**
- Consultamos el primer pais por cada region obtenida dentro de un for añadiendo el nombre de la region al url.
- Tomamos el nombre del pais de los datos obtenidos.

**3. De https://restcountries.eu/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1:**
-De los datos del pais y dentro del mismo for extraemos la columna ´languages´.
-Realizamos una normalizacion a la columna 'languajes' por ser un JSON anidado y tomamos el nombre del idioma.
-Llevamos a cabo la encriptación SHA1 haciendo uso de la libreria hashlib.

**4. En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico):**
-Con ayuda de la libreria time generamos el tiempo actual al inicio del ciclo for( en el ciclo for se arman las filas) almacenamos el tiempo en una variable como 'tiempo_actual', al finalizar el ciclo for generamos nuevamente el tiempo y lo restamos con la variable 'tiempo_actual', generando asi el tiempo en que tarda en armar una fila.

**5. La tabla debe ser creada en un DataFrame con la libreria PANDAS:**
- Se guardan las filas realizadas dentro de un DataFrame llamado ´tabla´ haciendo uso de la libreria Pandas:


|   |   Region|Country Name   | Language   | Time  |
| :------------: | :------------: | :------------: | :------------: | :------------: |
|  0 |  Asia |    Afghanistan|  cc50b3253c9ec78d83c0178cbd9aff6a66d8ced8 |  0.387430 |
|  1|   Europe|  Åland Islands |  04a422d38c95415cece1ac86e1ad2a1030048c03 | 0.831609|
|  2|  Africa |   Algeria|  af4f4762f9bd3f0f4a10caf5b6e63dc4ce543724 |   0.399655|
|  3 |   Oceania|  American Samoa | 649df08a448ee3fa90f3746baaf6b0907df42c91  |  0.352466 |
|  4|   Americas|  Anguilla |  649df08a448ee3fa90f3746baaf6b0907df42c91 | 0.391062  |
|  5|   Polar|  Antarctica|    649df08a448ee3fa90f3746baaf6b0907df42c91| 0.349763  |


**6. Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla:**

 -Con mean() generamos el tiempo promedio.
 -Con sum() el tiempo total.
 -Con min() el tiempo minimo.
 -Con max() el tiempo maximo.

**7. Guarde el resultado en sqlite:**

- Importamos la libreria sqlite3 y creamos una nueva base de datos llamada base_de_datos.db .
- Generamos una nueva tabla llamada ´datos´ y guardamos los datos.

**8. Genere un Json de la tabla creada y guardelo como data.json:**
-Creamos el archivo data.json con ayuda de la libreria Pandas to_json
