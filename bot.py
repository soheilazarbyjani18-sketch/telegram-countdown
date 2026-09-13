import os
import requests
from datetime import datetime, date
from zoneinfo import ZoneInfo

# -----------------------------
# تنظیمات
# -----------------------------

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

# 29 اسفند 1410
TARGET_DATE = date(2032, 3, 19)

# ساعت ایران
IRAN_TIMEZONE = ZoneInfo("Asia/Tehran")

# -----------------------------
# محاسبه روزهای باقی‌مانده
# -----------------------------

now = datetime.now(IRAN_TIMEZONE)

# تاریخ فعلی ایران
today = now.date()

# تعداد روزهای باقی‌مانده
days_left = (TARGET_DATE - today).days

# -----------------------------
# متن پیام
# -----------------------------

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
    },
    timeout=30
)

response.raise_for_status()

print(message)
