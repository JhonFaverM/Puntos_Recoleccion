import pymongo


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
            
    def existe_id_reporte(self, collection_name, id):
        try:
            collection = self.db[collection_name]
            result = collection.find_one({"id": id})
            return result is not None
        except Exception as e:
            print("Error al verificar la existencia del ID del punto")
            return False
            
    def insert_document(self, collection_name, document):
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(document)
            print("Documento creado en mongoDB:", result.inserted_id)
        except Exception as e:
            print("Error al insertar documento:", e)