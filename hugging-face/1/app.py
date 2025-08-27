import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
huggingface_token = os.environ.get("HF_TOKEN")


client = InferenceClient(
    provider="fireworks-ai",
    api_key=huggingface_token,
)

completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Instruct",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
)

print(completion.choices[0].message)
