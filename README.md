# Web App: License Plate Detection and OCR

This project is a web application built using Flask, EasyOCR, and YOLO for license plate detection and optical character recognition (OCR). The application allows users to upload images, detects license plates in the images, and extracts the text from the detected plates.

## Features

- **License Plate Detection**: Utilizes the YOLO model to detect license plates in the uploaded images.
- **Optical Character Recognition (OCR)**: Uses EasyOCR to read text from the detected license plates.
- **Image Processing**: Processes the image to enhance character recognition.
- **Web Interface**: Provides an intuitive web interface for uploading images and displaying results.

## Requirements

- Python 3.6+
- Flask
- EasyOCR
- Ultralytics YOLO
- OpenCV

## Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/your-repo/license-plate-ocr.git
    cd license-plate-ocr
    ```

2. **Create a Virtual Environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```


3. **Download YOLO Model**:

    Place the `best.pt` YOLO model file in the project directory.

## Usage

1. **Run the Application**:

    ```sh
    python app.py
    ```

2. **Open in Browser**:

    Navigate to `http://127.0.0.1:5000/` in your web browser.

3. **Upload Image**:

    - On the homepage, upload an image containing a license plate.
    - The application will process the image, detect the license plate, and display the OCR results.

## Project Structure

- `app.py`: Main application file.
- `templates/`: HTML templates for the web interface.
  - `index.html`: Homepage template with file upload form.
  - `result.html`: Template to display OCR results and processed images.
- `static/`: Static files (CSS, JS, images).
- `requirements.txt`: List of Python dependencies.

## Functionality

### Flask App

The Flask app is the core of the web application, handling requests and rendering templates.

- **Routes**:
  - `/`: Handles GET and POST requests for the homepage and file uploads.
  
### Image Processing

The `process_image` function processes the uploaded image:

- **License Plate Detection**: Uses the YOLO model to detect license plates.
- **Image Cropping and Scaling**: Crops the detected license plate region and scales it for better OCR.
- **Grayscale Conversion and Thresholding**: Enhances the image for better text recognition.
- **OCR**: Uses EasyOCR to read text from the processed image.

### Result Display

The results, including the original image, cropped license plate image, and OCR result, are converted to base64 and rendered in the `result.html` template.

## Future Improvements

- **Multi-language Support**: Extend OCR capabilities to support more languages.
- **Real-time Detection**: Implement real-time video stream processing.
- **Improved UI**: Enhance the user interface for better user experience.
