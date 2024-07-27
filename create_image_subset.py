import os
import shutil
import random

def create_image_subset(source_dir, dest_dir, subset_size):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Get all image files from the source directory
    image_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    
    # Check if the subset size is larger than the available images
    if subset_size > len(image_files):
        print("Subset size is larger than the number of available images. Adjusting subset size.")
        subset_size = len(image_files)
    
    # Randomly select a subset of images
    selected_images = random.sample(image_files, subset_size)
    
    # Move the selected images to the destination directory
    for image in selected_images:
        src_path = os.path.join(source_dir, image)
        dest_path = os.path.join(dest_dir, image)
        shutil.move(src_path, dest_path)
    
    print(f"Moved {subset_size} images to {dest_dir}")

# Example usage
source_directory = 'path_to_source_directory'
destination_directory = 'path_to_destination_directory'
subset_size = 100  # Number of images to move

create_image_subset(source_directory, destination_directory, subset_size)
