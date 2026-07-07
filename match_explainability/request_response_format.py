from pydantic import BaseModel, Field

class ProfileAttributes(BaseModel):
    job_title: str = Field(..., description="The job title of the individual.")
    skills: list[str] = Field(..., description="A list of skills possessed by the individual.")
    work_history: list[dict] = Field(..., description="A list of work history entries, each containing details about previous employment.")
    job_id: str = Field(..., description="The unique identifier for the job associated with the profile.")

class MatchExplainabilityResponse(BaseModel):
    explainability: str = Field(..., description="A detailed explanation of the match between the profile and the job requirements.")
    skills: str = Field(..., description="An explanation of how well the individual's skills match the job requirements.")
    wh_relevance: str = Field(..., description="An explanation indicating the relevance of the individual's work history to the job requirements.")
    gaps: str = Field(..., description="An explanation representing the missing skills or gap between the individual's profile and the job requirements.")
    rectifier: str = Field(..., description="A suggested rectifier or action to improve the match between the profile and the job requirements.")