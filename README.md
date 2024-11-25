# Website Blog dengan Flask, Tailwind CSS, dan Flowbite

Proyek ini adalah sebuah website blog sederhana yang dibangun menggunakan Flask sebagai backend, Tailwind CSS untuk styling, dan Flowbite untuk komponen UI.

## Prasyarat

Sebelum menjalankan proyek ini, pastikan Anda memiliki perangkat lunak berikut terinstal:

- Python 3.x
- Node.js dan npm

## Instalasi

Ikuti langkah-langkah di bawah ini untuk menginstal dan menjalankan proyek ini:

1. **Clone repositori ini**:
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
2. **Buat dan aktifkan virtual environment (opsional tetapi disarankan)**:
  ```bash
  python -m venv venv
  source venv/bin/activate
  venv/Scripts/Activate
3. **Instal Flask**:
  ```bash
  pip install Flask
4. **Instal Tailwind CSS**:
  ```bash
  npm install -D tailwindcss
5. **Instal Flowbite**:
  ```bash
  npm install flowbite
6. **Inisialisasi Tailwind CSS**:
  ```bash
  npx tailwindcss init
7. **Buat file konfigurasi Tailwind: Edit file tailwind.config.js dengan konten berikut:**:
  ```bash
    module.exports = {
    content: [
      "./templates/**/*.html",
      "./static/src/**/*.js",
      "./node_modules/flowbite/**/*.js"
    ],
    theme: {
      extend: {},
    },
    plugins: [
      require('flowbite/plugin')
    ],
  }
