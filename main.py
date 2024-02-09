import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    folder_name = os.path.basename(folder_path)
    date_today = datetime.now().strftime("%Y_%m_%d")
    compressed_filename = f"{folder_name}_{date_today}.{compress_type}"

    try:
        if compress_type == "zip":
            with zipfile.ZipFile(compressed_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

        elif compress_type == "tar":
            with tarfile.open(compressed_filename, "w") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))

        elif compress_type == "tgz":
            with tarfile.open(compressed_filename, "w:gz") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))

        print(f"Compression successful. Compressed file saved as {compressed_filename}")
    except Exception as e:
        print(f"Compression failed: {e}")

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    compress_types = ["zip", "tar", "tgz"]
    print("Available compressed file types:")
    for i, c_type in enumerate(compress_types, start=1):
        print(f"{i}. {c_type}")

    choice = int(input("Enter the number corresponding to the desired compressed file type: "))
    if 1 <= choice <= len(compress_types):
        compress_type = compress_types[choice - 1]
        compress_folder(folder_path, compress_type)
    else:
        print("Invalid choice. Please select a number corresponding to the desired compressed file type.")

if __name__ == "__main__":
    main()
