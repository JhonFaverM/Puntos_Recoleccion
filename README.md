# API Documentation
Puntos_Recoleccion

## Microservicio de Gestión de puntos de recoleción ##

Puntos_Recoleccion es un microservicio para gestionar la hubicacion y el estado de los puntos de recoleccción en una base de datos MongoDB a traves de operaciones RESTful.

## Installation

Clona este repositorio en tu maquina local:
git clone https://github.com/

Accede al directorio del proyecto:
cd Puntos_Recoleccion

## Para ejecutar la API
Crear en la raíz del proyecto un entorno virtual con el comando:
`python -m virtualenv env`

`Activa` el entorno virtual accediendo hasta la carpeta env la cual se crea con el comando anterior y ejecuta el siguiente comando:
PS C:\Puntos_Recoleccion\env> `.\Scripts\activate`
Deberia la ruta verse como en este ejemplo para asegurarse que el entorno virtual esta activo:
`(env)` PS C:\Puntos_Recoleccion\env>

Instala las dependencias necesarias utilizando pip:
pip install -r requirements.txt .

## Crea un archivo `.env` en el directorio raíz del proyecto para las variables de entorno, allí se define la conexión a MongoDB
MONGODB_HOST=localhost
MONGODB_PORT=27018
MONGODB_DATABASE=reportes_usuarios
MONGODB_USERNAME=
MONGODB_PASSWORD=


## Retorna a la carpeta raíz del proyecto e inicia o levanta el servidor con:
(env) PS C:\Puntos_Recoleccion> uvicorn main:app --reload

Para acceder a la documentacion de la API, copia la url y pegala en la web:
http://127.0.0.1:5000/docs


### Endpoints

Para `crear un nuevo punto de recolección`, realiza una solicitud `POST` a la siguiente URL:
http://localhost:5001/Puntos_Recoleccion/
El objeto json a pasar:
    {
        "id": "1",
        "point_status": "optimas condiciones",
        "neighborhood": "Calle 51 # 13-45 Chapinero",
        "coordinates": [5.53528, -73.36778]
    }

Para `obtener todos los puntos creados`, realiza una solicitud `GET` a la siguiente URL:
http://localhost:5001/Puntos_Recoleccion


Para `buscar un punto por ID`, realiza una solicitud `GET` a la siguiente URL, reemplazando {id} con el ID del punto a buscar:
http://localhost:5001/Puntos_Recoleccion/buscar_por_id?id=1


Para `actualizar un punto por ID`, realiza una solicitud `PUT` con el ID del punto a la siguiente URL, y proporciona los datos actualizados en el cuerpo de la solicitud
http://localhost:5002/Puntos_Recoleccion/actualizar_por_id?id=1
{
  "id": "1",
  "description": "Reporte de prueba",
  "username": "usuario1",
  "report_status": "completado"
}


Para `eliminar un reporte por su ID`, realiza una solicitud `DELETE` a la siguiente URL, reemplazando {id} con el ID del reporte a eliminar:
http://localhost:5002/reportes/eliminar_reporte_por_id?id=1


# Modelo de datos
  id: str
  report_date: datetime = datetime.now()
  description: str
  username: str
  report_status: str

`id` Campo de `tipo str`, representa el identificador unico del reporte de usuario, este campo identifica el reporte de manera unica en la base de datos.

`report_date` Campo de `tipo datetime`, especifica la fecha y hora en la que se crea el reporte, por defecto guarda la fecha y la hora en que se crea el reporte `datetime.now()`.

`description` Campo de `tipo str`, Contiene la descripcion o detalles del reporte de usuario, en este campo se proporciona informacion detallada de la situacion a reportar.

`username` Campo de `tipo str`, contiene el campo para registrar el nombre de usuario creador del reporte.

`report_status` Campo de `tipo str`, indica el estado actual del reporte, se validara mediante dos opciones, `pendiente o completado`.

