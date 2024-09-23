# Hindi & English OCR Web Application

This project is a simple web-based Optical Character Recognition (OCR) application built using Streamlit and Tesseract OCR. It allows users to upload images containing both Hindi and English text, extracts the text from the image, and provides a basic keyword search functionality to highlight specific terms within the extracted text.

## Features
- **Supports both Hindi and English text**: The OCR engine can extract text from images in both Hindi and English.
- **File Upload**: Upload JPEG, PNG, or JPG images.
- **Keyword Search**: After extracting the text from the image, users can search for specific keywords in the extracted text (in either Hindi or English).
- **Live Display**: The extracted text is displayed directly on the web page.

## Technologies Used
- **Streamlit**: Used to build the web interface.
- **Tesseract OCR**: The OCR engine used to extract text from images.
- **Python Libraries**:
  - `Pillow`: For image processing.
  - `pytesseract`: Python wrapper for the Tesseract OCR engine.
  - `Streamlit`: For the web application framework.

## Installation

Follow these steps to get the project up and running locally on your machine.

### Prerequisites
- Python 3.x
- Tesseract OCR (with Hindi language support)
  - **Linux**: `sudo apt-get install tesseract-ocr tesseract-ocr-hin`
  - **Windows**: Download and install from [Tesseract's official page](https://github.com/tesseract-ocr/tesseract/wiki)
  - **macOS**: Install via Homebrew `brew install tesseract`

### Running the Application
- Clone the repository or download the code files to your local machine.
- Open a terminal in the project directory.
- Run the Streamlit application:
  ```bash
  stremlit run app.py
  
### Python Libraries
Install the required Python packages by running:

```bash
pip install torch torchvision transformers
pip install streamlit
pip install pytesseract
pip install Pillow
