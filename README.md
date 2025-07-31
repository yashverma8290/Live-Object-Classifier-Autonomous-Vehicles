# 🚗 Live Object Classifier for Autonomous Vehicles using Webcam and CNN

A real-time deep learning project that lets you **label**, **train**, and **predict** object classes like **car**, **pedestrian**, **stop sign**, etc., directly from your webcam.  
Built using **TensorFlow** + **OpenCV**. Perfect for beginners learning computer vision and autonomous vehicle basics.

---

## 🎯 Features

- Live webcam feed with labeling UI  
- Press number keys to label objects  
- Real-time CNN training (no pre-saved dataset)  
- Live object prediction after training  
- Desi-style explanation for easy learning  

---

## 🧠 Object Classes

| Key | Class         |
|-----|---------------|
| 0   | Pedestrian    |
| 1   | Stop Sign     |
| 2   | Car           |
| 3   | Bicycle       |
| 4   | Traffic Light |

---

## 🛠️ Requirements

Python 3.6+  
Install the required packages:

```bash
pip install opencv-python tensorflow numpy
```

---

## 🚀 How to Run

1. Make sure your webcam is connected.
2. Run the script:

```bash
python your_script_name.py
```

> Replace `your_script_name.py` with the filename of your Python script.

---

## 🎮 Controls (Hotkeys)

| Key        | Action                                      |
|------------|---------------------------------------------|
| 0–4        | Label current frame with selected class     |
| T          | Train model with captured frames            |
| P          | Predict class of current webcam frame       |
| Q          | Quit the application                        |

> ⚠️ **Important:** Add at least **3–5 images per class** before training, otherwise the model won’t learn well.

---

## 🧑‍💻 Code Summary (Desi Style)

- `preprocess()` – Resizes the webcam frame to 64x64 and normalizes pixels to range [0, 1].
- `draw_ui()` – Draws class names and shortcut keys directly on the webcam screen.
- `build_model()` – Builds a simple CNN using Conv2D, MaxPooling, Dense, and softmax.
- Press number keys `0-4` to label the live frame in real-time.
- Press `T` to train the CNN on captured data.
- Press `P` to predict the class of the current frame using the trained model.

---

## 📊 Sample Output

```text
🔮 Predicted: car: 0.91
```

The predicted label is also shown in red on the live webcam feed.

---

## 📁 Optional Dataset Folder Structure

You can modify the project to save and load images using this folder format:

```
dataset/
├── pedestrian/
├── car/
├── stop_sign/
├── bicycle/
└── traffic_light/
```

---

## 💡 Future Extensions

- Save labeled data automatically to disk
- Save/load trained model (`.h5`)
- Use MobileNetV2 or ResNet for better accuracy
- Add prediction confidence threshold
- Upgrade to object detection using YOLOv8



## 🤝 Contributions

Pull requests are welcome!  
You can contribute:
- Better UI
- More object classes
- Model export functionality
- YOLO-style object detection

---

## 📜 License

MIT License

---

## 👨‍💻 By Yash Verma

