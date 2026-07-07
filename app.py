import uvicorn
from fastapi import FastAPI

from match_explainability.main import app as match_explainability_app

app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app!"}


app.mount("/api/v1/jobs/match-explainability", match_explainability_app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)