from src.parseCV import parsePDF
from pathlib import Path

def testParsePdf():
    file_path = Path(__file__).parent / "resources" / "test.pdf"
    text = parsePDF(file_path)
    assert "This is a test word doc!" in text