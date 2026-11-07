from pathlib import Path

from src.parseCV import parsePDF
from src.summariseCV import summarise

def testLlmSummary():
    file_path = Path(__file__).parent / "resources" / "detailedExampleCV.pdf"
    text = parsePDF(file_path)
    response = summarise(text)
    summary_dict = response.model_dump()
    print(summary_dict)
    assert isinstance(summary_dict, dict)
    assert (summary_dict.get('name') == 'John Smith')
    
def testllmSummaryTwo():
    file_path = Path(__file__).parent / "resources" / "limitedExampleCV.pdf"
    text = parsePDF(file_path)
    response = summarise(text)
    summary_dict = response.model_dump()
    print(summary_dict)
    assert isinstance(summary_dict, dict)
    assert (summary_dict.get('name') == 'Michael Brown')
    
def testllmSummaryThree():
    file_path = Path(__file__).parent / "resources" / "entryLevelCV.pdf"
    text = parsePDF(file_path)
    response = summarise(text)
    summary_dict = response.model_dump()
    print(summary_dict)
    assert isinstance(summary_dict, dict)
    assert (summary_dict.get('name') == 'Emily Wilson')