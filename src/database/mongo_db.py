import pymongo
from bson import ObjectId
from fastapi import HTTPException


class MongoConnetionManager:
    _intance = None
    
    def __new__(cls, host, port, database_name, username, password):
        if not cls._intance:
            cls._intance = super(MongoConnetionManager, cls).__new__(cls)
            cls._intance.client = None
            cls._intance.host = host
            cls._intance.port = port
            cls._intance.username = username
            cls._intance.password = password
            cls._intance.database_name = database_name
            cls._intance.connect()
        return cls._intance
    
    
    def connect(self):
        try:
            if not self.client:
                self.client = pymongo.MongoClient(host= self.host, port=self.port, username=self.username, password=self.password)
                print("Conectado a mongoDB {self.host}:{self.port}")
                self.db = self.client[self.database_name]
            print("conexión exitosa!!")
        except pymongo.errors.ServerSelectionTimeoutError as e:
            print("error al conectar")
            
            
    def close_connection(self):
        if self.client:
            self.client.close()
            print("conexión cerrada!!")
            
            
    def existe_id_punto(self, collection_name, id):
        try:
            collection = self.db[collection_name]
            result = collection.find_one({"id": id})
            return result is not None
        except Exception as e:
            print("Error al verificar la existencia del ID del punto", e)
            return False
        
            
    def insert_document(self, collection_name, document):
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(document)
            print("Documento creado en mongoDB:", result.inserted_id)
        except Exception as e:
            print("Error al insertar documento:", e)
            
            
    def get_all_documents(self, collection_name):
        try:
            collection = self.db[collection_name]
            result = list(collection.find())
            documents = {}
            for idx, doc in enumerate(result):
                document_dict = {}
                for key, value in doc.items():
                    if isinstance(value, ObjectId):
                        document_dict[key] = str(value)
                    else:
                        document_dict[key] = value
                documents[idx] = document_dict
            return documents
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error al obtener los puntos: {e}")
        
        
    def buscar_punto_por_id(self, collection_name, id):
        collection = self.db[collection_name]
        result = list(collection.find({"id": id}))
        if not result:
            return "Error: No se encuentra punto con ese ID"
        reportes = []
        for doc in result:
            document_dict = {}
            for key, value in doc.items():
                if isinstance(value, ObjectId):
                    document_dict[key] = str(value)
                else:
                    document_dict[key] = value
            reportes.append(document_dict)
        return reportes


    def actualizar_punto_por_id(self, collection_name, id, document):
        try:
            collection = self.db[collection_name]
            result = collection.update_one({"id": id}, {"$set": document})
            if result.matched_count == 0:
                return "Error: No existe punto con ese ID"
            return {"Mensaje": f"Punto con el id {id} actualizado correctamente"}, 200
        except Exception as e:
            print("Error al intentar actualizar el punto de recolección:", e)
            return False
    
            
    def eliminar_punto_por_id(self, collection_name, id):
        try:
            collection = self.db[collection_name]
            result = list(collection.find({"id": id}))
            if not result:
                return "Error: No existe punto con ese ID"
            result = collection.delete_one({"id": id})
            return {"Mensaje": f"Reporte con el id {id} eliminado correctamente"}, 200
        except Exception as e:
            print("Error al intentar eliminar el reporte mong:", e)