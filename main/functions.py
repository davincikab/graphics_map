from zipfile import ZipFile, LargeZipFile
from pathlib import Path
import requests
import glob
import shutil
import os

def handle_uploaded_project_file(f, title):
    try:
        with ZipFile(f, allowZip64=True) as file:
            directory_to_extract = f"media/uploads/projects/{title}"
            file.extractall(path=directory_to_extract)

            return directory_to_extract
    except (LargeZipFile, ValueError) as err:
        print(err)
        return 0

    # z = zipfile.ZipFile(f)
    # z.extractall()
    # with open(f"uploads/projects/{title}.zip", "wb+") as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)

def zip_directory(directory_path, zip_path):
    with ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                zipf.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), 
                                           os.path.join(directory_path, '..')))

def unzip_to_dir(file, destination):
    try:
        with ZipFile(file, allowZip64=True) as file:
            directory_to_extract = f"{destination}"
            file.extractall(path=directory_to_extract)

            return True
    except (LargeZipFile, ValueError) as err:
        print(err)
        return False

def delete_zip(file_url):
    os.remove(file_url)
    return True

def move_accessibility_icons(icons_dir, destination_dir):
    images_jpgs = Path(icons_dir).glob("*.jpg")
    print("Icons Folder")
    image_strings = [str(p) for p in images_jpgs]

    image_pngs = Path(icons_dir).glob("*.png")
    image_strings_png = [str(p) for p in image_pngs]
    for image in image_strings_png:
        shutil.copy2(image, destination_dir)
        
        
def handle_uploaded_icon(f):
    with open("/file/name.png", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)