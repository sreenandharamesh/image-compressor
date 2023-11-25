from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    """
    Compress an image.

    Parameters:
        input_path (str): The path to the input image.
        output_path (str): The path to save the compressed image.
        quality (int): The quality of the compression (0 to 100).

    Returns:
        None
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Save the image with compression
            img.save(output_path, quality=quality)
            print(f"Image compressed successfully and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def compress_all_images(input_folder, output_folder, quality=85):
    """
    Compress all images in a folder.

    Parameters:
        input_folder (str): The path to the folder containing input images.
        output_folder (str): The path to save compressed images.
        quality (int): The quality of the compression (0 to 100).

    Returns:
        None
    """
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Process each file in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                compress_image(input_path, output_path, quality)
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_folder = "input_images"
output_folder = "compressed_images"
compress_all_images(input_folder, output_folder, quality=85)
