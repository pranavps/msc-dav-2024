import kagglehub

# Download latest version
path = kagglehub.dataset_download("toramky/automobile-dataset")

print("Path to dataset files:", path)