(Insert catchy X-Ray image here)

# Chest X-Ray Images (Pneumonia) :satellite:

## Abstract :book:

This dataset, available on [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) and [Data Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/2), includes chest X-Ray images categorized into 2 categories: Pneumonia and Normal. The images are further separated into bacterial and viral pneumonia sets using labels gathered from their filenames. Afterwards a Convolutional Neural Network is trained and attempts to classify unseen images from the test set into their respective diagnosis.

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
When you run the notebook, it automatically downloads and sorts the ChestXRay2017 dataset from [Data Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/2). The original files are in the "chest_xray/train" and "chest_xray/test" folders. The files will be further sorted to separate viral from bacterial pneumonia images and placed in a train, validate and test set. The validation data is created from the train set.

## Data Dictionary
- X-ray
- pneumonia
- contrast
- [Compton Scattering](https://www.nde-ed.org/Physics/X-Ray/comptonscattering.xhtml)

## More information:

<details>
    <summary> Pneumonia </summary>
    
Pneumonia is an infection of the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material) which limits their ability to take in oxygen or expel carbon dioxide. A variety of infective agents can cause pneumonia including: bacteria, viruses and fungi. Viral pneumonia is usually mild and goes away on its own but can progress into bacterial pneumonia. Fungi pneumonia is less common. It usually occurs in people with chronic health problems or weakened immune systems and is not identified in this dataset.

- [Pneumonia](https://medlineplus.gov/pneumonia.html)
- [Viral Pneumonia](https://www.webmd.com/lung/viral-pneumonia)
- [Bacterial Pneumonia](https://www.webmd.com/lung/bacterial-pneumonia)
- [Types of Pneumonia](https://www.webmd.com/lung/pneumonia-types)

[Bronchitis](https://www.healthline.com/health/bronchitis-vs-pneumonia#similarities-differences) is a similar condition where the bronchial tubes become inflamed and usually produced mucus. Bronchitis is usually less severe but can lead to the development of pneumonia.
</details>

<details>
    <summary> Chest X-Ray </summary>
Chest x-rays are done for many reasons including the detection of pneumonia. A film or sensor is placed on one side of an object (in this case the chest cavity) and a shielded x-ray source on the other. The source will be briefly exposed, allowing high energy electromagnetic radiation, similar to light, to pass through the object and be collected by the film or sensor. X-rays darken or "expose" the film. As the x-rays pass through the object, they will interact with matter based on how dense it is. This is called Compton Scattering. The denser a material is, the more scattering takes place and less x-rays reach the film or sensor. Areas on the film or sensor that receive a lot of x-rays are black and areas that do not are white. The difference is called contrast. It allows us to see soft materials such as skin and muscle as a darker gray and harder materials such as metal and bones as a lighter gray. Pneumonia is detectable due to the buildup of mucus in the lungs. The mucus or liquid will scatter more x-rays, resulting in a lighter pattern in those areas versus areas filled with air or gases.

[Radiology Website](https://radiologyassistant.nl/chest/chest-x-ray/lung-disease)

</details>

<details>
    <summary> Pneumonia in chest x-rays </summary>
    
Pneumonia presents in four different ways in chest x-rays:

<details>
    <summary>Atypical pneumonia</summary>
    
[Atypical pneumonia](https://radiopaedia.org/articles/atypical-pneumonia?lang=us)
Image:
Credit:
</details>

<details>
    <summary>Round pneumonia</summary>

[Round pneumonia](https://radiopaedia.org/articles/round-pneumonia-1?lang=us) is usually only seen in pediatric patients. They are well defined, rounded opacities that represent regions of infected consolidation. The infective agent in round pneumonia is bacterial. The leading bacterial cause is streptococcus pneumoniae. It usually presents in a round-ish opacity, distinct from the surrounding tissue. Most cases occure in the top part of the lower lobes of the lungs.

Image:
Credit:
[Case](https://radiopaedia.org/cases/round-pneumonia-23?lang=us) courtesy of [Ryan Thibodeau](https://radiopaedia.org/)
</details>

<details>
    <summary>Cavitating pneumonia</summary>
    
[Cavitating pneumonia](https://radiopaedia.org/articles/cavitating-pneumonia?lang=us)
Image:
Credit:
</details>

<details>
    <summary>Hemorrhagic pneumonia</summary>
    
[Hemorrhagic pneumonia](https://radiopaedia.org/articles/haemorrhagic-pneumonia?lang=us)
Image:
Credit:
</details>

</details>

## Resources:

- [Radiopaedia](https://radiopaedia.org/?lang=us)
- [Radiology Assistant](https://radiologyassistant.nl/)
- 


