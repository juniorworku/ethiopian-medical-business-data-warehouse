# Object Detection Using YOLO

## Task 3 - Object Detection Using YOLO

This project involves setting up an environment for object detection using YOLO, downloading the YOLO model, preparing the data by collecting images, detecting objects in the images using YOLO, processing the detection results, and storing the detection data in a PostgreSQL database. The project also includes implementing logging to monitor the process.

### Setting Up the Environment

Ensure you have the necessary dependencies installed, including YOLO and its required libraries.

1. Install OpenCV:
   ```sh
   pip install opencv-python

2. Install PyTorch and torchvision (for PyTorch-based YOLO):
    ```sh
    pip install torch torchvision

3. Install OpenCV:
    ```sh
    pip install tensorflow


### Downloading the YOLO Model

1. Clone the YOLOv5 repository::
   ```sh
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5

2. Install the required dependencies::
    ```sh
    pip install -r requirements.txt


### Preparing the Data
1. Collect images from the Chemed Telegram Channel:Ensure you have the images saved in the object_detection/images directory.

### Object Detection with YOLO
1. Use the pre-trained YOLO model to detect objects in the images.

2. Process the detection results: Extract relevant data from the detection results, such as bounding box coordinates, confidence scores, and class labels.

3. Store detection data to a database table: Use PostgreSQL to store the detection data.

### Monitoring and Logging

Implement logging to track the object detection process, capture errors, and monitor progress.

### Running the Object Detection Script

1. Navigate to the object_detection directory:

    ```sh
    cd object_detection

2. Run the object detection script:
    ```sh
    python object_detection.py
    

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
-Ultralytics YOLOv5 for the YOLO implementation.
-Telethon for the Telegram scraping library.