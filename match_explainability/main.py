"""
This module defines a FastAPI endpoint for processing Support match explainability 
"""

from fastapi import FastAPI, HTTPException

from match_explainability.request_response_format import ProfileAttributes, MatchExplainabilityResponse
from match_explainability.explainability import MatchExplainability
from logger import loggerME as logger

app = FastAPI()

@app.post("/api/v1/jobs/match-explainability")
async def process_match_explainability(
    Job_ID: str,
    Profile_attributes: ProfileAttributes,
    )-> MatchExplainabilityResponse:
    """Processes the match explainability request for a given job ID and profile attributes."""
    try:
        match_explainability = MatchExplainability()
        response = await match_explainability.generate_explainability(
            job_id=Job_ID,
            profile_attributes=Profile_attributes.dict()
        )

        return response
    
    except Exception as e:
        logger.error(f"Error in /api/v1/jobs/match-explainability: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)