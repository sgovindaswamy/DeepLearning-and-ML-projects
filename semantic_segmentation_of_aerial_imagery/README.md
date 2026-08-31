# Semantic Segmentation of Aerial Imagery

This project applies deep learning to the task of semantic segmentation on aerial satellite imagery of Dubai. The goal is to classify each pixel in an aerial image into one of several semantic classes so that land cover and urban features can be mapped automatically.

## Overview

Semantic segmentation is a dense prediction task in which the model assigns a class label to every pixel in the image. This is particularly useful in geospatial analysis, urban planning, land-use mapping, and satellite image understanding.

In this project, the notebook builds a U-Net-inspired model from scratch using TensorFlow/Keras and trains it on aerial image patches and their corresponding segmentation masks.

---

## Dataset

The dataset is sourced from Kaggle and contains aerial imagery of Dubai along with labeled mask images.

### Data Characteristics

- image source: aerial satellite imagery
- target: semantic segmentation masks
- classes: multiple land-cover or building-related categories represented by RGB labels
- data format: image patches extracted from larger aerial scenes

The notebook preprocesses the dataset by:

- loading both image and mask files
- patchifying large images into smaller tiles
- converting segmentation masks from RGB labels to class-index maps
- splitting the dataset into train and test subsets

---

## Data Preprocessing

The dataset is processed carefully to prepare it for deep learning:

- large images are cropped to multiples of the patch size
- patches are extracted using `patchify`
- masks are matched to their corresponding image patches
- RGB masks are converted to class-encoded 2D label maps
- labels are then one-hot encoded for multi-class segmentation

The notebook performs a sanity check to visually inspect the matching between an image patch and its corresponding mask patch before training.

---

## Model Architecture

The model is a custom U-Net implementation defined in `simple_multi_unet_model.py`.

### U-Net Design

The architecture follows the classic encoder-decoder pattern:

- contraction path with convolutional layers and max pooling
- bottleneck with deeper feature extraction
- expansion path with transposed convolutions
- skip connections to preserve spatial information
- output layer with softmax activation for multi-class segmentation

### Key Architecture Details

The model includes:

- `Conv2D` blocks with ReLU activation
- `Dropout` regularization
- `MaxPooling2D` for downsampling
- `Conv2DTranspose` for upsampling
- `concatenate` layers for skip connections
- final segmentation head using `Conv2D(..., activation='softmax')`

This design is well suited for tasks where precise pixel-level localization matters.

---

## Loss Function and Training

The notebook uses a composite loss function built from:

- Dice loss
- focal loss

The model is trained with the following setup:

- optimizer: Adam
- loss: `dice_loss + focal_loss`
- metrics: segmentation metrics including IoU-based evaluation

The training pipeline is built to optimize both region overlap and class imbalance handling, which is important in aerial segmentation because some classes may occupy much smaller areas than others.

---

## Evaluation Metrics

The project evaluates its segmentation model using performance metrics suitable for pixel-wise prediction.

### Mean IoU

The notebook reports:

- Mean IoU = 0.6226041

This indicates that the model is performing reasonably well in identifying correct pixel classes across the test set, though there is still room for improvement.

The code also uses Keras `MeanIoU` for segmentation evaluation, which is one of the standard metrics for semantic segmentation tasks.

---

## Training Workflow

The notebook performs the following steps:

1. create image and mask patch datasets
2. convert masks to class-index labels
3. split data into train/test sets
4. train the U-Net model on patch data
5. save the trained model
6. evaluate predictions on a test image
7. visualize predicted segmentation output and compare it to the ground truth

The trained model is saved to:

- `model/unet_trained_100epochs_aerial.hdf5`

---

## Key Insights

1. Patch-based segmentation is effective for large aerial imagery.
2. U-Net is a strong choice when spatial detail matters.
3. The model learns a strong representation of urban land classes using skip connections.
4. IoU is the right metric for measuring segmentation quality because it focuses on overlap between true and predicted regions.

---

## Project Structure

- `aerial_imagery_32MB/`: dataset folders containing aerial images and masks
- `simple_multi_unet_model.py`: custom U-Net implementation
- `semantic_segmentation_aerial_images .ipynb`: notebook for preprocessing, training, and evaluation
- `requirements_aerial.txt`: dependencies for the project
- `model/unet_trained_100epochs_aerial.hdf5`: trained model checkpoint

---

## Conclusion

This project demonstrates how convolutional neural networks can be used for semantic segmentation of satellite imagery. The U-Net architecture is especially effective for this type of problem because it combines local spatial detail with contextual information from deeper layers.

The result is a practical pipeline for turning raw aerial images into structured segmentation maps that can be used for land classification, infrastructure analysis, and urban mapping.

---

## Suggested Next Steps

- train for more epochs with better augmentation
- experiment with different backbones or pre-trained encoders
- add class weighting for imbalanced segmentation masks
- evaluate with Dice coefficient, pixel accuracy, and per-class IoU
- scale the approach to larger aerial scenes without patch boundaries

