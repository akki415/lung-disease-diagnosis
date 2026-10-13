# Lung Disease Diagnosis Using Deep Learning

## 📌 Project Overview

The **Lung Disease Diagnosis Using Deep Learning** project aims to classify lung diseases from medical images using deep learning techniques. By leveraging image preprocessing and model-based classification, the system analyzes medical images and predicts the corresponding disease category.

The project demonstrates the application of artificial intelligence and computer vision in medical image analysis, with the goal of supporting research into automated disease classification.

## 🎯 Objectives

- Develop a deep learning model for lung disease classification.
- Preprocess medical images to prepare them for model training and evaluation.
- Train and evaluate the model using a labeled image dataset.
- Predict disease categories from input medical images.
- Explore the potential of AI-assisted medical image analysis.

## ✨ Key Features

- **Image Preprocessing:** Prepares input images for deep learning.
- **Automated Classification:** Predicts disease categories based on learned image patterns.
- **Model Training:** Supports training a deep learning model on labeled medical images.
- **Performance Evaluation:** Enables assessment using appropriate classification metrics.
- **Scalable Approach:** Can be extended to additional disease categories or datasets.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Deep Learning:** TensorFlow/Keras or PyTorch *(specify the framework used)*
- **Image Processing:** OpenCV, Pillow
- **Data Analysis:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Development Environment:** Jupyter Notebook / Google Colab / VS Code

## 📂 Project Structure

```text
Lung-Disease-Diagnosis/
│
├── dataset/                # Medical image dataset (if included)
├── notebooks/              # Experiments and model development
├── models/                 # Saved trained models
├── src/                    # Source code
├── results/                # Evaluation results and visualizations
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── main.py                 # Main execution script (if applicable)
```

*Update the directory structure to match your actual repository.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux/macOS**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure that `requirements.txt` contains the libraries required by your implementation.

## 🚀 Usage

1. Download or prepare the dataset used for training and evaluation.
2. Place the dataset in the appropriate directory.
3. Run the training notebook or training script to train the model.
4. Load the trained model.
5. Provide a supported medical image to generate a predicted class.

For example, if your project uses a Python entry point:

```bash
python main.py
```

*Replace this command with the actual execution steps for your project.*

## 🧠 MODEL ARCHITECTURE
Here the architecture is completely made from scratch using 
7 convolution block $ 3 deep fully connected layers.
CNN is used as backbone of architecture.
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1          [-1, 8, 222, 222]             224
              ReLU-2          [-1, 8, 222, 222]               0
       BatchNorm2d-3          [-1, 8, 222, 222]              16
         MaxPool2d-4          [-1, 8, 111, 111]               0
            Conv2d-5         [-1, 20, 109, 109]           1,460
              ReLU-6         [-1, 20, 109, 109]               0
       BatchNorm2d-7         [-1, 20, 109, 109]              40
         MaxPool2d-8           [-1, 20, 54, 54]               0
            Conv2d-9            [-1, 8, 52, 52]           1,448
             ReLU-10            [-1, 8, 52, 52]               0
      BatchNorm2d-11            [-1, 8, 52, 52]              16
        MaxPool2d-12            [-1, 8, 26, 26]               0
           Conv2d-13           [-1, 20, 26, 26]             180
             ReLU-14           [-1, 20, 26, 26]               0
      BatchNorm2d-15           [-1, 20, 26, 26]              40
           Conv2d-16           [-1, 36, 24, 24]           6,516
             ReLU-17           [-1, 36, 24, 24]               0
      BatchNorm2d-18           [-1, 36, 24, 24]              72
           Conv2d-19           [-1, 20, 22, 22]           6,500
             ReLU-20           [-1, 20, 22, 22]               0
      BatchNorm2d-21           [-1, 20, 22, 22]              40
           Conv2d-22           [-1, 36, 22, 22]             756
             ReLU-23           [-1, 36, 22, 22]               0
      BatchNorm2d-24           [-1, 36, 22, 22]              72
           Conv2d-25            [-1, 8, 20, 20]           2,600
             ReLU-26            [-1, 8, 20, 20]               0
      BatchNorm2d-27            [-1, 8, 20, 20]              16
AdaptiveAvgPool2d-28              [-1, 8, 1, 1]               0
           Linear-29                   [-1, 64]             576
             ReLU-30                   [-1, 64]               0
           Linear-31                   [-1, 32]           2,080
             ReLU-32                   [-1, 32]               0
           Linear-33                    [-1, 2]              66
================================================================
Total params: 22,718
Trainable params: 22,718
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.57
Forward/backward pass size (MB): 17.68
Params size (MB): 0.09
Estimated Total Size (MB): 18.34
----------------------------------------------------------------


## 🧠 Model Development

The project follows a typical deep learning workflow:

1. **Data Collection:** Obtain a labeled medical image dataset.
2. **Preprocessing:** Resize images, normalize pixel values, and prepare labels as required.
3. **Dataset Splitting:** Separate data into training, validation, and test sets.
4. **Model Training:** Train a suitable deep learning architecture on the training data.
5. **Evaluation:** Assess performance using metrics such as accuracy, precision, recall, F1-score, and a confusion matrix.
6. **Prediction:** Use the trained model to classify previously unseen images.

## 📊 Results and Evaluation

Model performance should be reported using results obtained from the actual test dataset.

| Metric | Result |
|---|---|

| Accuracy | 89 |
EPOCH, 5 
 ---------------------------------
loss = 0.2697784900665283 Batchid = 2341, Accuracy = 88.07: 100%|██████████| 2342/2342 [02:16<00:00, 17.18it/s]   
Test error: 
Accuracy: 89.07849829351535 %,  Avg loss: 0.21


## 🔮 Future Improvements

- Experiment with advanced architectures such as ResNet, EfficientNet, or DenseNet.
- Apply data augmentation to improve model generalization.
- Add Grad-CAM visualizations to help interpret model predictions.
- Develop a web interface for image upload and prediction.
- Evaluate model robustness on independent datasets.

## OPENING THE APP 

 1. Clone the repository
 2. create your virtual environment
 3. Install are the requirements
 4. in your terminal use following command
 5. Make sure you are in correct directory
 
  cd "Lung Disease Diagonisis"
  python -m uvicorn app:app --reload
  http://127.0.0.1:8000/docs

  you will get something like
  
## ⚠️ Disclaimer

This project is intended for educational and research purposes only. Its predictions are not a substitute for professional medical advice, clinical diagnosis, or evaluation by a qualified healthcare professional. The model's reliability depends on the dataset, training methodology, and independent validation.


