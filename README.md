# 🛡️ AI-Based Intelligent Border Surveillance System

> An AI-powered surveillance system that performs **real-time face recognition**, detects **known and unknown persons**, sends **Email & SMS alerts**, tracks intruders, and maintains movement logs to improve border security.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![DeepFace](https://img.shields.io/badge/DeepFace-Face%20Recognition-red)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📌 Overview

Border security requires continuous monitoring and rapid threat detection. Manual surveillance systems are time-consuming and prone to human error.

This project uses **Artificial Intelligence and Computer Vision** to automate surveillance by recognizing faces, detecting unauthorized individuals, sending instant alerts, and tracking movement in real time.

---

# 🚀 Features

✅ Real-time Face Detection

✅ Face Recognition using FaceNet512

✅ Known & Unknown Person Identification

✅ Automatic Email Alert with Intruder Image

✅ SMS Alert using Twilio

✅ Object Tracking

✅ Movement Logging

✅ Intruder Image Storage

---

# 🏗️ System Architecture

```
                Live Camera
                     │
                     ▼
            Face Detection
                     │
                     ▼
          Face Recognition
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
     Known Person         Unknown Person
          │                     │
          ▼                     ▼
   Display Identity      Capture Image
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
              Send Email Alert       Send SMS Alert
                    │
                    ▼
              Save Movement Log
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| OpenCV | Face Detection |
| DeepFace | Face Recognition |
| FaceNet512 | Face Embedding Generation |
| NumPy | Distance Calculation |
| SMTP | Email Notifications |
| Twilio API | SMS Notifications |
| Pickle | Store Face Encodings |

---

# 📂 Project Structure

```
AI-Surveillance-System/
│
├── dataset/
│   └── amjad/
│       ├── image1.jpg
│       ├── image2.jpg
│
├── unknown/
│
├── alert_email.py
├── alert_sms.py
├── encode_faces.py
├── tracking.py
├── main.py
├── movement_log.txt
├── encodings.pkl
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YourUsername/AI-Surveillance-System.git

cd AI-Surveillance-System
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
TWILIO_SID=xxxxxxxxxxxxxxxx

TWILIO_TOKEN=xxxxxxxxxxxxxxxx

TWILIO_NUMBER=+1xxxxxxxx

TARGET_NUMBER=+91xxxxxxxx

EMAIL_SENDER=your_email@gmail.com

EMAIL_PASSWORD=your_app_password
```

---

# 📸 Dataset

Dataset Structure

```
dataset/

└── amjad/

    ├── image1.jpg

    ├── image2.jpg
```

Use multiple clear face images for better recognition accuracy.

---

# ▶️ Usage

## Step 1

Generate Face Encodings

```bash
python encode_faces.py
```

---

## Step 2

Run Surveillance System

```bash
python main.py
```

---

# 📧 Alert System

Whenever an unknown person is detected:

- Intruder image is captured
- Email notification is sent
- SMS alert is sent
- Movement log is updated

---

# 📊 Output

The application displays

- Face Bounding Box
- Person Name
- Confidence Score
- Tracking ID

Example

```
ID 0 - Amjad (96%)

ID 1 - Unknown
```

---

# 📁 Movement Log

```
Unknown ID 0

Time : Wed Jul 09 11:24:56

Image Saved : unknown/172043221.jpg
```

---

# 🎯 Future Improvements

- Weapon Detection (YOLOv8)

- Drone Surveillance

- Satellite Tracking

- Multi-Camera Support

- Live Dashboard

- Cloud Database

- Face Mask Detection

- Night Vision Integration

---

# 📷 Screenshots

### Face Detection

(Add Screenshot)

---

### Unknown Person Detection

(Add Screenshot)

---

### Email Alert

(Add Screenshot)

---

### SMS Alert

(Add Screenshot)

---

# 💡 Learning Outcomes

This project helped in understanding

- Computer Vision

- Face Recognition

- Deep Learning Models

- OpenCV

- Real-time Video Processing

- API Integration

- Email Automation

- SMS Automation

- Object Tracking

---

# 👨‍💻 Author

**Amjad Ali**

B.Tech Information Technology

LinkedIn: https://linkedin.com/in/yourprofile

GitHub: https://github.com/yourusername

---

# ⭐ If you found this project useful

Please give this repository a ⭐ on GitHub.
