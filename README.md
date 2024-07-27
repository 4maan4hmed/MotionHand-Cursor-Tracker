
# MotionHand Cursor Tracker

**MotionHand Cursor Tracker** enables hands-free cursor control using hand gestures. By leveraging the MediaPipe library and OpenCV, this Python-based application tracks hand movements through a webcam to control the cursor on your screen.

## Features

- Real-time hand tracking using MediaPipe.
- Cursor movement based on index finger position.
- Click detection using thumb and index finger proximity.
- Adjustable sensitivity for click detection.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- PyAutoGUI (`pyautogui`)

## Installation

1. Clone this repository or download the ZIP file.
2. Install the required Python libraries. You can use the following commands:

    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

## Usage

1. Connect a webcam to your computer.
2. Run the `motion_hand_cursor_tracker.py` script:

    ```bash
    python motion_hand_cursor_tracker.py
    ```

3. Position your hand in front of the webcam:
   - Move your index finger to control the cursor position.
   - Pinch your thumb and index finger together to perform a click.

4. Press `q` to exit the application.

## Code Overview

- **Camera Setup**: Captures video from the webcam using OpenCV.
- **Hand Tracking**: Uses MediaPipe to detect hand landmarks and track movements.
- **Cursor Control**: Maps hand movements to cursor position using PyAutoGUI.
- **Click Detection**: Checks for a pinch gesture to perform a mouse click.


## Troubleshooting

- **Ensure the webcam is connected**: The application requires a functioning webcam to detect hand movements.
- **Adjust lighting conditions**: Make sure the environment is well-lit for accurate hand tracking.
- **Check dependencies**: Verify that all required Python libraries are installed.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or fixes.


---

