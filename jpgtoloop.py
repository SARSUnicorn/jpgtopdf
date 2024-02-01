from PIL import Image
import os
import shutil
import zipfile
import time

def resize_image(img, max_width, max_height):
    """
    Resize the image proportionally to fit within the specified dimensions.
    """
    original_width, original_height = img.size

    # Calculate the new dimensions while maintaining the aspect ratio
    ratio = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)

    # Resize the image using the default resampling method
    return img.resize((new_width, new_height))

def convert_images_to_individual_pdfs(input_folder, output_folder, archive_path):
    images = [file for file in os.listdir(input_folder) if file.lower().endswith('.jpg')]

    if not images:
        print(f"No JPG files found in {input_folder}.")
        return

    for image_name in images:
        image_path = os.path.join(input_folder, image_name)
        pdf_path = os.path.join(output_folder, os.path.splitext(image_name)[0] + ".pdf")

        try:
            img = Image.open(image_path)

            # Set the maximum width and height for the PDF page
            max_width = 595  # A4 width in points
            max_height = 842  # A4 height in points

            # Resize the image to fit within the PDF page dimensions
            resized_img = resize_image(img, max_width, max_height)

            # Save the resized image as a PDF directly
            resized_img.save(pdf_path, 'PDF', quality=95)

            print(f"PDF created successfully: {pdf_path}")

            # Calculate the relative path inside the zip archive
            relative_path = os.path.join(os.path.basename(archive_path), os.path.basename(input_folder), image_name)
            
            # Add the processed JPG file to the zip archive with maximum compression
            with zipfile.ZipFile(archive_path, 'a', compression=zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(image_path, arcname=relative_path)
            
            print(f"JPG file added to archive: {archive_path}/{os.path.basename(input_folder)}/{image_name}")
            
            # Remove the processed JPG file
            os.remove(image_path)
            print(f"JPG file removed: {image_path}")
        except Exception as e:
            print(f"Error processing {image_name}: {e}")

def main_loop():
    input_folders = ["C:/data/companya", "C:/data/companyb", "C:/data/companyc"]
    archive_path = "C:/data/arch.zip"
    
    while True:
        for input_folder in input_folders:
            output_folder = input_folder  # Save PDFs in the same folder as the input JPGs
            convert_images_to_individual_pdfs(input_folder, output_folder, archive_path)
        
        print("Waiting for one hour before the next iteration...")
        time.sleep(3600)  # Delay for one hour (3600 seconds)

if __name__ == "__main__":
    main_loop()
