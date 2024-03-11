from PIL import Image
import os

# Define directory containing folders
data_dir = "C:/Users/ADMIN/Downloads/archive/CT"

# Define folder names (modify if needed)
normal_dir = "normal"
cancer_dir = "cancer"

output_dir = "G:\Learn\lung_cancer_analysis\data"  # Modify as needed

target_resolution = (224, 224)

# Create output folders if they don't exist
os.makedirs(os.path.join(output_dir, normal_dir), exist_ok=True)
os.makedirs(os.path.join(output_dir, cancer_dir), exist_ok=True)

# Loop through each folder (normal and cancer)
for folder in [normal_dir, cancer_dir]:
    # Create full path for the folder
    folder_path = os.path.join(data_dir, folder)
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check for PNG or JPG extensions
        if filename.endswith(".png") or filename.endswith(".jpg"):
            img = Image.open(os.path.join(folder_path, filename))
            img = img.resize(target_resolution)
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            new_filepath = os.path.join(output_dir, folder, new_filename)
            img.save(new_filepath)
            print(f"Converted {folder}/{filename} to {new_filepath}")
