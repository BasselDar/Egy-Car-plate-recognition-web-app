from flask import Flask, render_template, request
import easyocr
from ultralytics import YOLO
import cv2
import base64

app = Flask(__name__)

# Initialize EasyOCR reader with Tesseract OCR engine
languages = ['ar']
reader = easyocr.Reader(languages)

# Initialize the YOLO license plate detector
license_plate_detector = YOLO("best.pt")

def process_image(image_path):
    # Load the image
    frame = cv2.imread(image_path)

    # Perform license plate detection
    license_plates = license_plate_detector(frame)[0]

    results = []

    # Process each detected license plate
    for license_plate in license_plates.boxes.xyxy.tolist():
        x1, y1, x2, y2 = map(int, license_plate)

        # Crop the license plate region
        cropped_plate = frame[y1:y2, x1:x2]

        # Resize the cropped image with a different scaling factor
        scale_factor = 10.0  # You can adjust this value
        resized_plate = cv2.resize(cropped_plate, (int(scale_factor * cropped_plate.shape[1]),
                                                   int(scale_factor * cropped_plate.shape[0])))

        # Convert the resized image to grayscale
        gray_resized_plate = cv2.cvtColor(resized_plate, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding to enhance characters
        _, segmented_plate = cv2.threshold(gray_resized_plate, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Perform OCR on the segmented image using EasyOCR
        result = reader.readtext(segmented_plate)

        results.append(result)

    # Convert segmented image to base64
    _, buffer = cv2.imencode('.jpg', segmented_plate)
    img_str = base64.b64encode(buffer).decode('utf-8')

    # Convert cropped image to base64
    _, buffer_cropped = cv2.imencode('.jpg', cropped_plate)
    img_str_cropped = base64.b64encode(buffer_cropped).decode('utf-8')

    # Convert original image to base64
    _, buffer_original = cv2.imencode('.jpg', frame)
    img_str_original = base64.b64encode(buffer_original).decode('utf-8')

    return results, img_str, img_str_cropped, img_str_original

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the image file from the POST request
        image_file = request.files['file']

        # Save the image file to a temporary location
        temp_image_path = "temp_image.jpg"
        image_file.save(temp_image_path)

        # Process the image and get OCR results, full image, cropped image, and original image data
        results, img_str, img_str_cropped, img_str_original = process_image(temp_image_path)

        # Render the result page with the OCR results and image data
        return render_template('result.html', results=results, image=img_str, image_cropped=img_str_cropped, image_original=img_str_original)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)