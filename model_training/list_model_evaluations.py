import os

from google.cloud import automl
from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv("PROJECT_ID")
model_id = os.getenv("MODEL_ID")

client = automl.AutoMlClient()

# Get the full path of the model.
model_full_id = client.model_path(project_id, "us-central1", model_id)

print("List of model evaluations:")

for evaluation in client.list_model_evaluations(parent=model_full_id, filter=""):
    
    print("Model evaluation name: {}".format(evaluation.name))
    print("Model annotation spec id: {}".format(evaluation.annotation_spec_id))
    print("Create Time: {}".format(evaluation.create_time))
    print("Evaluation example count: {}".format(evaluation.evaluated_example_count))
    print("Classification model evaluation metrics: {}".format(evaluation.classification_evaluation_metrics))