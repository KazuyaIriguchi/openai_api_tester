import os

from openai import AzureOpenAI

# endpoint of westus
azure_endpoint = "https://ai-robot-openai.openai.azure.com"
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_VERSION")
model = "gpt-4-filterless"

client = AzureOpenAI(
    azure_endpoint=azure_endpoint, api_key=api_key, api_version=api_version
)

messages = [{"role": "user", "content": "Perfumeについて3行以内で熱く語って"}]

response = client.chat.completions.create(messages=messages, model=model)

print(f"AOAI response: {response.model_dump_json(indent=4)}")
