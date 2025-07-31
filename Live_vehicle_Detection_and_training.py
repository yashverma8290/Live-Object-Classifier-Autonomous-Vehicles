import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# ==== Configuration ====
IMG_SIZE = 64
CLASSES = ['pedestrian', 'stop_sign', 'car', 'bicycle', 'traffic_light']
data = []
labels = []

def preprocess(frame):
    frame = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    return frame.astype('float32') / 255.0

def draw_ui(frame):
    h, w = frame.shape[:2]
    for i, cls in enumerate(CLASSES):
        cv2.rectangle(frame, (10, 10 + i*40), (200, 40 + i*40), (255, 255, 255), -1)
        cv2.putText(frame, f"Press {i} - {cls}", (15, 35 + i*40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)
    cv2.putText(frame, "Press T to Train | P to Predict | Q to Quit",
                (10, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

def build_model(num_classes):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

model = None
trained = False

# Start webcam
cap = cv2.VideoCapture(0)
print("📸 Starting webcam... Press number keys to label frames.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    draw_ui(frame)
    cv2.imshow("Autonomous Vehicle Object Trainer", frame)

    key = cv2.waitKey(1) & 0xFF

    # Label the frame
    if key in [ord(str(i)) for i in range(len(CLASSES))]:
        class_id = int(chr(key))
        img = preprocess(frame)
        data.append(img)
        labels.append(class_id)
        print(f"✅ Captured frame for: {CLASSES[class_id]}")

    # Train the model
    elif key == ord('t'):
        if len(data) < len(CLASSES) * 3:
            print("⚠️ Not enough samples. Capture more data.")
            continue
        print("🧠 Training model...")
        X = np.array(data)
        y = np.array(labels)
        model = build_model(len(CLASSES))
        model.fit(X, y, epochs=10, batch_size=8)
        trained = True
        print("🎉 Training complete!")

    # Predict
    elif key == ord('p') and trained:
        img = preprocess(frame)
        pred = model.predict(np.expand_dims(img, axis=0))[0]
        class_idx = np.argmax(pred)
        prob = np.max(pred)
        label = f"{CLASSES[class_idx]}: {prob:.2f}"
        cv2.putText(frame, label, (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.imshow("Autonomous Vehicle Object Trainer", frame)
        print(f"🔮 Predicted: {label}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
