import os
from pymongo.errors import PyMongoError
from src.models.puntosRec_model import PuntosRecoleccionModel
from src.database.mongo_db import MongoConnetionManager
from fastapi import HTTPException


class PuntosRecoleccionService:
    _database = None
    
    @staticmethod
    def get_database_instance():
        if not PuntosRecoleccionService._database:
            db_host = os.getenv("MONGODB_HOST")
            db_port = int(os.getenv("MONGODB_PORT"))
            db_name = os.getenv("MONGODB_DATABASE")
            db_username = os.getenv("MONGODB_USERNAME")
            db_password = os.getenv("MONGODB_PASSWORD")
            
            PuntosRecoleccionService._database = MongoConnetionManager(host=db_host, port=db_port, database_name=db_name, username=db_username, password=db_password)
            PuntosRecoleccionService._database.connect()
        return PuntosRecoleccionService._database
    
    
    @staticmethod
    def registrar_punto(puntos_recoleccion: PuntosRecoleccionModel):
        try:
            database = PuntosRecoleccionService.get_database_instance()
            coleccionReportes = "Puntos_Recoleccion"
            if not database.existe_id_reporte(coleccionReportes, puntos_recoleccion.prueba):
                database.insert_document(coleccionReportes, puntos_recoleccion.model_dump())
                return {"Mensaje": f"Registro exitoso!!"}, 201  #Mostrado en postman al crear
            else:
                raise HTTPException(status_code=400, detail="Ya existe un punto con ese ID.") 
        except Exception as e:
            print({"Error": f"Error al registrar el nuevo punto: {e}"}), 400
            
    @staticmethod
    def existe_id_reporte_ser(collection_name, id):
        try:
            database = PuntosRecoleccionService.get_database_instance()
            collection = database.db[collection_name]
            result = collection.find_one({"id": id})
            return result is not None
        except PyMongoError as e:
            print(f"Error al intentar verificar la existencia del ID: {e}")
            return False