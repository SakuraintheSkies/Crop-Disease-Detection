# Crop-Disease-Detection
## Description
This project  can be used as tool for widely assisting in the detection of diseases in crops like Wheat and Rice. 
basic crops like wheat and rice are used as datasets. and simple python program has been created in jupyter and VS code to implement the code.
## Table Of Contents
- Installation
- Usage
- Contribution
- Methodology
- Results
## Installation 
1. Download Anaconda Prompt for your PC.(https://www.anaconda.com/installation-success?source=installer)
   <br>-In The Prompt run the commands [pip install tensorflow , pip install keras, pip install streamlit, pip install numpy]
2. Download VScode.(https://code.visualstudio.com/download)
## Usage
1.Cost Efficiency:
<br>Using this project helps in reducing the need for broad-spectrum chemical applications by targeting specific disease outbreaks lowers input costs and minimizes labor requirements.
<br>2.Sustainability:
<br>Precise application of the tests done by the project enhances the sustainability of the crops quality.
<br>3.Scalability:
<br>Detection systems can be scaled to various sizes of farming operations, from smallholder farms to large agricultural enterprises, making the technology available for all.
## Contirbution
1.Enhanced Yield and Quality:
<br>Early detection of diseases allows for timely intervention, which can prevent significant yield loss and maintain the quality of the produce. This ensures a stable supply of food and maximizes the profitability for farmers.
<br>2.Precision Agriculture:
<br>Integrating disease detection systems into precision agriculture practices enables targeted treatments, reducing the use of pesticides and fertilizers. This not only lowers costs but also minimizes environmental impact. The project has been trained thoroughly to deal with as many samples of crops as uploaded.
<br>3.Data-Driven Decisions:
<br>Modern detection systems often involve data analytics and machine learning, providing farmers with actionable insights based on patterns and trends. This project tends to store the previous tests and assists in the precise detection of diseases.This facilitates informed decision-making regarding crop management strategies.
## Methodology
<br>1.Open command Promt and run the commands. [pip install tensorflow , pip install keras, pip install streamlit, pip install numpy,jupyter notebook]
<br>2.A jupyter Home page will open.
<br>3.Select the Folder for your project. the folder should be created before handedly .
<br>4.Three Main Folders are created -Testing -Training -Valid.
<br>5.Datasets are imported from the folder inide these folders separately. all these image datasets are read during training the Epochs.
<br>6.Datasets can be imported from these links as well as one can also use their downloaded datasets.Remember to copy the dataset in the project folder.<br>[https://www.kaggle.com/datasets/olyadgetch/wheat-leaf-dataset?resource=download]<br>[https://www.kaggle.com/datasets/nizorogbezuode/rice-leaf-images]
<br>7.In the Project folder create a Jupyter notebook named "Training".<br> [Training](https://github.com/SakuraintheSkies/Crop-Disease-Detection/blob/main/training.ipynb).
<br>8.For the precision of your project the number of epochs trained in the cnn model ca be increased.This facilotates the detection process and gives a high accuracy graph.
<br>9.After Training the model, now in the project folder create another jupyter noteboo named "Testing".<br> [Testing](https://github.com/SakuraintheSkies/Crop-Disease-Detection/blob/main/testing.ipynb).
<br>10.During Testing make sure to test as many Images as you can. this helps the model to train and validate the Images.
<br>11.after traning and testing is complete ,create a VS code file . This file should be created inside the project folder itself as well.
<br>12. in the VS code , open command prompt and run the following as per to activate your python environnment and connect the notebook to your python file .
<br>13. name the file as "main.py".<br>[Conda activate base,
<br>Conda activate tensorflow,
<br>Pip install streamlit]
<br>"Streamlit run main.py"activate this code after executing the code block in pytho environment. <br>[Main.py](https://github.com/SakuraintheSkies/Crop-Disease-Detection/blob/main/main.py)

### about CNN model
Convolutional Neural Networks (CNNs) are a class of deep learning algorithms that have proven highly effective for a variety of tasks, especially in image processing and computer vision.
<br>This project involves Use of CNN model at a very basic yet in a deep level to process the uploaded image .the images can be of different sizes , colour and resolution, the model works diversely on these images to give the best possible result.
### Epochs
An epoch is an integral part of Keras API which is used for one complete iteration over the entire training dataset.In this model we have a training dataset of 3761 images belonging to 7 classes so set the number of epochs to 30, the model will go through all 3761 images 30 times. 
#### Epochs are used as :
<br>1.Model Learning: Each epoch allows the model to learn and update its weights. More epochs mean the model has more opportunities to adjust its weights based on the data it sees.
<br>2.Convergence: Training for too few epochs can result in underfitting, where the model has not learned enough from the data. Training for too many epochs can lead to overfitting, where the model learns the training data too well, including its noise and outliers, reducing its ability to generalize to new data.For example , if I use only 10 epochs to train the model then its not trained well and during tesing it may muddle up the results. So to overcome this , I trained the model 30 times over to get even more precise answer.
<br>3.Monitoring Performance: In the code block we used  matplotlib library to import graphs , this happens to give us a metric view of the accuracy table and losses and gains during training. By monitoring metrics , you can determine how well the model is learning and whether it is converging or not. This helps a lot in deciding the number epochs that are required.
#### Determining the Number of Epochs:
<br>1.Trial and Error: Start with a reasonable number of epochs, then increase or decrease based on the model's performance.
<br>2.Early Stopping: Implement early stopping to halt training when the model's performance on a validation set stops improving, which helps prevent overfitting.
<br>3.Cross-Validation: Use cross-validation to determine the optimal number of epochs.
