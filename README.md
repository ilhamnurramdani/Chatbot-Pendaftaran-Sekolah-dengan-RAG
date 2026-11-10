# 🎓 Chatbot Pendaftaran Sekolah Berbasis Retrieval-Augmented Generation (RAG)

<p align="center">
  <b>Intelligent School Admission Assistant</b><br>
  Chatbot AI untuk membantu calon siswa dan orang tua memperoleh informasi pendaftaran sekolah secara cepat, interaktif, dan relevan.
</p>

---

## 📌 Deskripsi Proyek

**Chatbot Pendaftaran Sekolah** merupakan aplikasi berbasis Artificial Intelligence (AI) yang dirancang untuk membantu calon siswa dan orang tua mendapatkan informasi terkait proses penerimaan peserta didik baru (PPDB).

Aplikasi ini menerapkan pendekatan **Retrieval-Augmented Generation (RAG)** yang menggabungkan pencarian informasi berdasarkan basis pengetahuan (*knowledge base*) dengan kemampuan Large Language Model (LLM) dalam menghasilkan jawaban secara natural.

Dengan memanfaatkan **Ollama dan LLaMA 3**, chatbot dapat memproses pertanyaan pengguna dan menghasilkan respons berdasarkan informasi yang relevan dari dokumen atau basis pengetahuan sekolah.

## ✨ Fitur Utama

- 🤖 **AI-Powered Chatbot** – Menjawab pertanyaan pengguna menggunakan model LLaMA 3.
- 🔎 **Retrieval-Augmented Generation** – Mengambil informasi relevan dari knowledge base sebelum menghasilkan jawaban.
- 🧠 **Semantic Search** – Menggunakan SentenceTransformer untuk mengubah teks menjadi representasi embedding.
- 📚 **School Information** – Menyediakan informasi pendaftaran, persyaratan, biaya pendidikan, jadwal, dan prosedur penerimaan.
- ⚡ **Local AI Processing** – Menjalankan model AI secara lokal menggunakan Ollama.
- 💬 **Natural Language Interaction** – Memungkinkan pengguna bertanya menggunakan bahasa sehari-hari.

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| Flask | Backend web application |
| Ollama | Menjalankan LLM secara lokal |
| LLaMA 3 | Model bahasa untuk menghasilkan jawaban |
| SentenceTransformer | Text embedding |
| SQLite | Penyimpanan knowledge base |
| NumPy | Pengolahan data numerik |
| HTML, CSS, JavaScript | Antarmuka aplikasi |

## 🧠 Arsitektur Sistem RAG

Sistem menggunakan pendekatan Retrieval-Augmented Generation dengan alur berikut:

1. **User Input** – Pengguna memasukkan pertanyaan melalui chatbot.
2. **Text Embedding** – Pertanyaan dikonversi menjadi embedding menggunakan SentenceTransformer.
3. **Information Retrieval** – Sistem mencari informasi yang paling relevan dari knowledge base menggunakan cosine similarity.
4. **Context Augmentation** – Informasi hasil pencarian dimasukkan ke dalam prompt.
5. **Response Generation** – LLaMA 3 melalui Ollama menghasilkan jawaban berdasarkan konteks yang diberikan.
6. **Output** – Jawaban ditampilkan kepada pengguna melalui antarmuka chatbot.

## 🔄 Workflow Sistem

```text
        User Question
              |
              v
       Text Embedding
              |
              v
      Semantic Retrieval
              |
              v
       Knowledge Base
              |
              v
      Relevant Context
              |
              v
       Prompt Augmentation
              |
              v
        Ollama - LLaMA 3
              |
              v
       Generated Response
              |
              v
        Chatbot Interface
```

## ⚙️ Instalasi dan Konfigurasi

### 1. Clone Repository

```bash
git clone https://github.com/ilhamnurramdani/Chatbot-Pendaftaran-Sekolah-dengan-RAG.git
```

Masuk ke direktori proyek:

```bash
cd Chatbot-Pendaftaran-Sekolah-dengan-RAG
```

### 2. Buat Virtual Environment

```bash
python -m venv .env
```

Aktifkan virtual environment.

Windows:

```bash
.env\Scripts\activate
```

Linux / macOS:

```bash
source .env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install dan Jalankan Ollama

Unduh Ollama melalui:

https://ollama.com/download

Kemudian unduh model LLaMA 3:

```bash
ollama pull llama3
```

Pastikan Ollama sudah berjalan sebelum menjalankan aplikasi.

### 5. Jalankan Aplikasi

```bash
python app.py
```

Buka browser dan akses:

```text
http://127.0.0.1:5000
```

## 📊 Evaluasi Model

Evaluasi performa chatbot dilakukan menggunakan **BERTScore** untuk mengukur tingkat kesesuaian semantik antara jawaban yang dihasilkan chatbot (*generated answer*) dengan jawaban referensi (*reference answer*).

Pengujian dilakukan terhadap 10 pertanyaan seputar informasi pendaftaran sekolah. Evaluasi menggunakan tiga metrik utama, yaitu Precision, Recall, dan F1-Score.

### Hasil Evaluasi

| Metrik | Nilai Rata-rata |
|---|---:|
| BERTScore Precision | 87% |
| BERTScore Recall | 85% |
| BERTScore F1-Score | 86% |

### Analisis Hasil

Berdasarkan hasil pengujian, chatbot memperoleh nilai rata-rata BERTScore Precision sebesar 87%, Recall sebesar 85%, dan F1-Score sebesar 86%.

Hasil tersebut menunjukkan bahwa chatbot mampu menghasilkan jawaban dengan tingkat kesesuaian semantik yang baik terhadap jawaban referensi. Nilai F1-Score sebesar 86% menunjukkan keseimbangan antara kemampuan sistem dalam mempertahankan relevansi informasi dan menangkap makna dari jawaban referensi.

Dengan demikian, pendekatan Retrieval-Augmented Generation (RAG) yang diterapkan dapat membantu chatbot memberikan respons yang relevan berdasarkan informasi yang tersedia dalam knowledge base.

## 🎯 Tujuan Pengembangan

Proyek ini dikembangkan sebagai implementasi pemanfaatan Artificial Intelligence dan Natural Language Processing (NLP) dalam bidang pendidikan, khususnya untuk:

- Mempermudah akses informasi pendaftaran sekolah.
- Mengurangi ketergantungan pada layanan informasi manual.
- Menerapkan teknologi Generative AI berbasis RAG.
- Mengembangkan chatbot yang mampu memberikan informasi berdasarkan knowledge base yang tersedia.

## 👨‍💻 Author

**Ilham Nur Ramdani**

Mahasiswa Magister Ilmu Komputer – Universitas Budi Luhur.

Interested in:
- Data Science & Data Mining
- Artificial Intelligence & Machine Learning
- Natural Language Processing
- Generative AI & Retrieval-Augmented Generation
- Web Application Development

GitHub: [@ilhamnurramdani](https://github.com/ilhamnurramdani)

---

<p align="center">
  <b>Developed with Python, Flask, and Generative AI</b><br>
  ⭐ If you find this project useful, feel free to give it a star!
</p>
