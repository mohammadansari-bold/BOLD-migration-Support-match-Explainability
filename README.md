# Bold Migration Support Match Explainability

A FastAPI service that generates support match explainability using OpenAI. It evaluates how a user profile aligns with a job description and returns structured explainability details.

## Features

- FastAPI application with a mounted explainability endpoint
- OpenAI chat-based text generation using a structured prompt
- `MatchExplainabilityResponse` output with explainability, skill alignment, work history relevance, gaps, and rectifier guidance
- Simple logging and environment-based OpenAI API configuration

## Requirements

- Python 3.12+
- OpenAI API key
- Dependencies from `pyproject.toml`

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

> If `requirements.txt` is not available, install from `pyproject.toml`:
>
> ```bash
> python -m pip install -e .
> ```

2. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

## Run the application

Start the API server with:

```bash
python app.py
```

Or using Uvicorn directly:

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

The main API will be available at:

- `GET /app` — health check
- `POST /api/v1/jobs/match-explainability` — generate explainability

Swagger UI is available at `http://127.0.0.1:8000/docs`.

## API Usage

### POST /api/v1/jobs/match-explainability

Send a JSON payload with `Job_ID` and `Profile_attributes`.

Example request body:

```json
{
  "Job_ID": "job-123",
  "Profile_attributes": {
    "job_title": "Software Engineer",
    "skills": ["Python", "FastAPI", "REST APIs"],
    "work_history": [
      {
        "company": "Example Corp",
        "role": "Backend Developer",
        "duration": "2 years",
        "highlights": "Built RESTful APIs and automated deployments"
      }
    ],
    "job_id": "job-123"
  }
}
```

### Response schema

The endpoint returns a JSON object matching `MatchExplainabilityResponse`:

- `explainability`: explanation of how the profile fits the job
- `skills`: matched skills between profile and job description
- `wh_relevance`: relevance of work history to the job
- `gaps`: missing skills or experience gaps
- `rectifier`: suggested next step or missing details to add

## Project structure

- `app.py` — root FastAPI app and endpoint mounting
- `match_explainability/main.py` — explainability endpoint implementation
- `match_explainability/explainability.py` — OpenAI prompt and explainability generation logic
- `match_explainability/prompts.py` — system prompt template for match explainability
- `match_explainability/request_response_format.py` — Pydantic request/response models
- `utilities/ai_generator.py` — OpenAI integration helpers and generator classes
- `config.py` — environment loading for `OPENAI_API_KEY`
- `constants.py` — OpenAI model and default settings
- `logger.py` — logging configuration

## Notes

- The current implementation uses a placeholder job description: `Implement job description fetching logic`.
- To make the service production-ready, add real job description retrieval based on `Job_ID`.
- Ensure your OpenAI key is valid and has access to the configured model.

## Development

- Update prompt templates in `match_explainability/prompts.py` to refine reasoning and JSON output.
- Adjust model parameters in `utilities/ai_generator.py` and `match_explainability/explainability.py`.
- Add tests around request validation and response parsing.
