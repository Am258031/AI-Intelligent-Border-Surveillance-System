import cv2
import pickle
import time
import numpy as np
import os
from deepface import DeepFace

# ✅ ALERT MODULES
from alert_email import send_email
from alert_sms import send_sms

# Create folder for unknown faces
if not os.path.exists("unknown"):
    os.makedirs("unknown")

# Load encodings
with open("encodings.pkl", "rb") as f:
    known_faces, known_names = pickle.load(f)

cap = cv2.VideoCapture(0)
last_alert = 0

# 🔥 MATCH FUNCTION (with confidence)
def find_match(embedding):
    distances = []

    for known in known_faces:
        dist = np.linalg.norm(np.array(known) - np.array(embedding))
        distances.append(dist)

    min_dist = min(distances)
    index = distances.index(min_dist)

    # Confidence calculation
    confidence = max(0, 100 - min_dist * 15)

    print("Distance:", min_dist)  # debug

    if min_dist < 6:   # ✅ FIXED THRESHOLD
        return known_names[index], confidence
    else:
        return "Unknown", confidence


while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # ✅ Better detection backend
        faces = DeepFace.extract_faces(
            frame,
            detector_backend="opencv",
            enforce_detection=False
        )

        for face in faces:
            area = face['facial_area']

            x = area['x']
            y = area['y']
            w = area['w']
            h = area['h']

            # Get embedding
            embedding = DeepFace.represent(
                img_path=face["face"],
                model_name="Facenet",
                enforce_detection=False
            )[0]["embedding"]

            name, confidence = find_match(embedding)

            # Label text
            label = f"{name} ({confidence:.1f}%)"

            # Draw box + name
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            # 🚨 ALERT SYSTEM
            if name == "Unknown":
                if time.time() - last_alert > 10:
                    print("🚨 ALERT: Unknown person detected!")

                    filename = f"unknown/{int(time.time())}.jpg"
                    cv2.imwrite(filename, frame)

                    print(f"📸 Saved: {filename}")

                    # 📧 Email Alert
                    send_email(filename)

                    # 📱 SMS Alert
                    send_sms()

                    last_alert = time.time()

    except Exception as e:
        print("Error:", e)

    cv2.imshow("AI Surveillance System", frame)

    # Press 'q' or ESC to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()