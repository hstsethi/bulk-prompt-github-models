import os
import time
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

models_names = ["gpt4-0", "Phi-3.5-mini-instruct", "Mistral-large"]  
def promptModel(models_name, prompt):
    endpoint = "https://models.inference.ai.azure.com"
    model_name = models_name
    token = os.environ["GITHUB_TOKEN"]

    client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)
    response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt)
    ],
    model=model_name,
    temperature=1.0,
    max_tokens=1000,
    top_p=1.0
)

    print(response.choices[0].message.content)

for i in model_names:
    print("Prompting: " + i)
    promptModel(i,"What is your name, model version, architecture, and other technical info")
    time.sleep(5)
