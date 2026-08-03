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
