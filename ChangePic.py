import logging
import os
from PIL import Image, UnidentifiedImageError

logging.basicConfig(filename='conversion.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

try:
    input_folder = r"C:\Users\JefferyLi\Desktop\ChangePICType\path_to_gif_folder" # 确保路径正确
    output_folder = r"C:\Users\JefferyLi\Desktop\ChangePICType\output_jpg_folder" # 确保路径正确

    if not os.path.exists(input_folder):
        print(f"Error: Input folder not found: {input_folder}")
        exit()

    if not os.path.exists(output_folder):
        print(f"Creating output folder: {output_folder}")
        os.makedirs(output_folder)
        if not os.path.exists(output_folder):
            print(f"Error: Failed to create output folder: {output_folder}")
            exit()

    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    print(f"Files in input folder: {os.listdir(input_folder)}") # 打印文件列表

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if not os.path.isfile(file_path):
            print(f"Skipping non-file: {filename}")
            continue

        print(f"Processing file: {filename}")

        if filename.lower().endswith((".gif", ".bmp")):  # 关键修改：同时判断 .gif 和 .bmp
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")
            print(f"Saving to: {output_path}")

            try:
                with Image.open(file_path) as img:
                    img.convert("RGB").save(output_path, "JPEG")
                    print(f"Saved: {output_path}")
            except UnidentifiedImageError:
                print(f"Failed to open or decode image: {file_path}") # 修改错误提示更通用
            except OSError as e:
                print(f"Error saving image: {e}")
            except Exception as e:
                print(f"Unexpected error when saving: {e}")
        else:
            print(f"Skipping non-GIF/BMP file: {filename}") # 修改提示更通用

    print("Conversion completed!")

except FileNotFoundError:
    print(f"Input folder not found: {input_folder}")
except Exception as e:
    print(f"An error occurred: {e}")