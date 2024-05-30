Matias Cuneo

Teniendo en cuenta que la carpeta /tmp/data esta vacía o no existe, al correr:

docker compose up --build -d

el resultado esperado del siguiente comando:

curl http://localhost:5000

deberia ser:

2024-05-07 02:15:19.420019+00:00%

o en ese estilo de fecha y hora


para probar el CRUD:

al correr el siguiente comando con datos de ejemplo para crear una nueva configuración:

curl -X POST -H "Content-Type: application/json" -d '{"layersNum":3,"neuronsNum":2,"optimizer":"Adam","lossFunc":"MSE","alpha":2.5,"weightsId":"1234"}' http://localhost:5000/create_config/652132eb-82a0-406c-9c7c-7d3d0088c88b

el resultado esperado es:

{
  "success": "User Config added successfully!"
}

entonces al correr:

curl http://localhost:5000/configs

el resultado esperado debería ser:

{
  "success": [
    {
      "alpha": 2.5,
      "id": "5b09c6be-86c1-48c7-88c6-dfef763633b4", <-- id autogenerado con uuid
      "layersNum": 3,
      "lossFunc": "MSE",
      "neuronsNum": 2,
      "optimizer": "Adam",
      "userId": "652132eb-82a0-406c-9c7c-7d3d0088c88b",
      "weightsId": "1234"
    }
  ]
}

para poder modificarlo, correr el siguiente comando con datos de ejemplo (reemplazando el id por el correspondiente uuid):

curl -X PATCH -H "Content-Type: application/json" -d '{"neuronsNum":5,"optimizer":"SGD"}' http://localhost:5000/update_config/5b09c6be-86c1-48c7-88c6-dfef763633b4

el resultado esperado es:

{
  "success": "Config updated successfully!"
}

esto debería verse reflejado en la configuración del usuario con el siguiente comando:

curl http://localhost:5000/usrconfig/652132eb-82a0-406c-9c7c-7d3d0088c88b

siendo el resultado esperado la configuración con los datos de ejemplo modificados:

{
  "success": {
    "alpha": 2.5,
    "id": "5b09c6be-86c1-48c7-88c6-dfef763633b4",
    "layersNum": 3,
    "lossFunc": "MSE",
    "neuronsNum": 5,
    "optimizer": "SGD",
    "userId": "652132eb-82a0-406c-9c7c-7d3d0088c88b",
    "weightsId": "1234"
  }
}