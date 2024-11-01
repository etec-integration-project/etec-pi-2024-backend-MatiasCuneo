# Matias Cuneo

Teniendo en cuenta que la carpeta /tmp/data esta vacía o no existe, al correr:

### docker compose up --build -d

Si existe un error de conexión con la base de datos, lo más probable es que con solo reiniciar el compose con "docker compose start", el problema se vea arreglado

el resultado esperado del siguiente comando:

### curl http://localhost:8501/

deberia ser:

### 2024-05-07 02:15:19.420019+00:00%

o en ese estilo de fecha y hora


## para probar el CRUD:

al correr el siguiente comando con datos de ejemplo para crear una nueva configuración:

### curl -X POST "http://localhost:8501/predict" -F "file=@/path_to_your_image/image.png"

(siendo la imagen un numero dibujado a mano o similar) el resultado esperado seria un json de este estilo:

### {"success": 3}

el numero que devuelve es la predicción que arroja el modelo en base a la imágen recibida