import os

from google.cloud import automl
from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv("PROJECT_ID")
model_id = os.getenv("MODEL_ID")
content = "How does the len() function work?"

prediction_client = automl.PredictionServiceClient()

# Get the full path of the model.
model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)

text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
payload = automl.ExamplePayload(text_snippet=text_snippet)

response = prediction_client.predict(name=model_full_id, payload=payload)

for annotation_payload in response.payload:
    print(u"Predicted question tag: {}".format(annotation_payload.display_name))
    print(u"Predicted score: {}".format(annotation_payload.classification.score))