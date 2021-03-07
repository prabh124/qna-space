from google.cloud import automl

project_id = "qna-space"
display_name = "Questions4"

client = automl.AutoMlClient()

# A resource that represents Google Cloud Platform location.
project_location = f"projects/{project_id}/locations/us-central1"

# Specify the classification type
# Types:
# MultiLabel: Multiple labels are allowed for one example.
# MultiClass: At most one label is allowed per example.

metadata = automl.TextClassificationDatasetMetadata(
    classification_type=automl.ClassificationType.MULTICLASS
)
dataset = automl.Dataset(
    display_name=display_name,
    text_classification_dataset_metadata=metadata,
)

# Create a dataset with the dataset metadata in the region.
response = client.create_dataset(parent=project_location, dataset=dataset)

created_dataset = response.result()

# Display the dataset information
print("Dataset name: {}".format(created_dataset.name))
print("Dataset id: {}".format(created_dataset.name.split("/")[-1]))