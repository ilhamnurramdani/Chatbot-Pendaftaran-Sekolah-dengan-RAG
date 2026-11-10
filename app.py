import mysql.connector
import json
import ollama
from sentence_transformers import SentenceTransformer
from flask import Flask, redirect, render_template, request, jsonify, url_for

# --- Inisialisasi Aplikasi Flask ---
app = Flask(__name__)

# --- Konfigurasi dan Koneksi Awal (SAMA SEPERTI KODE LAMA ANDA) ---
OLLAMA_HOST = "http://127.0.0.1:11434"
OLLAMA_MODEL = "llama3:8b"

llm_agent = ollama.Client(host=OLLAMA_HOST)
model = SentenceTransformer("BAAI/bge-m3")

# Koneksi ke database (sebaiknya ditaruh di luar fungsi agar koneksi tetap ada)
try:
    db = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        port=4000,
        user="2CRtcPpAtdLfW78.root",
        password="AyILLaPC8II2N0WK", 
        database="RAG",
        ssl_ca="isrgrootx1.pem",
        ssl_verify_cert=True,
        ssl_verify_identity=True
    )
    print("Koneksi ke database berhasil!")
except mysql.connector.Error as err:
    print(f"Error koneksi ke database: {err}")
    db = None

# --- Fungsi Logika Chatbot (SAMA SEPERTI KODE LAMA ANDA) ---
def search_document(database, query, k_top=5):
    if not database or not database.is_connected():
        return [{"text": "Koneksi database terputus.", "distance": 0}]

    result = []
    query_embedding = model.encode(query).tolist()
    query_embedding_json = json.dumps(query_embedding)
    
    curr = database.cursor()
    sql = f"""
    SELECT text, vec_cosine_distance(embedding, %s) AS distance
    FROM documents 
    ORDER BY distance ASC
    LIMIT {k_top}"""
    
    curr.execute(sql, (query_embedding_json,))
    search_results = curr.fetchall()
    curr.close()
    
    for row in search_results:
        text, distance = row
        result.append({"text": text, "distance": distance})
    return result

def response_query(database, query):
    retrieved_docs = search_document(database, query)
    
    if not retrieved_docs:
        return "Maaf, saya tidak dapat menemukan informasi yang relevan."

    context = "\n".join([f"{doc['text']}" for doc in retrieved_docs])
    prompt = f"Berikan jawaban yang akurat dan ringkas berdasarkan konteks berikut:\n\n{context}\n\nPertanyaan: {query}\nJawaban:"
    
    try:
        response = llm_agent.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Terjadi error saat menghubungi LLM: {e}"

# --- Rute Flask (BAGIAN BARU) ---

# Rute untuk halaman utama
@app.route("/")
def home():
    # Menampilkan file index.html dari folder templates
    return render_template("index.html")

# Rute untuk API chatbot
@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json.get("question")
    if not user_query:
        return jsonify({"answer": "Mohon masukkan pertanyaan."}), 400

    response = response_query(database=db, query=user_query)
    return jsonify({"answer": response})

# ==========================================================
# --- RUTE UNTUK ADMIN PANEL (CRUD KNOWLEDGE BASE) ---
# ==========================================================

# READ: Menampilkan semua data knowledge
@app.route("/admin")
def admin_panel():
    if not db or not db.is_connected():
        return "Koneksi database terputus.", 500
    
    curr = db.cursor(dictionary=True) # dictionary=True agar hasil seperti dict Python
    curr.execute("SELECT id, text FROM documents ORDER BY id DESC")
    documents = curr.fetchall()
    curr.close()
    return render_template("admin.html", documents=documents)

# CREATE: Menampilkan form tambah data & memprosesnya
@app.route("/admin/add", methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        question = request.form["question"]
        answer = request.form["answer"]
        
        # Gabungkan pertanyaan dan jawaban menjadi satu teks
        text = str(question) + " " + str(answer)
        
        # Buat embedding
        embedding = model.encode(text).tolist()
        embedding_json = json.dumps(embedding)
        
        # Simpan ke database
        curr = db.cursor()
        sql = "INSERT INTO documents (text, embedding) VALUES (%s, %s)"
        curr.execute(sql, (text, embedding_json))
        db.commit()
        curr.close()
        
        # Kembali ke halaman admin
        return redirect(url_for("admin_panel"))
        
    # Jika method GET, tampilkan form
    return render_template("add_data.html")

# UPDATE: Menampilkan form edit & memprosesnya
@app.route("/admin/edit/<int:doc_id>", methods=["GET", "POST"])
def edit_data(doc_id):
    curr = db.cursor(dictionary=True)
    if request.method == "POST":
        question = request.form["question"]
        answer = request.form["answer"]
        
        text = str(question) + " " + str(answer)
        
        # Buat ulang embedding karena teksnya berubah
        embedding = model.encode(text).tolist()
        embedding_json = json.dumps(embedding)
        
        # Update di database
        update_sql = "UPDATE documents SET text = %s, embedding = %s WHERE id = %s"
        curr.execute(update_sql, (text, embedding_json, doc_id))
        db.commit()
        curr.close()
        
        return redirect(url_for("admin_panel"))
    
    # Jika method GET, ambil data lama dan tampilkan di form
    curr.execute("SELECT id, text FROM documents WHERE id = %s", (doc_id,))
    document = curr.fetchone()
    curr.close()
    
    return render_template("edit_data.html", document=document)

# DELETE: Menghapus data
@app.route("/admin/delete/<int:doc_id>", methods=["POST"])
def delete_data(doc_id):
    curr = db.cursor()
    curr.execute("DELETE FROM documents WHERE id = %s", (doc_id,))
    db.commit()
    curr.close()
    return redirect(url_for("admin_panel"))

# --- Menjalankan Server Flask ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)