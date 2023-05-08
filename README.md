# Cotton Crop Disease Detection using SWIN Transformers

This project is a Deep learning and Computer vision-based solution to detect the disease in cotton crops using SWIN Transformers.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Dataset](#dataset)
- [Architecture](#architecture)
- [Implementation](#implementation)
- [Results](#results)
- [Contributing](#contributing)

## Introduction
Cotton is one of the most important cash crops in many countries, and its cultivation faces various challenges, including the outbreak of diseases that can cause significant economic losses. Identifying the type of disease and the severity level in a timely manner is essential for effective disease management. This project proposes a deep learning-based solution to detect the disease in cotton crops using SWIN Transformers. We have trained the model on the publicly available [Cotton Disease Dataset](https://drive.google.com/drive/folders/1nJ6rhsY6pWfVPdxZsLEGOU0vwtaJs2N4?usp=share_link) and achieved state-of-the-art results in terms of accuracy.

## Installation
1. Clone this repository: 
```
git clone https://github.com/gallayagnesh/cotton_crop_disease_detection_using_SWIN_transformers.git
```
2. Install the required dependencies using pip:
```
pip install -r requirements.txt
```

## Prerequisites

1. Python3
2. Spyder IDE


## Dataset

This dataset contains a total of 5816 photos of Cotton leaves that have been divided into four categories or classes. Download the [Cotton Disease Dataset](https://drive.google.com/drive/folders/1nJ6rhsY6pWfVPdxZsLEGOU0vwtaJs2N4?usp=share_link) and extract it to a directory named "dataset" in the project root directory.

### Dataset Split

Out of the total images, 4652 photos were used for training the model and 1164 images were used for validating the model.

### Category Distribution

The four categories in the dataset along with the number of images in each category are listed below:

| Category | No. of Images |
| --- | --- |
| Healthy | 848 |
| Bacterial Blight | 838 |
| Curl Virus | 1078 |
| Fusarium Wilt | 3052 |

As can be seen from the above table, there is an imbalance in the distribution of images across categories, with Fusarium Wilt having a significantly larger number of images compared to the other categories. This is because Fusarium Wilt is the most common local disease found in cotton crops. 

This dataset can be used to train and evaluate models for identifying different types of cotton leaf diseases and can be useful for researchers working in the field of agriculture and plant pathology.

## Architecture
![Architecture Diagram](https://github.com/gallayagnesh/cotton_crop_disease_detection_using_SWIN_transformers/blob/main/SWIN%20Architecture.png)
The Swin Transformer architecture can be divided into two main components:
Patch embedding stage and Hierarchical transformer stage.

In the patch embedding stage, the input image is first divided into non-overlapping patches of a fixed size. Each patch is then linearly projected into a lower-dimensional vector, which is passed through a small feedforward network to generate an initial feature representation.

In the hierarchical transformer stage, the network processes the patches in a hierarchical manner using multiple stages of transformer blocks. Each stage contains a certain number of transformer blocks, and each block consists of two layers: a Swin layer and a Shift layer.

The Swin layer applies a multi-head self-attention mechanism to the input patches, allowing the network to capture global relationships between them. Specifically, the Swin layer applies a self-attention operation to each patch, and then uses another set of linear projections to combine the information across all patches. This operation is similar to the self-attention mechanism used in the original Transformer architecture.

The Shift layer shifts the positions of the patches in a structured manner, which helps to reduce computational complexity and improve efficiency. Specifically, the Shift layer first divides the patches into groups, and then shifts the positions of the patches within each group. This operation creates overlapping regions between adjacent patches, which helps to capture more local information about the input image.

The output of each stage is then passed through a downsampling layer, which reduces the resolution of the patches and prepares them for processing in the next stage. This process is repeated for several stages until the final output, which is a vector of probabilities indicating the predicted class of the input image.

Learn more about SWIN Transformers, [read this article](https://towardsdatascience.com/a-comprehensive-guide-to-swin-transformer-64965f89d14c).

## Implementation

1. Replace the dataset folder path with your working dataset directory path.
2. After execution, save the model for the deployment.
3. Run the ```app.py``` in the Spyder IDE.
4. In the terminal, there will be a local host address. Open it and upload the image which have to be detected. Those uploaded images are saved in the ```webapp/static``` folder.

## Results
This model achieved a classification accuracy of 96.89% for the test dataset. The confusion matrix, classification report for the test set and also deployment results are included in the `results` directory.

## Contributing
Contributions to this project are welcome. To contribute, please fork the repository, create a new branch, and submit a pull request.

