import requests
import pyautogui
import time
import random

# Konfigurasi
nomor_wa = "628xxxxxxxx"  # Isi dengan nomor WA target
otp = "123456"  # Isi dengan OTP yang ingin disebarkan

# Fungsi untuk mengirimkan OTP
def kirim_otp():
    link = f"https://wa.me/{nomor_wa}?text={otp}"
    requests.get(link)

# Fungsi untuk mengirimkan spam OTP
def spam_otp():
    for i in range(1000):  # Isi dengan jumlah spam yang ingin dikirim
        kirim_otp()
        time.sleep(1)  # Tunggu 1 detik sebelum mengirimkan spam berikutnya

# Eksekusi spam OTP
spam_otp()
```
