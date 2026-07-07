# BOLD Migration Support Match Explainability

A FastAPI service that generates support match explainability using OpenAI. It evaluates how a user profile aligns with a job description and returns structured explainability details.

## Features

- FastAPI application with a mounted explainability endpoint
- OpenAI chat-based text generation using a structured prompt
- `MatchExplainabilityResponse` output with explainability, skill alignment, work history relevance, gaps, and rectifier guidance
- Logging and environment-based OpenAI API configuration

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12+ | Programming Language |
| FastAPI | REST API Framework |
| OpenAI API | Explainability Generation |
| Pydantic | Request & Response Validation |
| uv | Dependency Management |

---

## Project Structure

```
.
├── app.py
├── config.py
├── constants.py
├── logger.py
├── match_explainability
│   ├── explainability.py
│   ├── main.py
│   ├── prompts.py
│   └── request_response_format.py
└── utilities
    └── ai_generator.py
```

### Description

| File | Purpose |
|------|---------|
| `app.py` | FastAPI application and route registration |
| `config.py` | Environment configuration |
| `constants.py` | Default model configuration |
| `logger.py` | Logging configuration |
| `match_explainability/main.py` | API endpoint implementation |
| `match_explainability/explainability.py` | Explainability generation logic |
| `match_explainability/prompts.py` | Prompt templates |
| `match_explainability/request_response_format.py` | Request and response models |
| `utilities/ai_generator.py` | OpenAI helper utilities |

---

# Prerequisites

- Python 3.12+
- OpenAI API Key
- uv package manager

Install uv if required:

```bash
pip install uv
```

---

# Installation

Clone the repository:

```bash

git clone https://github.com/mohammadansari-bold/BOLD-migration-Support-match-Explainability.git
cd BOLD-migration-Support-match-Explainability

```

Create a virtual environment:

### Windows

```bash
uv venv
.\.venv\Scripts\activate
```

### Linux / macOS

```bash
uv venv
source .venv/bin/activate
```

Install dependencies:

```bash
uv sync
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
```

| Variable | Required | Description |
|----------|----------|-------------|
| OPENAI_API_KEY | Yes | OpenAI API Key used for generating explainability |

---

# Running the Application

Run the application:

```bash
uv run app.py
```

or

```bash
uv run uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoint

## Generate Match Explainability

**POST**

```
/api/v1/jobs/match-explainability
```

### Request Body

```json
{
  "Job_ID": "job-123",
  "Profile_attributes": {
    "job_title": "Software Engineer",
    "skills": [
      "Python",
      "FastAPI",
      "REST APIs"
    ],
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

## Sample Response

```json
{
  "explainability": "The job description is very brief, mentioning backend/API work and data retrieval. Your background in RESTful API development aligns well with implementing server-side logic to fetch and serve job description data.",
  "skills": "This job aligns with your profile because you possess the following skills that are mentioned in the job description: REST APIs, Python.",
  "wh_relevance": "Your work as a Backend Developer focused on building RESTful APIs and maintaining microservices, which is transferable to implementing backend logic.",
  "gaps": "The job description doesn't mention specific requirements, but potential gaps include database/query skills, integration with external APIs, caching, and API specifications.",
  "rectifier": "You could improve your profile by highlighting backend fetching and integration work, API documentation, and database experience."
}
```

---

# Response Fields

| Field | Description |
|-------|-------------|
| explainability | Overall reasoning behind the candidate-job match |
| skills | Skills aligned with the job description |
| wh_relevance | Relevance of previous work history |
| gaps | Missing skills or experience |
| rectifier | Suggested improvements for the profile |

---

# HTTP Status Codes

| Status Code | Description |
|------------|-------------|
| 200 | Explainability generated successfully |
| 400 | Invalid request payload |
| 422 | Validation error |
| 500 | Internal server error |

---

## Notes

- The current implementation uses a placeholder job description: `Implement job description fetching logic`.
- To make the service production-ready, add real job description retrieval based on `Job_ID`.
- Ensure your OpenAI key is valid and has access to the configured model.

## Development

- Update prompt templates in `match_explainability/prompts.py` to refine reasoning and JSON output.
- Adjust model parameters in `utilities/ai_generator.py` and `match_explainability/explainability.py`.
- Add tests around request validation and response parsing.
