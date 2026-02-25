# Goruntu isleme ile Yuz Tanıma ve Guvenlik Sistemi

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![DeepFace](https://img.shields.io/badge/AI-DeepFace-green?style=for-the-badge)
![PyQt5](https://img.shields.io/badge/Desktop-PyQt5-orange?style=for-the-badge)

🎓 **Bitirme Projesi — Zonguldak Bülent Ecevit Üniversitesi**

---

## 🎯 Vizyon & Problem Tanımı

Geleneksel güvenlik sistemleri kart, şifre veya manuel kontrol mekanizmalarına dayanmaktadır.  
Bu yöntemler:

- Kart paylaşımı ile güvenlik açığı oluşturabilir  
- Manuel kontrol gerektirir  
- Gerçek zamanlı analiz yapamaz  

Bu proje, **Yapay Zeka destekli yüz tanıma teknolojisi** kullanarak yetkili giriş kontrolünü otomatikleştirmeyi amaçlamaktadır.

Sistem, gerçek zamanlı kamera görüntüsünü analiz eder ve kişiyi doğrulayarak güvenli bir erişim kontrol mekanizması oluşturur.

---

## 🚀 Temel Özellikler

- ✅ Gerçek zamanlı yüz algılama (OpenCV)
- ✅ Embedding tabanlı yüz tanıma (DeepFace)
- ✅ PostgreSQL veritabanı entegrasyonu
- ✅ Masaüstü uygulaması (PyQt5)
- ✅ Yetkili kullanıcı kayıt sistemi
- ✅ Yetkisiz giriş log kaydı
- ✅ Bildirim sistemi (Alarm sesi olmadan popup bildirim)

---

## 🧠 Sistem Mimarisi

Sistem modüler bir yapı ile tasarlanmıştır:


Kamera
↓
Yüz Algılama (OpenCV)
↓
Yüz Tanıma (DeepFace)
↓
PostgreSQL
↓
Masaüstü Bildirim (PyQt5)


---

## 🏗️ Modüler Yapı

### 1️⃣ Kamera Modülü
- Kameradan gerçek zamanlı görüntü alır
- Yüz tespiti yapar
- Yüz görüntüsünü tanıma modülüne iletir

### 2️⃣ Yüz Tanıma Modülü
- Embedding üretir
- Veritabanındaki kayıtlarla karşılaştırma yapar
- Sonuç üretir (Yetkili / Yetkisiz)

### 3️⃣ Veritabanı Modülü
- Yetkili kullanıcı kayıtlarını tutar
- Giriş-çıkış loglarını saklar
- Yetkisiz giriş fotoğraflarını kaydeder

### 4️⃣ Masaüstü Arayüz
- Kamera görüntüsünü gösterir
- Tanınan kişiyi ekranda gösterir
- Bildirim oluşturur
- Yetkili ekleme ekranı sağlar

---

## 🗄️ Veritabanı Tasarımı

### Yetkililer Tablosu
| id | ad | soyad | embedding |

### Giriş Kayıtları Tablosu
| id | isim | tarih | saat | durum |

### Yetkisiz Kayıt Tablosu
| id | foto_yolu | tarih | saat |

---

## 🛠️ Kullanılan Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| Programlama Dili | Python |
| Görüntü İşleme | OpenCV |
| Yüz Tanıma | DeepFace |
| Veritabanı | PostgreSQL |
| Masaüstü Arayüz | PyQt5 |
| Bildirim Sistemi | Plyer |

---

## 📂 Proje Klasör Yapısı


security-system/

├── ai/
│ ├── camera_module.py
│ ├── recognition_module.py
│
├── database/
│ ├── db.py
│ ├── schema.sql
│
├── ui/
│ ├── main_window.py
│
├── images/
│
├── main.py
└── README.md


---

## 🔧 Kurulum

### 1️⃣ Depoyu Klonlayın

```bash
git clone https://github.com/kullaniciadi/ai-yetkili-giris-sistemi.git
2️⃣ Gerekli Kütüphaneleri Yükleyin
pip install opencv-python
pip install deepface
pip install pyqt5
pip install psycopg2
pip install plyer
👥 Ekip
İsim	Rol
Emircan Alkan	Kamera ve Yüz Algılama
Embiya Talas	Yüz Tanıma ve Embedding
Şükran Yılmaz	PostgreSQL ve Kayıt Sistemi
Kaan Baydere	Masaüstü Arayüz ve Bildirim
📌 Proje Durumu

🔄 Aktif geliştirme aşamasındadır.
Bu proje akademik amaçlı olarak geliştirilmiştir.

✨ Akademik Katkı

Bu sistem:

Gerçek zamanlı AI uygulamasıdır

Embedding tabanlı biyometrik doğrulama kullanır

Modüler yazılım mimarisi içerir

Güvenlik sistemleri için uygulanabilir bir prototiptir
