# Image Subset Creator

This Python script allows you to create a subset of images from a given directory, create a new folder, and move the selected images to the new folder. This can be particularly useful for tasks such as data preprocessing in machine learning projects, organizing image datasets, and more.

## Features

- Randomly selects a specified number of images from the source directory.
- Ensures the destination directory exists or creates it if it doesn't.
- Moves the selected images to the destination directory.

## Prerequisites

- Python 3.x

## Installing

1. **Clone the repository**:
   ```
   git clone https://github.com/abdulvahapmutlu/create-image-subset.git
   
2. **Navigate to the project directory**:
   ```
   cd create-image-subset

## Usage

1. **Modify the script**:
   - Open `create_image_subset.py` in a text editor.
   - Set the `source_directory` to the path of your source directory containing the images.
   - Set the `destination_directory` to the path where you want to move the subset of images.
   - Set the `subset_size` to the number of images you want to move.

2. **Run the script**:
   ```
   python create_image_subset.py
   ```

### Example

Suppose you have a directory of images located at `/path/to/source/images` and you want to move 100 randomly selected images to a new directory at `/path/to/destination/images`. You would set the following variables in the script:

```
source_directory = '/path/to/source/images'
destination_directory = '/path/to/destination/images'
subset_size = 100
```

After running the script, 100 images will be moved from the source directory to the destination directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
