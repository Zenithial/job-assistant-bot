from pathlib import Path

from src.formatCvSummary import format_llm_response
from src.parseCV import parsePDF
from src.summariseCV import summarise

def test_dic_to_string():
    file_path = Path(__file__).parent / "resources" / "detailedExampleCV.pdf"
    text = parsePDF(file_path)
    response = summarise(text)
    string = format_llm_response(response)
    print(string)