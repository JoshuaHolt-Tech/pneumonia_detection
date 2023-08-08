(Insert catchy X-Ray image here)

# Chest X-Ray Images (Pneumonia) :satellite:

## Abstract :book:

This dataset, available on [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) and [Data Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/2), includes chest X-Ray images categorized into 2 categories: Pneumonia and Normal. The images are further separated into bacterial and viral pneumonia sets using labels gathered from their filenames. Afterwards a Convolutional Neural Network is trained and attemps to classify unseen images from the test set into their respective diagnosis.

## Dataset Information :globe_with_meridians:
<details>
  <summary> Dataset Structure </summary>
The dataset is organized into three main folders:

- train, validate and test.

Each of these folders contains three subfolders:

- bacterial_pneumonia, viral_pneumonia and normal

</details>

## Goal :dart:
The goal of this project is to train a neural network model to classify X-Ray images into three categories: "Normal", "Viral Pneumonia" and "Bactrial Pneumonia".

## Acquire :inbox_tray:
When you run the notebook, it automatically downloads and sorts the ChestXRay2017 dataset from [Data Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/2). The origional files are in the "chest_xray/train" and "chest_xray/test" folders. The files will be further sorted to seperate viral from bacterial pneumonia images and placed in a train, validate and test set. The validation data is created from the train set.

## More information:
<details>
    <summary> Pneumonia </summary>
    
Pneumonia is an infection of the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material). A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia. Pneumonia can start as viral or bacterial. Viral pneumonia is usally mild and goes away on its own but can progress into bacterial pneumonia. Fungi pneumonia is less common. It usually occures in people with chronic health problems or weakened immune systems and is not identified in this dataset.

[Pneumonia](https://medlineplus.gov/pneumonia.html)
[Viral Pneumonia](https://www.webmd.com/lung/viral-pneumonia)
[Bacterial Pneumonia](https://www.webmd.com/lung/bacterial-pneumonia)
[Types of Pneumonia](https://www.webmd.com/lung/pneumonia-types)

[Bronchitis](https://www.healthline.com/health/bronchitis-vs-pneumonia#similarities-differences) is a similar condition where the bronchial tubes become inflamed and usually produced mucus. Bronchitis is usually less severe but can lead to the development of pneumonia.
</details>
<details>
    <summary> Chest X-Ray </summary>

[Radiology Website](https://radiologyassistant.nl/chest/chest-x-ray/lung-disease)

</details>
