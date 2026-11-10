import json 
import pandas as pd
import mysql.connector

from sentence_transformers import SentenceTransformer

# membuat instance untukk embedding model
model = SentenceTransformer("BAAI/bge-m3")

# koneksi ke database
db = connection = mysql.connector.connect(
  host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
  port = 4000,
  user = "2CRtcPpAtdLfW78.root",
  password = "AyILLaPC8II2N0WK",
  database = "RAG",
  ssl_ca = "isrgrootx1.pem",
  ssl_verify_cert = True,
  ssl_verify_identity = True
)

curr = db.cursor()

df = pd.read_csv("data_knowledge_manda.csv")

for index, row in df.iterrows():
    
    text = str(row['question']) + " " + str(row['answer'])

    try:    
        embedding = model.encode(text).tolist()
        embedding_json = json.dumps(embedding)

        sql = "INSERT INTO documents (text, embedding) VALUES (%s, %s)"
        val = (text, embedding_json)
        curr.execute(sql, val)
        
    except Exception as e:
        print(f"Error processing row {index}: {e}")
  
db.commit()


