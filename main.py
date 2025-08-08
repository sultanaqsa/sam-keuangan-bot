import os
import logging
from telegram.ext import Application
from telegram import Update

# --- Konfigurasi Logging ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Fungsi utama untuk mengatur dan menjalankan bot."""

    # Dapatkan token bot dari variabel lingkungan Heroku
    TOKEN = os.getenv("BOT_TOKEN")
    # Dapatkan nama aplikasi Heroku dari variabel lingkungan Heroku
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")

    logger.info(f"DEBUGGING: BOT_TOKEN yang dibaca: {'[TOKEN DITEMUKAN]' if TOKEN else '[TOKEN TIDAK DITEMUKAN]'} (panjang: {len(TOKEN) if TOKEN else 0})")
    if TOKEN:
        # Untuk keamanan, hanya cetak beberapa karakter pertama dan terakhir
        logger.info(f"DEBUGGING: Token awal 5: {TOKEN[:5]}, Token akhir 5: {TOKEN[-5:]}")
    
    logger.info(f"DEBUGGING: HEROKU_APP_NAME yang dibaca: {HEROKU_APP_NAME if HEROKU_APP_NAME else '[TIDAK DITEMUKAN]'}")

    if not TOKEN:
        logger.error("DEBUGGING: Variabel lingkungan 'BOT_TOKEN' tidak ditemukan atau kosong. Bot tidak dapat diinisialisasi.")
        # Kita akan keluar secara paksa karena tanpa token, bot tidak akan berfungsi
        os._exit(1) 
    
    # Coba bangun aplikasi Telegram. Ini akan memicu InvalidToken jika token salah.
    try:
        application = Application.builder().token(TOKEN).build()
        logger.info("DEBUGGING: Inisialisasi aplikasi Telegram BERHASIL (token diterima oleh PTB).")
        # Jika berhasil diinisialisasi, kita tidak perlu menjalankan polling/webhook untuk diagnostik ini
        # Kita hanya ingin memastikan tokennya valid.
        
        # Jika HEROKU_APP_NAME ada, ini berarti kita harusnya di Heroku.
        if HEROKU_APP_NAME:
            logger.info("DEBUGGING: Bot siap untuk mode webhook (setelah inisialisasi token berhasil).")
            # Kita tidak perlu menjalankan webhook di sini, cukup verifikasi inisialisasi.
        else:
            logger.info("DEBUGGING: Bot siap untuk mode polling (setelah inisialisasi token berhasil).")
            # application.run_polling(allowed_updates=Update.ALL_TYPES) # Jangan jalankan polling, hanya verifikasi
        
        logger.info("DEBUGGING: Skrip diagnostik selesai. Periksa log Heroku untuk pesan sukses di atas.")

    except Exception as e:
        logger.error(f"DEBUGGING: Gagal menginisialisasi aplikasi Telegram: {e}", exc_info=True)
        logger.error("DEBUGGING: Bot gagal dimulai. Pastikan BOT_TOKEN Anda 100% benar dan tidak ada spasi/karakter tersembunyi.")
        # Keluar dengan status error agar Heroku menandainya sebagai crashed
        os._exit(1)


if __name__ == "__main__":
    main()
