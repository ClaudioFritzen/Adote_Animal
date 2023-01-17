from decouple import config
from pymongo import MongoClient

MONGO_URI = config('MONGO_URI')
MONGO_DBNAME = config('MONGO_DBNAME')

client = MongoClient(MONGO_URI)
db = client[MONGO_DBNAME]

# Teste de conexão
try:
    client.server_info()
    print("Conexão com o MongoDB Atlas realizada com sucesso!")
except Exception as e:
    print("Erro ao se conectar ao MongoDB Atlas:", e)
