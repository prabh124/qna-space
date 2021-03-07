from google.cloud import automl

project_id = "qna-space"
dataset_id = "TCN4819247975228243968"
path = "gs://qna-space-lcm/Questions4.csv"

client = automl.AutoMlClient()

# Get the full path of the dataset.
dataset_full_id = client.dataset_path(project_id, "us-central1", dataset_id)

# Get the multiple Google Cloud Storage URIs
input_uris = path.split(",")
gcs_source = automl.GcsSource(input_uris=input_uris)
input_config = automl.InputConfig(gcs_source=gcs_source)

# Import data from the input URI
response = client.import_data(name=dataset_full_id, input_config=input_config)

print("Processing import...")
print("Data imported. {}".format(response.result()))