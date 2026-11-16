from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
config = types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=200,
    )
API_KEY = os.environ.get("GOOGLE_API_KEY")   
client = genai.Client(api_key=API_KEY)

def llm_model(model="gemini-2.5-flash",config =config):
   
    client = genai.Client()
    client.models.generate_content(model=model, config=config)


def llm_model_generate_embedding(
    model="gemini-embedding-001",
    contents="No Data",
    task_type="RETRIEVAL_DOCUMENT",
):
    response = client.models.embed_content(
        model=model,
        contents=contents,
        config=types.EmbedContentConfig(
            task_type=task_type,
            output_dimensionality=768,
        ),
    )
    if not response.embeddings or not response.embeddings[0].values:
        raise ValueError("The embedding API returned no embedding values")
    return response.embeddings[0].values

