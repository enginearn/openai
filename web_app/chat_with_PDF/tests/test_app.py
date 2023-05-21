import sys
sys.path.append('../')
import warnings

from app import pdf_to_text, text_to_chunks

def test_pdf_to_text():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    # You need to have a sample PDF file for this test
    with open("tests/sample.pdf", "rb") as f:
        text = pdf_to_text(f)
    assert isinstance(text, str)  # Assert that the function returns a string

def test_text_to_chunks():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    text = "This is a test text. We want to split this into chunks."
    chunks = text_to_chunks(text)
    assert isinstance(chunks, list)  # Assert that the function returns a list
    assert all(isinstance(chunk, str) for chunk in chunks)  # Assert that all elements in the list are strings
