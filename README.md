# Flask Blog Website

![Alt Text](/static/img/ss.png)

Sebuah proyek website blog yang dibuat menggunakan **Flask** untuk backend, **Tailwind CSS** untuk styling, dan **Material UI Flowbite** untuk komponen UI modern dan responsif.

## 🎯 Fitur

- **Manajemen Blog:**
  - Create dan Read untuk posting blog.
  - Kategori dan tag untuk pengelompokan artikel.
- **Otentikasi:**
  - Registrasi, login, dan logout pengguna.
- **Desain Responsif:**
  - Tampilan yang rapi dan menarik menggunakan Tailwind CSS dan komponen Flowbite.

## 🛠️ Teknologi yang Digunakan

- **Backend:**
  - Python (Flask Framework)
  - Jinja2 (untuk template rendering)
- **Frontend:**
  - Tailwind CSS
  - Material UI Flowbite
- **Database:**
  - MySQL

## ⚙️ Instalasi dan Penggunaan

### 1. Prasyarat

Pastikan Anda memiliki:

- Python 3.8 atau lebih baru
- Node.js & npm (untuk mengelola Tailwind CSS)
- Virtual environment (opsional, tetapi disarankan)

### 2. Clone Repository

```bash
git clone https://github.com/username/flask-blog.git
cd flask-blog
```

### 3. Instal Dependensi Backend

- Buat dan aktifkan virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Untuk Linux/Mac
  venv\Scripts\activate     # Untuk Windows
  ```

- Instal dependensi Python:
  ```bash
  pip install -r requirements.txt
  ```

### 4. Setup Tailwind CSS
- Instal Tailwind CSS dan dependensinya:
  ```bash
  npm install
  ```
- Bangun file Tailwind:
  ```bash
  npx tailwindcss build src/styles.css -o static/css/main.css
  ```

## 📁 Struktur Proyek
flask-blog/
│
├── app/                  # Folder aplikasi utama
│   ├── static/           # File statis (CSS, JS, gambar)
│   ├── templates/        # Template HTML
│   ├── __init__.py       # Inisialisasi aplikasi Flask
│   ├── models.py         # Model database
│   ├── routes.py         # Routing
│   └── forms.py          # Formulir Flask-WTF
│
├── migrations/           # File migrasi database
├── requirements.txt      # Dependensi Python
├── tailwind.config.js    # Konfigurasi Tailwind CSS
├── package.json          # Konfigurasi npm
├── README.md             # File dokumentasi ini
└── Dockerfile            # File untuk Docker

