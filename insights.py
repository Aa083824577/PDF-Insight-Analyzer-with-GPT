# insights.py: This file interacts with the OpenAI API to get insights from text.
#  It loads the OpenAI API key and model name from environment variables and defines a system_prompt to guide the LLM in analyzing and interpreting PDF documents.
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

model_name = os.getenv("MODEL")  # fallback if MODEL not in .env

# Define system role instructions
system_prompt = (
    "You are a highly capable assistant designed to analyze and interpret PDF documents. "
    "Your task is to carefully extract key information, identify relevant insights, and "
    "provide clear, accurate, and concise responses based on the document’s content. "
    "Ensure your answers are well-structured, insightful, and tailored to the user's "
    "needs, offering valuable information and actionable summaries."
)

def get_llm_insights(prompt: str) -> str:
    """
    Query the OpenAI API with a given prompt and return insights.
    """
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_completion_tokens=1000 
    )
    return response.choices[0].message.content.strip()

