from pdf2image import convert_from_path
import pytesseract
import pymupdf
from typing import Dict
from collections import defaultdict
import re

BIRD_NAMES = [
    "crow", "sparrow", "eagle", "ostrich", "robin", "parrot", "pigeon",
    "hawk", "falcon", "woodpecker", "dove", "finch", "swan", "pelican",
    "penguin", "flamingo", "owl", "kingfisher", "canary", "hummingbird"
]

def extract_text_and_count_birds(path: str) -> Dict[str, int]:
    """
    Extracts text from a PDF and formats it into a JSON structure.
    
    Args:
        pdf_path (str): The path to the PDF file to be processed.

    Returns:
        Dict[str, int]: A dictionary with page numbers as keys and a list of text blocks for each page.
    """
    bird_count = defaultdict(int)

    try:
        # Attempt to open PDF file
        document = pymupdf.open(path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: Could not open file '{path}'. {e} ")
        return {}
    except Exception as e:
        # Catch-all for any other exceptions
        print(f"An unexpected error occurred while opening the file: {e}")
        return {}

    for page_num in range(document.page_count):
        
        try:
            page = document[page_num]
            page_text = page.get_text("text")

            if not page_text.strip():
                print(f"Page {page_num + 1} might be an image or scanned PDF. No text extracted, using OCR...")

                # Convert the specific PDF page to an image using pdf2image
                images = convert_from_path(path, first_page=page_num + 1, last_page=page_num + 1)

                # Extract text using pytesseract on the first image (should be only one)
                page_text = pytesseract.image_to_string(images[0])

                if not page_text.strip():
                    print(f"No text found even after OCR on Page {page_num + 1}. Skipping this page.")
                    continue

            page_lines = page_text.split("\n")

            for line in page_lines:
                for bird in BIRD_NAMES:
                    bird_count[bird] += len(re.findall(rf"\b{bird}s?\b", line, re.IGNORECASE))

        except Exception as e:
            print(f"Unexpected error on Page {page_num + 1}: {e}")
            continue

    document.close()

    existing_birds = {}
    for bird in bird_count:
        if bird_count[bird] != 0:
            existing_birds[bird] = bird_count[bird]

    return existing_birds
