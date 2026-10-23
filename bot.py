
import os
import requests
from datetime import date, datetime
from zoneinfo import ZoneInfo

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

# تاریخ شروع شمارش معکوس
START_DATE = date(2026, 10, 24)

# تاریخ هدف: 29 اسفند 1413
TARGET_DATE = date(2035, 3, 20)

# منطقه زمانی تهران
TEHRAN = ZoneInfo("Asia/Tehran")

# تاریخ امروز در تهران
today = datetime.now(TEHRAN).date()

# بررسی تاریخ شروع
if today < START_DATE:
    print("Countdown has not started yet.")
    raise SystemExit(0)

# محاسبه و ساخت پیام
if today == TARGET_DATE:
    message = "🎯 امروز روز بهترین ورژن خودته!"
elif today > TARGET_DATE:
    message = "🏆 به تاریخ هدف رسیدی!"
else:
    days_left = (TARGET_DATE - today).days
    message = f" {days_left} روز تا رسیدن به همه‌ی خواسته‌هات 💪 "

# ارسال پیام به کانال تلگرام
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
