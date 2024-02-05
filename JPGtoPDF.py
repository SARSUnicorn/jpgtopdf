from PIL import Image
import os
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

def convert_images_to_individual_pdfs(input_folder, output_folder, archive_folder, counts):
    images = [file for file in os.listdir(input_folder) if file.lower().endswith('.jpg')]

    if not images:
        print(f"No JPG files found in {input_folder}.")
        return counts

    converted_count, error_count = counts

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
            converted_count += 1

            # Optionally, you can remove the original JPG file if needed
            # os.remove(image_path)
            # print(f"JPG file removed: {image_path}")

        except Exception as e:
            print(f"Error processing {image_name}: {e}")
            error_count += 1

    return converted_count, error_count

def update_log(log_file_path, converted_count, error_count, current_day):
    log_entry = f"{current_day} - converted {converted_count} JPG, had {error_count} JPG conversion error\n"

    with open(log_file_path, 'a') as log_file:
        log_file.write(log_entry)

def main_loop():
    input_folders = ["C:/data/companya", "C:/data/companyb", "C:/data/companyc"]
    archive_folders = ["C:/archive/companya", "C:/archive/companyb", "C:/archive/companyc"]
    
    current_day = None
    counts = {folder: [0, 0] for folder in archive_folders}

    while True:
        for input_folder, archive_folder in zip(input_folders, archive_folders):
            log_file_path = os.path.join(archive_folder, "log.txt")
            counts[archive_folder] = convert_images_to_individual_pdfs(input_folder, input_folder, archive_folder, counts[archive_folder])

        current_time = time.localtime()
        if current_day is None or current_time.tm_mday != current_day:
            current_day = current_time.tm_mday
            
            # Update the log once per day for each company
            for archive_folder in archive_folders:
                update_log(os.path.join(archive_folder, "log.txt"), counts[archive_folder][0], counts[archive_folder][1], f"{current_time.tm_year}-{current_time.tm_mon:02d}-{current_day:02d}")
                
                # Reset counts for each company
                counts[archive_folder] = [0, 0]

        print("Waiting for one hour before the next iteration...")
        time.sleep(3)  # Delay for one hour (3600 seconds)

if __name__ == "__main__":
    main_loop()

if __name__ == "__main__":
    main_loop()
