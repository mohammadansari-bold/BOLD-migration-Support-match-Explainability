import json

from match_explainability.prompts import (
    MATCH_EXPLAINABILTY_SYSTEM_PROMPT,
    MATCH_EXPLAINABILTY_USER_PROMPT
)

from logger import loggerME as logger
from constants import GPT_Model
from utilities.ai_generator import OpenAITextGenerator, OpenAI_Text_Config

from match_explainability.request_response_format import MatchExplainabilityResponse


class MatchExplainability:
    def __init__(self):
        self.model = GPT_Model.GPT_5_4_NANO.value
        self.ai_generator = OpenAITextGenerator(
            config=OpenAI_Text_Config(
                model=self.model,
                temperature=0.7,
                top_p=0.5,
                frequency_penalty=0,
                presence_penalty=0,
            )
        )

    async def generate_explainability(self, job_id: str, profile_attributes: dict) -> MatchExplainabilityResponse:
        """Generates explainability for the given job_id and profile_attributes."""
        try:
            # Extract user profile attributes
            user_title = profile_attributes.get("job_title", "N/A")
            user_skills = profile_attributes.get("skills", [])
            user_wh = profile_attributes.get("work_history", [])

            # TODO: Fetch the actual Job Description using the job_id.
            job_description = "Implement job description fetching logic"

            logger.info(f"Generating explainability for Job ID: {job_id}")

            system_prompt = MATCH_EXPLAINABILTY_SYSTEM_PROMPT.format(
                user_title=user_title,
                user_skills=user_skills,
                user_wh=user_wh,
                jd=job_description
            )
            user_prompt = MATCH_EXPLAINABILTY_USER_PROMPT

            response = await self.ai_generator.async_generate_response(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                response_format=MatchExplainabilityResponse,
                json_response=True
            )
            logger.info(f"Explainability generated successfully for Job ID: {job_id}")

            return response["response"]

        except Exception as e:
            logger.error(f"Error generating explainability: {str(e)}")
            raise