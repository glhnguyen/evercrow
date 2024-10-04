import unittest
import pymupdf
import os

from backend.evercrow.extract import extract_text_and_count_birds

class TestExtraction(unittest.TestCase):

    def test_text_extraction(self):
        """
        Testing extracting text from PDF file
        """
        pdf_path = os.path.join(os.path.dirname(__file__), 'test.pdf')

        text = extract_text_and_count_birds(pdf_path)
        self.assertIsInstance(text, list)
    
    def test_ocr_on_image_pdf(self):
        """
        Testing OCR extraction on an image-based PDF.
        """
        pdf_image_path = os.path.join(os.path.dirname(__file__), 'test_image.pdf')
        ocr_text = extract_text_and_count_birds(pdf_image_path)

        self.assertIsInstance(ocr_text, list)