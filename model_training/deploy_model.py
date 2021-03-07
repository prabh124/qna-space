import os

from google.cloud import automl
from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv("PROJECT_ID")
model_id = os.getenv("MODEL_ID")

client = automl.AutoMlClient()

# Get the full path of the model.
model_full_id = client.model_path(project_id, "us-central1", model_id)
response = client.deploy_model(name=model_full_id)

print(f"Model deployment finished. {response.result()}")