import json
import os

# GANTI 'bot-keuangan-api-781df83f7a07.json' dengan NAMA FILE JSON kredensial Anda yang sebenarnya.
# Pastikan file JSON ini berada di folder yang sama dengan skrip ini, atau berikan jalur lengkapnya.
json_file_path = 'bot-keuangan-api-781df83f7a07.json'

try:
    # Buka dan baca seluruh konten file JSON
    with open(json_file_path, 'r', encoding='utf-8') as f:
        raw_json_content = f.read()
    
    # Parse string JSON mentah menjadi dictionary Python
    data = json.loads(raw_json_content)

    # Ubah dictionary kembali menjadi string JSON dalam format yang ringkas,
    # secara otomatis meng-escape karakter newline (\n) menjadi \\n
    formatted_json_for_env = json.dumps(data)

    # Cetak string yang siap untuk file .env Anda.
    # String ini dibungkus dengan tanda kutip tunggal ('') seperti yang diharapkan oleh dotenv.
    print(f"GOOGLE_CREDENTIALS_JSON='{formatted_json_for_env}'")

except FileNotFoundError:
    print(f"Error: File JSON tidak ditemukan di '{json_file_path}'. Pastikan nama file dan lokasinya benar.")
except json.JSONDecodeError as e:
    print(f"Error: Gagal memparsing konten JSON. Pastikan file JSON valid dan tidak rusak. Detail: {e}")
except Exception as e:
    print(f"Terjadi kesalahan yang tidak terduga: {e}")

# Catatan: Tidak perlu os._exit(0) saat menjalankan sebagai skrip biasa
