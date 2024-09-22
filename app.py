import streamlit as st
import pytesseract
from PIL import Image
import json

# OCR function
def ocr_image(image):
    extracted_text = pytesseract.image_to_string(image, lang="eng+hin")
    return extracted_text

# Web app
def main():
    st.title("OCR for Hindi & English Text")

    # File uploader for the image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform OCR
        extracted_text = ocr_image(image)
        st.write("Extracted Text:")
        st.write(extracted_text)

        # Basic keyword search functionality
        search_term = st.text_input("Enter a keyword to search in the extracted text:")

        if search_term:
            if search_term.lower() in extracted_text.lower():
                st.write(f"Keyword '{search_term}' found in the text!")
                highlighted_text = extracted_text.replace(search_term, f"**{search_term}**")
                st.write(highlighted_text)
            else:
                st.write(f"Keyword '{search_term}' not found in the text.")

if __name__ == "__main__":
    main()
