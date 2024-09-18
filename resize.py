import os
from PIL import Image
import argparse

def resize_image(input_path, output_path, max_width, max_height):
    # Open an image file
    with Image.open(input_path) as img:
        # Get original dimensions
        original_width, original_height = img.size
        
        # Calculate the scaling factor for width and height
        width_ratio = max_width / original_width
        height_ratio = max_height / original_height
        
        # Choose the smaller of the two ratios to maintain aspect ratio
        scaling_factor = min(width_ratio, height_ratio)
        
        # Calculate the new dimensions
        new_width = int(original_width * scaling_factor)
        new_height = int(original_height * scaling_factor)
        
        # Resize the image with the new dimensions and use the LANCZOS filter for high quality
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Save the resized image to the output path
        resized_img.save(output_path)
        print(f"Image resized to {new_width}x{new_height} and saved to {output_path}")

def process_images(input_dir, output_dir, max_width, max_height):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        
        # Check if the file is an image (you can add more formats if needed)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            output_path = os.path.join(output_dir, filename)
            resize_image(input_path, output_path, max_width, max_height)

if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Resize images from input directory to a maximum width and height.')
    parser.add_argument('max_width', type=int, help='Maximum width of the resized images')
    parser.add_argument('max_height', type=int, help='Maximum height of the resized images')
    
    args = parser.parse_args()
    
    # Input and output directories
    input_directory = './images/'
    output_directory = './outputs/'

    # Process the images in the directory
    process_images(input_directory, output_directory, args.max_width, args.max_height)

