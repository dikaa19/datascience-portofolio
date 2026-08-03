# 📊 Data Scientist Portfolio

## Tentang Saya
Saya adalah seorang mahasiswa Ilmu Komputer yang antusias dan berdedikasi dengan semangat yang besar untuk belajar dan berkembang di bidang data science dan AI engineering.

## Keahlian
- **Pemrograman:** Python (pandas, numpy, scikit-learn, matplotlib, seaborn), SQL
- **Machine Learning:** Supervised & Unsupervised Learning, Feature Engineering, Hyperparameter Tuning
- **AI & Integration:** Model Context Protocol (MCP / FastMCP), Google Gemini API (`google-genai`)
- **Pengolahan Data:** Data Cleaning, Exploratory Data Analysis (EDA), Data Preprocessing
- **Teknologi & Tools:** Visual Studio Code, Git/GitHub, Virtualenv

---

## 📁 Struktur Repository

```text
datascience-portofolio/
├── 📁 modelling/       # Kumpulan Proyek Machine Learning & Data Analytics (Jupyter Notebooks)
└── 📁 mcp_practice/   # Implementasi Model Context Protocol (MCP) Server & Integrasi Gemini AI
```

---

## 🚀 Proyek Saya

### 1. 📁 `modelling/` (Machine Learning & Data Analytics)

#### Garment Worker Productivity
Tujuan utama adalah memprediksi efektivitas dan efisiensi buruh di pabrik garmen. Dengan melakukannya, perusahaan bertujuan untuk:
- Mengidentifikasi penurunan kinerja buruh sehingga intervensi bisa segera dilakukan.
- Meningkatkan efisiensi operasional melalui alokasi sumber daya yang lebih baik.

- **Algoritma yang digunakan:** Regresi Linear, KNN, Decision Tree, Random Forest, SVM, dan MLP
- **Hyperparameter Tuning:** GridSearch
- **Hasil:** Random Forest menjadi model terbaik dengan RMSE sebesar 0.114971 dan SMAPE 10.996979
- 📖 **Dokumentasi Kode:** [garment_worker_productivity.ipynb](modelling/garment_worker_productivity.ipynb)

---

#### Customer Segmentation
- **Tujuan Proyek:** Menganalisis dan mengelompokkan pelanggan berdasarkan data transaksi online retail.
- **Algoritma yang digunakan:** KMeans Clustering
- **Hasil:** Mendapatkan nilai silhouette score sebesar 0.81 (sangat baik)
- 📖 **Dokumentasi Kode:** [[Clustering]_Submision_Akhir_BMLP_Khafidz_Putra_Mahardika.ipynb](modelling/[Clustering]_Submision_Akhir_BMLP_Khafidz_Putra_Mahardika.ipynb)

---

#### Rice Seed Classification
- **Latar Belakang & Tujuan:** Membangun model machine learning yang mampu mengklasifikasikan dua tipe padi (Jasmine dan Gonen) secara otomatis berdasarkan fitur geometris.
- **Algoritma yang digunakan:** GaussianNB, LinearSVC, dan DecisionTreeClassifier
- **Hasil:** Model LinearSVC dan DecisionTree mencapai akurasi 100%, sedangkan GaussianNB mencapai 99.46%.
- 📖 **Dokumentasi Kode:** [rice_clasification.ipynb](modelling/rice_clasification.ipynb)

---

#### Airline Passenger Satisfaction (SQL & Data Analysis)
- **Tujuan:** Menganalisis faktor-faktor yang paling mempengaruhi kepuasan pelanggan penerbangan dan profil penumpang berulang.
- 📖 **Dokumentasi Kode:** [airplane_passenger_satisfaction.ipynb](modelling/airplane_passenger_satisfaction.ipynb)

---

### 2. 📁 `mcp_practice/` (Model Context Protocol & AI Agent)

Proyek ini adalah implementasi **Model Context Protocol (MCP)** menggunakan **FastMCP** yang diintegrasikan dengan **Google Gemini API** (`google-genai` SDK) untuk analisis data penjualan SBN (Surat Berharga Negara) secara interaktif.
- **`server.py`**: MCP Server dengan tool `hello`, `get_total_sales`, `top_product`, dan `get_sales_data`.
- **`client.py`**: Pengujian otomatis MCP Server.
- **`gemini_chat.py`**: Asisten AI interaktif Gemini berbasis Function Calling.
- 📖 **[Lihat Dokumentasi Lengkap MCP Practice](mcp_practice/README.md)**

---

## 📬 Kontak
- **LinkedIn:** [khafidz-putra-mahardika](https://www.linkedin.com/in/khafidz-putra-mahardika)
- **GitHub:** [dikaa19](https://github.com/dikaa19)
- **Email:** khafidzputra93@gmail.com
