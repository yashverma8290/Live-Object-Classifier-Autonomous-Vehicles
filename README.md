🚗 Live Object Classifier for Autonomous Vehicles using Webcam and CNN

A real-time deep learning project that lets you label, train, and predict object classes like car, pedestrian,
stop sign, etc., directly from your webcam. Built using TensorFlow + OpenCV. Perfect for beginners
learning computer vision and autonomous vehicle basics.

────────────────────────────
🎯 Features
────────────────────────────
- Live webcam feed with labeling UI
- Press number keys to label objects
- Real-time CNN training (no pre-saved dataset)
- Live object prediction after training
- Desi-style explanation for easy learning

────────────────────────────
🧠 Object Classes
────────────────────────────
Key  |  Class
-----|-------------------
0    |  Pedestrian
1    |  Stop Sign
2    |  Car
3    |  Bicycle
4    |  Traffic Light

────────────────────────────
🛠️ Requirements
────────────────────────────
Python 3.6+
Install these Python packages:

pip install opencv-python tensorflow numpy

────────────────────────────
🚀 How to Run
────────────────────────────
1. Make sure your webcam works.
2. Install the required packages.
3. Run the script:
   python your_script_name.py
   (Replace your_script_name.py with your file name)

────────────────────────────
🎮 Controls (Hotkeys)
────────────────────────────
0–4   → Label current frame with class
T     → Train model with captured data
P     → Predict class of current frame
Q     → Quit the application

⚠️ Add at least 3–5 images for EACH class before pressing T to train.
Else model will be under-trained and prediction will be bad.

────────────────────────────
🧑‍💻 Code Summary (Desi Style)
────────────────────────────
preprocess()  → Resize image to 64x64 and normalize to [0, 1]
draw_ui()     → Draws UI buttons on screen to guide key presses
build_model() → CNN with Conv2D, MaxPooling, Flatten, Dense, softmax
labeling      → Press 0–4 to collect training samples live
training      → Press T to train CNN model on captured data
prediction    → Press P to predict label of live frame

────────────────────────────
📊 Sample Output
────────────────────────────
🔮 Predicted: car: 0.91
(Also shown in webcam feed using red text)

────────────────────────────
📁 Optional Folder Structure
────────────────────────────
dataset/
  ├── pedestrian/
  ├── car/
  ├── stop_sign/
  ├── bicycle/
  └── traffic_light/

You can use this format to save images automatically for future training.

────────────────────────────
💡 Future Ideas
────────────────────────────
- Automatically save captured data to folders
- Export model to .h5 and reload later
- Use MobileNetV2 or ResNet for better accuracy
- Add threshold for confidence score
- Upgrade to object detection (YOLOv8 style)

────────────────────────────
📸 Screenshot (Optional)
────────────────────────────
Add a screenshot showing the webcam feed with predicted label (e.g., "car: 0.91").

────────────────────────────
🤝 Contributions
────────────────────────────
Pull requests are welcome! Add better UI, better models, more classes or YOLO extensions.

────────────────────────────
📜 License
────────────────────────────
MIT License

────────────────────────────
👨‍💻 Author
────────────────────────────
Made with ❤️ by [YourName]
