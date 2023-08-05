import os, warnings, requests, zipfile, shutil
from zipfile import ZipFile
from io import BytesIO

def acquire_data(url=None, data_dir="data"):
    """
    This function downloads and extracts images into a data folder.
    """
    if url is None:
        url = "https://data.mendeley.com/public-files/datasets/rscbjbr9sj/files/f12eaf6d-6023-432f-acc9-80c9d7393433/file_downloaded"
    print("Starting download...")
    try:
        # Makes data directory if it doesn't exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Send request to url
        req = requests.get(url)
        filename = f"{url.split('/')[-1]}.zip"
        with open(filename, "wb") as output_file:
            output_file.write(req.content)
        print("Download Complete")

        # Extracts usable files from downloaded zip file
        print("Extracting content")
        zipfile = ZipFile(BytesIO(req.content))
        zipfile.extractall(data_dir)
        print("Extraction complete")

        # Removes zip file
        os.remove(filename)
        if url == "https://data.mendeley.com/public-files/datasets/rscbjbr9sj/files/f12eaf6d-6023-432f-acc9-80c9d7393433/file_downloaded":
            shutil.rmtree(os.path.join(data_dir, "__MACOSX"))
    except Exception as e:
        print(f"An error occurred: {e}")