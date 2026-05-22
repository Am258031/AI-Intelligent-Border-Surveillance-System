import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

sid = os.getenv("TWILIO_SID")
token = os.getenv("TWILIO_TOKEN")
from_no = os.getenv("TWILIO_NUMBER")
to_no = os.getenv("TARGET_NUMBER")

# ✅ Debug check
if not all([sid, token, from_no, to_no]):
    raise ValueError("❌ Missing environment variables. Check .env file!")

client = Client(sid, token)

def send_sms():
    message = client.messages.create(
        body="🚨 ALERT: Unknown person detected!",
        from_=from_no,
        to=to_no
    )
    print("📱 SMS sent:", message.sid)