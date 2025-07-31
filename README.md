title: "🚗 Live Object Classifier for Autonomous Vehicles using Webcam and CNN"
description: >
  A real-time deep learning project that lets you label, train, and predict object classes like car, pedestrian,
  stop sign, etc., directly from your webcam. Built using TensorFlow + OpenCV. Perfect for beginners
  learning computer vision and autonomous vehicle basics.

features:
  - Live webcam feed with labeling UI
  - Press number keys to label objects
  - Real-time CNN training (no pre-saved dataset)
  - Live object prediction after training
  - Desi-style explanation for easy learning

object_classes:
  - key: 0
    class: "Pedestrian"
  - key: 1
    class: "Stop Sign"
  - key: 2
    class: "Car"
  - key: 3
    class: "Bicycle"
  - key: 4
    class: "Traffic Light"

requirements:
  python: ">=3.6"
  pip_packages:
    - opencv-python
    - tensorflow
    - numpy

run_instructions: |
  1. Make sure your webcam works.
  2. Install dependencies:
     ```bash
     pip install opencv-python tensorflow numpy
     ```
  3. Run the script:
     ```bash
     python your_script_name.py
     ```
     Replace `your_script_name.py` with the filename you saved.

controls:
  - key: "0–4"
    action: "Label current frame with respective object class"
  - key: "T"
    action: "Train the model using collected frames"
  - key: "P"
    action: "Predict object class for current webcam frame"
  - key: "Q"
    action: "Quit the program"

note: "👉 Add at least 3–5 images for **each** class before training (press 'T') or prediction will be poor."

code_overview:
  preprocess: "Resize the webcam frame to 64x64 and normalize pixel values to [0, 1]."
  draw_ui: "Draws UI overlay on the webcam feed to show class labels and hotkeys."
  build_model: "Creates a simple CNN with Conv2D, MaxPooling, Flatten, Dense, and softmax."
  labeling: "Press number keys (0-4) to collect and label training data on the fly."
  training: "Press 'T' to train the model once enough data is captured."
  prediction: "Press 'P' to run real-time prediction using trained model."

example_prediction: |
  🔮 Predicted: car: 0.91
  (Also shown in red text on the webcam feed)

optional_folder_structure: |
  📁 dataset/
      ├── pedestrian/
      ├── car/
      ├── stop_sign/
      ├── bicycle/
      └── traffic_light/

future_extensions:
  - Save labeled data automatically in folders
  - Save and load trained model (.h5)
  - Replace CNN with transfer learning model (e.g., MobileNetV2)
  - Add real-time confidence threshold tuning
  - Move to bounding-box based object detection (YOLOv8)

screenshot_note: "📸 You can add a screenshot here showing webcam feed with predictions"

contributing: "Pull requests are welcome. If you’ve got better UI, model ideas, or detection features, feel free to fork and PR!"

license: "MIT License"

author: "👨‍💻 Made with ❤️ by [YourName]"
