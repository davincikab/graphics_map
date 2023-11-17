from zipfile import ZipFile, LargeZipFile

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

def handle_uploaded_icon(f):
    with open("/file/name.png", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)