Matias Cuneo

Al correr:

docker compose up --build -d

el resultado esperado del siguiente comando:

curl http://localhost:5000

deberia ser:

2024-05-07 02:15:19.420019+00:00%

o en ese estilo de fecha y hora


curl:

curl -X POST -H "Content-Type: application/json" -d '{"layersNum":3,"neuronsNum":2,"optimizer":"Adam","lossFunc":"MSE","alpha":2.5,"weightsId":"1234"}' http://localhost:5000/create_config/652132eb-82a0-406c-9c7c-7d3d0088c88b