import os
from typing import List
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel

class jobSummary(BaseModel):
    company: str
    salary: str
    responsibilities: List[str]
    benefits: List[str]
    required_skills: List[str]
    desirable_skills: List[str]
    experience_needed: str
    

def summariseDescription(job_description_text):
    prompt=f"""
    Your task is to analyse a given job description, extract key information from it and provide a summary of the job description. 
    This summary should include:
    1. Name of the company
    2. Salary of the role if given
    3. Key responsibilities of the role
    4. Company benefits
    5. Required skills for the role
    6. Desired skills for the role
    7. Experience needed for the role
    You must return a JSON response in the above format. Do not use information not given in the job description. Keep each section concise. Key responsibilities should not be more than two sentences.
    Here is the job description: 
    {job_description_text}
    """
    load_dotenv()
    client = genai.Client(api_key=os.getenv("API_KEY"))
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=(prompt),
        config={
            "response_mime_type": "application/json",
            "response_schema": jobSummary,
        }
    )
        
    return jobSummary.model_validate_json(response.text)