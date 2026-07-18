import os
from dotenv import load_dotenv

from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

credentials = Credentials(
    url=os.getenv("URL"),
    api_key=os.getenv("WATSONX_APIKEY")
)

model = ModelInference(
    model_id=os.getenv("MODEL_ID"),
    credentials=credentials,
    project_id=os.getenv("PROJECT_ID"),
)

SYSTEM_PROMPT = """
You are InterviewAce AI, an Agentic Interview Preparation Assistant developed using IBM Granite.

Always provide:
- Structured answers
- Markdown headings
- Bullet points
- Professional tone
- Actionable suggestions
"""

def generate_response(user_prompt):
    response = model.generate_text(
        prompt=f"{SYSTEM_PROMPT}\n\n{user_prompt}",
        params={
            "temperature": 0.3,
            "max_new_tokens": 1200,
            "top_p": 0.9
        }
    )
    return response