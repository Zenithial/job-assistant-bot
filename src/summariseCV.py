from typing import List

from google import genai
from dotenv import load_dotenv
import os
from pydantic import BaseModel

class Education(BaseModel):
    degree_subject: str
    grade: str
    institution: str
    dates: str
    relevant_modules: List[str]
    
class WorkExperience(BaseModel):
    job_title: str
    company: str
    dates: str
    responsibilities: str
    
class CvSummary(BaseModel):
     name: str 
     background_info: str 
     key_strengths_and_skills: str 
     education: List[Education]
     work_experience: List[WorkExperience]
     personal_hobbies_and_interests: List[str]

def summarise(cv_as_text):
    prompt = f"""
    You are a recruiter who looks at and reviews CVs. 
    Your task is to analyse a given CV, extract information from it and provide a summary of the CV.
    This summary should include:
    1. Name
    2. Background information
    3. Key strengths and skills
    4. Education
    5. Work experience
    6. Personal hobbies and interests
    You must return a JSON response in the above format. Do not use information not given in the CV.
    Here is the CV: 
    {cv_as_text}
    """
    load_dotenv()
    client = genai.Client(api_key=os.getenv("API_KEY"))
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=(prompt),
        config={
            "response_mime_type": "application/json",
            "response_schema": CvSummary,
        }
    )
    
    return CvSummary.model_validate_json(response.text)
    

