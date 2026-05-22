import cv2
import pickle
import time
import numpy as np
import os
from deepface import DeepFace

from alert_email import send_email
from alert_sms import send_sms
from tracking import Tracker

# Folder
if not os.path.exists("unknown"):
    os.makedirs("unknown")

# Load encodings
with open("encodings.pkl", "rb") as f:
    known_faces, known_names = pickle.load(f)

cap = cv2.VideoCapture(0)
tracker = Tracker()
last_alert = 0

def find_match(embedding):
    if len(known_faces) == 0:
        return "Unknown", 0
    distances = []

    for known in known_faces:
        dist = np.linalg.norm(np.array(known) - np.array(embedding))
        distances.append(dist)

    min_dist = min(distances)
    index = distances.index(min_dist)

    print("Distance:", min_dist)
    confidence = round((1 - min_dist) * 100, 2)
    if min_dist < 5:
        return known_names[index], confidence
    else:
        return "Unknown", confidence


while True:
    ret, frame = cap.read()
    if not ret:
        break

    rects = []
    names = []
    confidences = []

    try:
        faces = DeepFace.extract_faces(
            frame,
            detector_backend="opencv",
            enforce_detection=False
        )

        for face in faces:
            area = face['facial_area']
            x, y, w, h = area['x'], area['y'], area['w'], area['h']

            rects.append((x, y, w, h))

            padding = 30

            x1 = max(0, x - padding)
            y1 = max(0, y - padding)
            x2 = min(frame.shape[1], x + w + padding)
            y2 = min(frame.shape[0], y + h + padding)

            face_crop = frame[y1:y2, x1:x2]
            embedding = DeepFace.represent(
                img_path=face_crop,
                model_name="Facenet512",
                enforce_detection=False
            )[0]["embedding"]

            name, confidence = find_match(embedding)

            names.append(name)
            confidences.append(confidence)

    except Exception as e:
        print("Error:", e)

    # 🔥 TRACKING
    objects = tracker.update(rects)

    for ((objectID, centroid), (x, y, w, h), name, conf) in zip(
        objects.items(), rects, names, confidences
    ):

        color = (0,255,0) if name != "Unknown" else (0,0,255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        label = f"ID {objectID} - {name} ({conf:.1f}%)"
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # 🚨 ALERT
        if name == "Unknown":
            if time.time() - last_alert > 10:
                print(f"🚨 ALERT: Unknown ID {objectID}")

                filename = f"unknown/{int(time.time())}.jpg"
                cv2.imwrite(filename, frame)

                send_email(filename)
                send_sms()

                # Movement log
                with open("movement_log.txt", "a") as f:
                    f.write(f"Unknown ID {objectID} at {time.ctime()}\n")

                last_alert = time.time()

    cv2.imshow("AI Surveillance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()