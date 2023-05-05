# Cotton Crop Disease Detection using SWIN Transformers

This project is a machine learning-based solution to detect the disease in cotton crops using SWIN Transformers.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Results](#results)
- [Contributing](#contributing)

## Introduction
Cotton is one of the most important cash crops in many countries, and its cultivation faces various challenges, including the outbreak of diseases that can cause significant economic losses. Identifying the type of disease and the severity level in a timely manner is essential for effective disease management. This project proposes a deep learning-based solution to detect the disease in cotton crops using SWIN Transformers. We have trained the model on the publicly available [Cotton Disease Dataset](https://drive.google.com/drive/folders/1nJ6rhsY6pWfVPdxZsLEGOU0vwtaJs2N4?usp=share_link) and achieved state-of-the-art results in terms of accuracy.

## Installation
1. Clone this repository: 
```
git clone https://github.com/gallayagnesh/cotton-crop-disease-detection-using-SWIN_transformers.git
```
2. Install the required dependencies using pip:
```
pip install -r requirements.txt
```

## Usage
1. Download the [Cotton Disease Dataset](https://drive.google.com/drive/folders/1nJ6rhsY6pWfVPdxZsLEGOU0vwtaJs2N4?usp=share_link) and extract it to a directory named "dataset" in the project root directory.
2. Open a terminal in the project root directory and replace the dataset training images path in the python notebook.
3. After the model is trained, you can save the model for the deployment.

## Architecture
![Architecture Diagram](https://github.com/gallayagnesh/cotton_crop_disease_detection_using_SWIN_transformers/blob/main/SWIN%20Architecture.png)

## Results
Our model achieved a classification accuracy of 96.89% for the test dataset. The confusion matrix and classification report for the test set are included in the `results` directory.

## Contributing
Contributions to this project are welcome. To contribute, please fork the repository, create a new branch, and submit a pull request.

