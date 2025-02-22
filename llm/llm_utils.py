from transformers import pipeline
from config.config import Config

# Load OpenAI or Hugging Face model
generator = pipeline("text-generation", model="facebook/opt-350m")

def generate_response(prompt):
    """Generate a response using the LLM."""
    result = generator(prompt, max_length=50, do_sample=True)
    return result[0]['generated_text']
