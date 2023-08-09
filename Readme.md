(Insert catchy X-Ray image here)

# Chest X-Ray Images (Pneumonia) :satellite:

## Abstract :book:

This dataset, available on [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) and [Data Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/2), includes chest X-Ray images categorized into 2 categories: Pneumonia and Normal. The images are further separated into bacterial and viral pneumonia sets using labels gathered from their filenames. My first model will train a Convolutional Neural Netowrk to classify images as "pneumonia" or "nomral". Afterwards a second Convolutional Neural Network will be trained and attempts to classify images as "bacterial pneumonia" or "viral pneumonia".

## Dataset Information :globe_with_meridians:
<details>
  <summary> Dataset Structure </summary>
The dataset is organized into three main folders:

- train, validate and test.

The first model will access the subfolders of NORMAL and PNEUMONIA from the chest_xray directory.
The second model will access the subfolders of bacterial_pneumonia, viral_pneumonia and normal from the data directory.

</details>

## Goal :dart:
The goal of this project is to automatically classify X-Ray images into three categories: "Normal", "Viral Pneumonia" and "Bactrial Pneumonia".

## Acquire :inbox_tray:
When you run the notebook, it automatically downloads and sorts the ChestXRay2017 dataset from [Data Mendeley](https://data.mendeley.com/datasets/rscbjbr9sj/2). The original files are in the "chest_xray/train" and "chest_xray/test" folders. The files will be further sorted to separate viral from bacterial pneumonia images and placed in a train, validate and test set. The validation data is created from the train data set.

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
    
Pneumonia is not diagnosed just using chest x-rays. It is just a single piece of the puzzle. Here is how pneumonia presents in chest x-rays:

* <details>
    <summary>Viral pneumonia</summary>

    [Viral pneumonia](https://radiopaedia.org/articles/viral-respiratory-tract-infection-1?lang=us) frequently manifests in chest X-rays with an interstitial pattern, showcasing a fine reticular (net-like) appearance. This is due to the inflammation of the lung tissue between the air sacs. The X-ray might also present with peribronchial thickening, leading to a "hazy" or "ground-glass" appearance in the lungs. Viruses such as influenza, respiratory syncytial virus (RSV), and SARS-CoV-2 are common culprits. While the changes are often bilateral and widespread, they tend to be more subtle compared to bacterial pneumonia.
    
    Image: ![Viral pneumonia](viral-pneumonia.jpg)
    
    Credit: [Case](https://radiopaedia.org/cases/75217?lang=us) courtesy of Joachim Feger
  </details>

* <details>
    <summary>Bacterial pneumonia</summary>

    [Bacterial pneumonia](https://radiopaedia.org/articles/bacterial-pneumonia?lang=us) often results in an alveolar or 'air-space' pattern on chest X-rays. This is characterized by areas of increased opacity (whiteness) indicating consolidation, where the alveoli are filled with inflammatory cells and exudate. The borders of the heart and diaphragm might be obscured in the region of consolidation, a phenomenon known as 'silhouette sign'. The predominant pathogens include Streptococcus pneumoniae, Haemophilus influenzae, and Klebsiella pneumoniae. The consolidation can involve an entire lobe (lobar pneumonia) or appear as patchy areas across multiple lobes.
    
    Image: ![Bacterial pneumonia](bacterial-pneumonia.jpg)
    
    Credit: [Case](https://radiopaedia.org/cases/29090?lang=us) courtesy of Jack Ren
  </details>

* <details>
    <summary>Atypical pneumonia</summary>

    [Atypical pneumonia](https://radiopaedia.org/articles/atypical-pneumonia?lang=us) presents similar to bacterial pneumonia but is caused by a different bacteria. Opacities are normally located near the center of the chest where the blood enters and exits the lungs. This is the most common type of pneumonia when contracted in the general population, outside of a healthcare facility.
    
    Image: ![Atypical pneumonia](atypical-pneumonia.jpg)
    
    Credit: [Case](https://radiopaedia.org/cases/21993?lang=us) courtesy of Royal Melbourne Hospital Respiratory.
    
  </details>

* <details>
    <summary>Round pneumonia</summary>

    [Round pneumonia](https://radiopaedia.org/articles/round-pneumonia-1?lang=us) is usually only seen in pediatric patients. They are well defined, rounded opacities that represent regions of infected consolidation. The infective agent in round pneumonia is bacterial. The leading bacterial cause is streptococcus pneumoniae. It shows up on X-rays as a round-ish opacity, distinct from the surrounding tissue. Most cases occur in the top part of the lower lobes of the lungs.

    Image: ![Round Pneumonia](round-pneumonia.jpeg)

    [Video](https://youtu.be/taImIMRBLFk) describing what to look for in the chest x-ray.
  
    Credit:
    
    [Case](https://radiopaedia.org/cases/round-pneumonia-23?lang=us) courtesy of Ryan Thibodeau

  </details>

* <details>
    <summary>Cavitating pneumonia</summary>

    [Cavitating pneumonia](https://radiopaedia.org/articles/cavitating-pneumonia?lang=us) is a rare complication and associated with severe illness. Pediatric cases are most commonly caused by Streptococcus pneumoniae. It shows up on X-rays as darker spots or 'holes' that appear over the regular lung tissue. These darker spots indicate areas where the lung tissue has been damaged or lost due to the infection.

    Image: ![Cavitating Pneumonia](cavitating-pneumonia.jpg)

    [Video](https://www.youtube.com/watch?v=jtwOSdAH5sM)
    
    Credit:

    [Case](https://radiopaedia.org/cases/54686?lang=us) courtesy of Callum Smith
  </details>

* <details>
    <summary>Hemorrhagic pneumonia</summary>

    [Hemorrhagic pneumonia](https://radiopaedia.org/articles/haemorrhagic-pneumonia?lang=us) is a severe form of pneumonia where bleeding occurs within the lung parenchyma. On chest X-rays, it can manifest as areas of increased opacity, similar to consolidations seen in bacterial pneumonia. However, the distinct feature is the rapid progression and the presence of a dense, 'ground-glass' appearance indicating blood filling the alveoli. The areas of hemorrhage can be widespread or focal. Common pathogens causing hemorrhagic pneumonia include Staphylococcus aureus, especially the MRSA strain, and Klebsiella pneumoniae. It's essential to identify and treat this type swiftly due to its potential for rapid deterioration.
    
    Image: None

  </details>

</details>


## Resources:

- [Radiopaedia](https://radiopaedia.org/?lang=us)
- [Radiology Assistant](https://radiologyassistant.nl/)
- 


