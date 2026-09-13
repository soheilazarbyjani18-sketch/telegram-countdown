import os
import requests
from datetime import date

# -----------------------------
# تنظیمات
# -----------------------------

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

# تاریخ هدف: 29 اسفند 1410
# معادل 19 مارس 2032 در تقویم میلادی
TARGET_DATE = date(2032, 3, 19)

# -----------------------------
# محاسبه روزهای باقی‌مانده
# -----------------------------

today = date.today()
days_left = (TARGET_DATE - today).days

if days_left < 0:
    message = "🎯 امروز روز بهترین ورژن خودته!"
else:
   message = f"🚀 {days_left} روز دیگه؛ ادامه بده، نسخه جدیدت نزدیکه!"

# -----------------------------
# ارسال پیام به کانال
# -----------------------------

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHANNEL_ID,
        "text": message
    }
)

response.raise_for_status()

print(message)
