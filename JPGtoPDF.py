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

def convert_images_to_individual_pdfs(input_folder, output_folder, archive_folder):
    images = [file for file in os.listdir(input_folder) if file.lower().endswith('.jpg')]

    if not images:
        print(f"No JPG files found in {input_folder}.")
        return

    for image_name in images:
        image_path = os.path.join(input_folder, image_name)
        pdf_path = os.path.join(archive_folder, os.path.splitext(image_name)[0] + ".pdf")

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

            # Optionally, you can remove the original JPG file if needed
            # os.remove(image_path)
            # print(f"JPG file removed: {image_path}")

        except Exception as e:
            print(f"Error processing {image_name}: {e}")

def main_loop():
    input_folders = ["C:/users/admin/Dropbox/Azja","C:/users/admin/Dropbox/Browar", "C:/users/admin/Dropbox/Cafe","C:/users/admin/Dropbox/CKF13","C:/users/admin/Dropbox/CookClub","C:/users/admin/Dropbox/Corner","C:/users/admin/Dropbox/Destilo","C:/users/admin/Dropbox/Europejska","C:/users/admin/Dropbox/Garden","C:/users/admin/Dropbox/GND","C:/users/admin/Dropbox/Hotelowa","C:/users/admin/Dropbox/Italia","C:/users/admin/Dropbox/Izba","C:/users/admin/Dropbox/Kuznica","C:/users/admin/Dropbox/NewPort","C:/users/admin/Dropbox/Pino","C:/users/admin/Dropbox/Remo","C:/users/admin/Dropbox/River","C:/users/admin/Dropbox/Stek","C:/users/admin/Dropbox/Zapiecek"]
    archive_folders = ["D:/ftp/dropbox/Azja","D:/ftp/dropbox/Browar", "D:/ftp/dropbox/Cafe","D:/ftp/dropbox/CKF13","D:/ftp/dropbox/CookClub","D:/ftp/dropbox/Corner","D:/ftp/dropbox/Destilo","D:/ftp/dropbox/Europejska","D:/ftp/dropbox/Garden","D:/ftp/dropbox/GND","D:/ftp/dropbox/Hotelowa","D:/ftp/dropbox/Italia","D:/ftp/dropbox/Izba","D:/ftp/dropbox/Kuznica","D:/ftp/dropbox/NewPort","D:/ftp/dropbox/Pino","D:/ftp/dropbox/Remo","D:/ftp/dropbox/River","D:/ftp/dropbox/Stek","D:/ftp/dropbox/Zapiecek"]
    
    while True:
        for input_folder, archive_folder in zip(input_folders, archive_folders):
            convert_images_to_individual_pdfs(input_folder, input_folder, archive_folder)
        
        print("Waiting for one hour before the next iteration...")
        time.sleep(1800)  # Delay for one hour (3600 seconds)

if __name__ == "__main__":
    main_loop()
