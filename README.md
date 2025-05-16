# 📘 Laporan Proyek Machine Learning

## 🧩 Domain Proyek

**Judul:** *Model Segmentasi Strategi Iklan Pemerintah NYC (Clustering-Based Framework)*

**Latar Belakang:**
Pemerintah kota besar seperti New York City (NYC) memiliki berbagai kampanye iklan yang diluncurkan oleh banyak lembaga pemerintahan. Namun, pendekatan strategi iklan yang digunakan sering kali tidak seragam dan kurang optimal, terutama dari segi pengeluaran anggaran dan efektivitas media. Melalui pendekatan *machine learning*, khususnya *clustering* dan *classification*, proyek ini bertujuan untuk mengidentifikasi pola strategi periklanan yang paling cocok berdasarkan atribut kampanye.

**Alasan Masalah Ini Perlu Diselesaikan:**

- Optimalisasi anggaran publik sangat penting bagi pemerintah.
- Strategi iklan yang tepat dapat meningkatkan partisipasi masyarakat.
- Tidak semua jenis kampanye cocok untuk semua media atau besaran anggaran.

**Referensi:**
Data diperoleh dari NYC Open Data: [https://data.cityofnewyork.us](https://data.cityofnewyork.us)

## 🧠 Business Understanding

### Problem Statement

Bagaimana cara mengelompokkan kampanye iklan pemerintah berdasarkan karakteristik kampanye untuk kemudian mengembangkan model klasifikasi yang dapat merekomendasikan strategi periklanan optimal?

### Goals

- Melakukan segmentasi kampanye iklan berdasarkan atribut yang tersedia.
- Mengembangkan model klasifikasi yang mampu memprediksi jenis strategi iklan yang optimal berdasarkan data historis kampanye.

### Solution Statement

1. Menggunakan *Agglomerative Clustering* untuk segmentasi kampanye berdasarkan data numerik (Spend Amount).
2. Menggunakan *Logistic Regression* untuk membuat model klasifikasi yang mampu memprediksi strategi iklan berdasarkan atribut seperti media, bahasa, jenis kampanye, dan lainnya.
3. Menggabungkan hasil clustering sebagai label untuk melatih tiga model klasifikasi sekaligus (*ensemble model*), yang kemudian dievaluasi secara gabungan.

## 📊 Data Understanding

**Sumber Data:** NYC Government Ad Spend Data

- URL: [https://data.cityofnewyork.us](https://data.cityofnewyork.us)

**Ukuran Dataset:** 18.000+ baris data historis

**Contoh Fitur Penting:**

- `Spend Amount`: Total pengeluaran kampanye
- `Purpose`: Tujuan kampanye (Rekrutmen, Edukasi, Kesehatan, dll)
- `Type of Media`: Jenis media iklan
- `Language`: Bahasa yang digunakan
- `Agency`: Lembaga penyelenggara kampanye

### EDA & Visualisasi:

- Histogram jumlah kampanye per agensi
- Korelasi pengeluaran vs media
- Distribusi pengeluaran berdasarkan kategori kampanye

## 🧹 Data Preparation

**Langkah-langkah yang Dilakukan:**

1. *Cleaning*: Menghapus duplikat dan menangani missing value
2. *Encoding*: Mengubah data kategorikal menjadi numerik
3. *Normalization*: Untuk fitur numerik seperti pengeluaran
4. *Clustering Labels*: Hasil *clustering* digunakan sebagai label pelatihan model klasifikasi

**Alasan:**

- Encoding dibutuhkan untuk model ML
- Clustering diperlukan karena tidak ada label klasifikasi awal
- Normalisasi agar algoritma tidak bias terhadap fitur ber-skala besar

## 🤖 Modeling

### Clustering:

- Algoritma: **Agglomerative Clustering**
- Fitur utama: `Spend Amount`
- Hasil: 3 klaster yang dibedakan sebagai Cluster 0, 1, dan 2

| Cluster | Ukuran (%) | Rata-rata Pengeluaran | Rentang         | Karakteristik                         |
| ------- | ---------- | --------------------- | --------------- | ------------------------------------- |
| 0       | 24.79%     | \$4,028               | \$2,192–\$4,956 | Kampanye besar dan prioritas          |
| 1       | 52.31%     | \$162                 | \$2–\$871       | Kampanye efisien, biaya rendah        |
| 2       | 22.90%     | \$1,346               | \$573–\$2,324   | Kampanye menengah, kombinasi strategi |

### Klasifikasi:

- Model: **Logistic Regression** (dengan ensemble dari 3 model berbeda)
- Fitur: Media, Bahasa, Vendor, Agency, Purpose, dll

**Evaluasi Model Gabungan:**

- **Accuracy:** 0.9803
- **Precision:** 0.8736
- **Recall:** 0.9818
- **F1-score:** 0.9151

## 📈 Evaluation

### Metrik Evaluasi:

- **Accuracy:** Persentase prediksi yang benar dari keseluruhan
- **Precision:** Seberapa tepat model memprediksi kategori yang benar
- **Recall:** Seberapa baik model menangkap seluruh contoh dari masing-masing kategori
- **F1-score:** Harmoni antara precision dan recall

### Interpretasi:

- Nilai F1-score 0.91 menunjukkan keseimbangan yang baik antara recall dan precision
- Accuracy yang tinggi menunjukkan keakuratan model secara keseluruhan
- Recall yang sangat tinggi sangat baik dalam konteks pemerintahan karena setiap kampanye yang salah sasaran bisa berdampak besar

## 🏁 Kesimpulan Strategis

- **Cluster 1 = Kampanye Efisien:**  
  Volume tinggi, biaya rendah (rekrutmen, pengumuman lokal)

- **Cluster 0 = Kampanye Prioritas Nasional:**  
  Jangkauan luas, anggaran besar (kesehatan publik, transportasi)

- **Cluster 2 = Kompromi Ideal:**  
  Kombinasi strategi efisiensi dan dampak moderat (edukasi, kesehatan lokal)

Model gabungan berbasis clustering dan klasifikasi ini terbukti dapat merekomendasikan strategi iklan secara efektif, membantu pemerintah dalam menyesuaikan pendekatan per kampanye.

---

**Catatan Tambahan:**

- Proyek dapat dikembangkan lebih lanjut menggunakan fitur temporal (tanggal kampanye)
- Dapat diterapkan sistem rekomendasi real-time untuk memilih strategi iklan optimal
- Model klasifikasi dapat di-update seiring waktu menggunakan data kampanye terbaru
