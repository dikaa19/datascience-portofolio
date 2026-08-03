<<<<<<< HEAD
# 🚀 Bareksa Demo - MCP & Gemini AI Practice

Proyek ini adalah demonstrasi implementasi **Model Context Protocol (MCP)** menggunakan [FastMCP](https://github.com/jlowin/fastmcp) yang diintegrasikan dengan **Google Gemini API** (`google-genai` SDK) untuk melakukan analisis data penjualan SBN (Surat Berharga Negara).

---

## 🌟 Fitur Utama

1. **MCP Server (`server.py`)**:
   - Menyediakan tool analisis data berbasis Pandas dari file dataset `data/sbn_sales_per_series.csv`.
   - Tool yang tersedia:
     - `hello`: Sapaan dasar.
     - `get_total_sales`: Menghitung total akumulasi penjualan SBN.
     - `top_product`: Menampilkan produk SBN teratas (atau terendah) berdasarkan kriteria penjualan, jumlah investor, frekuensi transaksi, atau rata-rata pembelian.
     - `get_sales_data`: Mengambil detail data penjualan untuk kode produk SBN tertentu.

2. **MCP Client Test (`client.py`)**:
   - Pengujian terisolasi untuk memastikan MCP Server dan semua tool berjalan lancar via FastMCP Client.

3. **Gemini AI Chat Assistant (`gemini_chat.py`)**:
   - Asisten AI interaktif yang memanfaatkan **Gemini API** (`gemini-flash-lite-latest` / model berkuota tinggi).
   - Secara otomatis mendeteksi dan memanggil MCP Tools (Function Calling) untuk menjawab pertanyaan pengguna dalam bahasa natural.

---

## 📁 Struktur Proyek

```text
mcp_practice/
├── data/                         # Folder data lokal (Diabaikan oleh Git)
│   └── sbn_sales_per_series.csv.example  # Template skema data
├── server.py                     # Implementasi MCP Server (FastMCP)
├── client.py                     # Script pengetesan MCP Client
├── gemini_chat.py                # Asisten Chat Gemini API + MCP Tools
├── .env.example                  # Template konfigurasi environment variable
├── .gitignore                    # Konfigurasi pengabaian file sensitif Git (env & data)
├── requirements.txt              # Daftar dependensi Python
└── README.md                     # Dokumentasi proyek
```

---

## 🛠️ Instalasi & Persiapan

### 1. Clone Repository & Setup Virtual Environment
```bash
git clone <URL_REPOSITORY_ANDA>
cd mcp_practice

# Membuat virtual environment
python -m venv .venv

# Aktivasi virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
# Aktivasi virtual environment (Linux/Mac)
source .venv/bin/activate
```

### 2. Install Dependensi
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables & Data
1. Buat file `.env` berdasarkan template `.env.example`:
   ```bash
   cp .env.example .env
   ```
   Buka file `.env` dan isi `GEMINI_API_KEY` Anda:
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

2. Siapkan file dataset Anda sendiri di folder `data/`:
   - Buat folder `data/` jika belum ada.
   - Letakkan file CSV Anda dengan nama `data/sbn_sales_per_series.csv` (lihat contoh skema di `data/sbn_sales_per_series.csv.example`).

---

## 💻 Cara Menjalankan

### A. Uji Coba MCP Tools (`client.py`)
Jalankan pengujian fungsi MCP Server tanpa API luar:
```bash
python client.py
```

### B. Chat dengan Gemini AI Assistant (`gemini_chat.py`)
Jalankan asisten AI berbasis Gemini yang terhubung dengan MCP Tools:
```bash
python gemini_chat.py
```

**Contoh Pertanyaan yang Bisa Diajukan:**
- *"Berapa total penjualan SBN?"*
- *"Produk apa yang memiliki jumlah investor tertinggi?"*
- *"Berapa penjualan untuk produk ST006?"*
- *"Produk dengan penjualan terendah apa?"*

### C. Menjalankan MCP Server Standalone (`server.py`)
```bash
python server.py
```

---

## 🔐 Keamanan Data
File sensitif seperti file konfigurasi `.env` (API Key) dan seluruh isi folder `data/` (beserta file `*.csv`) telah ditambahkan ke [.gitignore](file:///d:/Exercise/mcp_practice/.gitignore) agar **TIDAK TER-PUSH** ke GitHub.
=======
# Data Scientist Portfolio

## Tentang Saya
Saya adalah seorang mahasiswa Ilmu Komputer yang antusias dan berdedikasi dengan semangat yang besar untuk belajar dan berkembang di bidang data science.

## Keahlian
- **Pemrograman:** Python (pandas, numpy, scikit-learn, matplotlib, seaborn), SQL
- **Machine Learning:** Supervised dan Unsupervised Learning, Feature Engineering, Hyperparameter Tuning
- **Pengolahan Data:** Data Cleaning, Exploratory Data Analysis (EDA), Data Preprocessing
- **Teknologi:** Google Colab, Visual Studio Code, Git/GitHub

## Proyek Saya
### Garment Worker Productivity
Tujuan utama adalah memprediksi efektivitas dan efisiensi buruh di pabrik garmen. Dengan melakukannya, perusahaan bertujuan untuk:
- Mengidentifikasi penurunan kinerja buruh sehingga intervensi bisa segera dilakukan.
- Meningkatkan efisiensi operasional melalui alokasi sumber daya yang lebih baik.

**Key Business Questions**
- Apa saja faktor yang paling mempengaruhi produktivitas buruh?
  - Memahami variabel mana yang paling mempengaruhi produktivitas buruh seperti jumlah pekerja, jumlah perubahan desain, lembur, dan insentif.
- Bagaimana kita dapat membangun model untuk memprediksi produktivitas buruh secara akurat?
  - Mengembangkan model prediktif untuk memperkirakan produktivitas berdasarkan data historis dan faktor-faktor yang relevan.
- Tindakan apa yang bisa diambil untuk meningkatkan atau menjaga produktivitas buruh?
  - Mengidentifikasi langkah-langkah yang dapat diambil dari hasil prediksi untuk meningkatkan atau mempertahankan produktivitas buruh .

**Algoritma yang digunakan:** Regresi Linear, KNN, Decision Tree, Random Forest, SVM, dan MLP

**Hyperparameter Tuning**: GridSearch

**Hasil:** Random Forest menjadi model terbaik dengan RMSE sebesar 0.114971 dan SMAPE 10.996979

**Dokumentasi Kode**:  https://github.com/dikaa19/datascience-portofolio/blob/main/garment_worker_productivity.ipynb

---
### Customer Segmentation
**Tujuan Proyek:** Menganalisis dan mengelompokkan pelanggan berdasarkan data transaksi online retail.

**Key Business Question**
  1. Apa saja segmen utama pelanggan yang ada berdasarkan pola pembelian mereka?
  2. Bagaimana distribusi geografis pelanggan berdasarkan segmen tersebut?
  3. Strategi pemasaran apa yang dapat diterapkan untuk masing-masing segmen pelanggan?
     
**Algoritma yang digunakan:** KMeans Clustering

**Hasil:** Mendapatkan nilai sillhoute score sebesar 0.81 (sangat baik)

**Dokumentasi Kode:** https://github.com/dikaa19/datascience-portofolio/blob/main/[Clustering]_Submision_Akhir_BMLP_Khafidz_Putra_Mahardika.ipynb

---
### Rice Seed Classification
**Bahasa Pemrograman:** Python

**Latar Belakang**

Dalam industri pertanian, identifikasi tipe padi menjadi aspek penting untuk memastikan kualitas dan efisiensi produksi. Dua tipe padi utama dalam dataset ini adalah Jasmine dan Gonen, yang memiliki karakteristik berbeda, baik dari segi fisik maupun kualitas hasil panen. Identifikasi manual seringkali tidak efisien dan rawan kesalahan, terutama untuk volume besar. Dengan dataset yang mencakup fitur geometris butir padi seperti Area, Perimeter, dan Roundness, pendekatan machine learning dapat membantu mengotomatisasi proses klasifikasi ini. Hal ini bertujuan meningkatkan akurasi, efisiensi, dan kecepatan identifikasi.

**Masalah Bisnis:** Bagaimana membangun model machine learning yang mampu mengklasifikasikan dua tipe padi, Jasmine dan Gonen, secara otomatis berdasarkan fitur geometrisnya?

**Tujuan Proyek:** 

1. Membangun model klasifikasi yang dapat memanfaatkan fitur geometris seperti Area, Eccentricity, dan Roundness untuk membedakan padi Jasmine dan Gonen.
2. Melakukan evaluasi model menggunakan metrik seperti akurasi, precision, recall, F1-score, dan confusion matrix untuk memastikan performa optimal.
3. Menghasilkan model yang dapat diterapkan pada dataset baru dengan performa konsisten.

**Algoritma yang digunakan:** GaussianNB, LinearSVC, dan DecisionTreeClassifier

**Hasil:** Model GaussianNB, LinearSVC, dan DecisionTree mampu memprediksi jenis padi dengan **Sangat Baik** berdasarkan fitur-fitur yang tersedia. Nilai Akurasi model-model ini mencapai 100% pada algoritma LinearSVC dan DecisionTree, sedangkan untuk algoritma GaussianNB tingkat akurasinya sebesar 99.46%. Hal ini menunjukkan model memiliki kemampuan generalisasi yang baik terhadap data yang diberikan.

**Dokumentasi Kode:** https://github.com/dikaa19/datascience-portofolio/blob/main/rice_clasification.ipynb

---
### SQL Analysis: Airline Passenger Satisfaction

**Bahasa Pemrograman:** Python dan SQL

**Recommend Analysis:**

1. Which percentage of airline passengers are satisfied? Does it vary by customer type? What about type of travel?
2. What is the customer profile for a repeating airline passenger?
3. Does flight distance affect customer preferences or flight patterns?
4. Which factors contribute to customer satisfaction the most? What about dissatisfaction?
5. What is the average departure delay and arrival delay?
6. What is the Average rating of On-board Service and Airline Service?

**Dokumentasi Kode:** https://github.com/dikaa19/datascience-portofolio/blob/main/airplane_passenger_satisfaction.ipynb

---

## Kontak
- **Linkedin:** www.linkedin.com/in/khafidz-putra-mahardika
- **Github:** https://github.com/dikaa19
- **Email:** khafidzputra93@gmail.com
>>>>>>> ce16e675acb814d2a01d809a8dd166f0efbd2074
