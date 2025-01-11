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

**Hasil:** Model GaussianNB, LinearSVC, dan DecisionTree mampu memprediksi jenis padi dengan **Sangat Baik** berdasarkan fitur-fitur yang tersedia. Nilai Akurasi model-model ini mencapai 100% pada algoritma LinearSVC dan DecisionTree, sedangkan untuk algoritma GaussianNB tingkat akurasinya sebesar 99.43%. Hal ini menunjukkan model memiliki kemampuan generalisasi yang baik terhadap data yang diberikan

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

**Dokumentasi Kode:** https://github.com/dikaa19/datascience-portofolio/blob/main/airplane_satisfaction.ipynb

---

## Kontak
- **Linkedin:** www.linkedin.com/in/khafidz-putra-mahardika
- **Github:** https://github.com/dikaa19
- **Email:** khafidzputra93@gmail.com
