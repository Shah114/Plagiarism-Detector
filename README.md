## Plagiarism-Detector
This repository contains a Plagiarism Detection project that uses machine learning models to identify instances of plagiarism in textual data. The project includes data preprocessing, feature extraction, model training, and a simple web application for interacting with the trained model. <br/>
<br/>

## Project Overview 
Plagiarism detection is a crucial task in various fields such as academia, journalism, and content creation. This project implements a machine learning approach to detect plagiarism using several classification algorithms. After comparing the performance of multiple models, the Support Vector Machine (SVM) model was selected due to its superior accuracy. <br/>
<br/>

**Models Used** <br/>
The following machine learning models were trained and evaluated: <br/>
* Logistic Regression
* Random Forest
* Naive Bayes
* Support Vector Machine (SVM) <br/>

Among these, the SVM model provided the best results and was chosen for the final implementation. <br/>
<br/>

**Dataset** <br/>
The dataset used for training the models was obtained from the AI with NOOR YouTube channel. The dataset consists of labeled pairs of text, indicating whether one text is a plagiarized version of the other. <br/>
<br/>

## Project Structure
* PlagiarismDetector.ipynb: This Jupyter notebook contains the data preprocessing steps, including tokenization and feature extraction, as well as the training and evaluation of the machine learning models. 
* app.py: This Python script serves as the backend for the web application. It uses Flask to create an interface where users can input text and receive predictions on whether the text is plagiarized.
* templates/: This directory contains the HTML files used to render the web application interface.
* static/: This directory contains static assets such as CSS files and images used in the web application. <br/>
<br/>

## How to Run 
![image](https://github.com/user-attachments/assets/cb89224f-3990-4531-8f38-c08cb85e5e48)
<br>

## Future Work
* Model Optimization: Experiment with hyperparameter tuning for the SVM model to further improve accuracy.
* Advanced Features: Implement additional features such as handling different file formats (e.g., PDF, DOCX) and providing detailed reports on detected plagiarism.
<br/>

## Acknowledgments
AI with NOOR YouTube Channel: The dataset for this project was sourced from the AI with NOOR YouTube channel.
* https://youtu.be/eK1fS-QmVaE?si=m3C6YbGTjfaYob_B




