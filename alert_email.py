import smtplib
from email.message import EmailMessage

EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "Coder@0000"   # ⚠️ normal password nahi (App Password use karo)
EMAIL_RECEIVER = "receiver_email@gmail.com"

def send_email(image_path):
    msg = EmailMessage()
    msg["Subject"] = "🚨 Alert: Unknown Person Detected"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg.set_content("Unknown person detected. See attached image.")

    # Attach image
    with open(image_path, "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype="image", subtype="jpeg", filename=file_name)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("📧 Email sent!")