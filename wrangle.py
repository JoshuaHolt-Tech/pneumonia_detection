import os, requests, zipfile, shutil, random
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
        print("Extracting files")
        zipfile = ZipFile(BytesIO(req.content))
        zipfile.extractall(data_dir)
        print("Files extracted")

        # Removes zip file
        os.remove(filename)
        #Removes macOS metadata file if it exists
        if os.path.exists(os.path.join(data_dir, "__MACOSX")):
            shutil.rmtree(os.path.join(data_dir, "__MACOSX"))
    except Exception as e:
        print(f"An error occurred: {e}")

def prepare_data(random_seed=1969):
    """
    This function checks if folders exist and processes images if not. 
    Model 1 will use the `data/chest_xray/` folders.
    Model 2 will use the `data/` folders.
    """
    if random_seed != None:
        random.seed(random_seed)

    # First model path variables
    train_norm_path = "data/chest_xray/train/NORMAL/"
    train_pneu_path = "data/chest_xray/train/PNEUMONIA/"
    val_norm_path = "data/chest_xray/val/NORMAL/"
    val_pneu_path = "data/chest_xray/val/PNEUMONIA/"
    test_norm_path = "data/chest_xray/test/NORMAL/"
    test_pneu_path = "data/chest_xray/test/PNEUMONIA/"

    # Second model path variables
    train_path = "data/train/"
    val_path = "data/val/"
    test_path = "data/test/"

    new_path_list = [train_path, val_path, test_path]

    # Builds file directory for first model
    for path in [val_norm_path, val_pneu_path]:
        if not os.path.exists(path):
            os.makedirs(path)

    # Builds file directory for second model
    for path in new_path_list:
        if not os.path.exists(path):
            os.makedirs(path)
            os.makedirs(os.path.join(path, "viral_pneumonia"))
            os.makedirs(os.path.join(path, "bacterial_pneumonia"))
            os.makedirs(os.path.join(path, "normal"))

    # Move 300 NORMAL train images to validate directories
    train_norm_files = []
    for file in os.listdir(train_norm_path):
        if file.endswith(".jpeg"):
            train_norm_files.append(file)

    # Randomly selects 300 random samples, moves to `val/NORMAL` folder and copies to `data/val/normal` folder.
    for file in random.sample(train_norm_files, 300):
        source = os.path.join(train_norm_path, file)
        destination0 = os.path.join(val_norm_path, file)
        destination1 = os.path.join("data/val/normal/", file)
        shutil.move(source, destination0)
        shutil.copy(destination0, destination1)

    viral_indicator = "virus"
    bacterial_indicator = "bacteria"
    
    #Get a list of pneumonia image files to parce
    train_pneu_files = []
    for file in os.listdir(train_pneu_path):
        if file.endswith(".jpeg"):
            train_pneu_files.append(file)

    # Seperte bacterial and viral pneumonia images
    unknown_pneumonia_files = 0
    viral_files = []
    bacterial_files = []
    for file in train_pneu_files:
        if file.find("virus") != (-1):
            viral_files.append(file)
        elif file.find("bacteria") != (-1):
            bacterial_files.append(file)
        else:
            unknown_pneumonia_files += 1

    # Checking if files don't have indicators
    if unknown_pneumonia_files > 0:
        print(f"Files with unknown pneumonia type in val: {unknown_pneumonia_files}")

    # Gathering samples
    sampled_viral = random.sample(viral_files, 300)
    sampled_bacterial = random.sample(bacterial_files, 300)

    # Moving viral pneumonia files to validate folder and coping for second model
    for file in sampled_viral:
        source = os.path.join(train_pneu_path, file)
        destination0 = os.path.join(val_pneu_path, file)
        destination1 = os.path.join("data/val/viral_pneumonia/", file)
    
        shutil.move(source, destination0)
        shutil.copy(destination0, destination1)

    # Moving bacterial pneumonia files to validate folder and coping for second model
    for file in sampled_bacterial:
        source = os.path.join(train_pneu_path, file)
        destination0 = os.path.join(val_pneu_path, file)
        destination1 = os.path.join("data/val/bacterial_pneumonia/", file)
    
        shutil.move(source, destination0)
        shutil.copy(destination0, destination1)

    # Copy normal test images for second model
    for file in os.listdir(test_norm_path):
        if file.endswith(".jpeg"):
            source = os.path.join(test_norm_path, file)
            destination = os.path.join("data/test/normal/", file)
            shutil.copy(source, destination)

    # Separate bacterial and viral pneumonia images, then copy for second model
    unknown_pneumonia_files = 0
    for file in os.listdir(test_pneu_path):
        source = os.path.join(test_pneu_path, file)
        if file.find("virus") != (-1):
            destination = os.path.join("data/test/viral_pneumonia/", file)
            shutil.copy(source, destination)
        elif file.find("bacteria") != (-1):
            destination = os.path.join("data/test/bacterial_pneumonia/", file)
            shutil.copy(source, destination)
            bacterial_files.append(file)
        else:
            unknown_pneumonia_files += 1

    # Checking if files don't contain indicators
    if unknown_pneumonia_files > 0:
        print(f"Files with unknown pneumonia type in test: {unknown_pneumonia_files}")