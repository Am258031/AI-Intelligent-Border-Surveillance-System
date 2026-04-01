from deepface import DeepFace
import os
import pickle

DATASET_PATH = "dataset"
ENCODING_FILE = "encodings.pkl"

known_faces = []
known_names = []

print("🔄 Encoding faces...")

for person in os.listdir(DATASET_PATH):
    person_path = os.path.join(DATASET_PATH, person)

    if not os.path.isdir(person_path):
        continue

    print(f"📁 Processing: {person}")

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        try:
            embedding = DeepFace.represent(
                img_path=img_path,
                model_name="Facenet",
                enforce_detection=False
            )

            if embedding and len(embedding) > 0:
                known_faces.append(embedding[0]["embedding"])
                known_names.append(person)
                print(f"✅ Encoded: {img_name}")
            else:
                print(f"⚠️ No face found: {img_name}")

        except Exception as e:
            print(f"❌ Error in {img_name}: {e}")

# Save encodings
with open(ENCODING_FILE, "wb") as f:
    pickle.dump((known_faces, known_names), f)

print("\n🎉 Encoding complete!")
print(f"Total faces encoded: {len(known_faces)}")