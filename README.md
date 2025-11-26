Algerian Forest Fires Dataset – ML Prediction Project

This project uses the Algerian Forest Fires Dataset from the UCI Machine Learning Repository to build a Machine Learning model that predicts forest fire occurrence based on meteorological and Fire Weather Index (FWI) parameters.

Dataset Source

The dataset is publicly available on the UCI ML Repository:
Algerian Forest Fires Dataset (UCI)
Origin: 2012–2015 forest fire records collected from north-eastern Algeria
Regions: Bejaia and Sidi Bel-Abbes

Dataset Description

The dataset contains 244 instances and 11 meteorological + FWI features, including:

Temperature
Relative Humidity (RH)
Wind Speed (Ws)
Rain
Fine Fuel Moisture Code (FFMC)
Duff Moisture Code (DMC)
Initial Spread Index (ISI)
Classes (Fire / No Fire)
Region (Bejaia = 1, Sidi Bel-Abbes = 0)

Project Objectives

Clean and preprocess the Algerian forest fire dataset
Perform EDA (Exploratory Data Analysis)
Train and evaluate ML models for fire prediction
Export the final model using Pickle
Build a Flask web application for real-time prediction
Deploy UI form for user input (Temperature, RH, Ws, FFMC, etc.)

Machine Learning Workflow

Data Preprocessing
Feature Scaling
Train/Test Split
ML Algorithms 
Hyperparameter Tuning
Model Evaluation (R², Accuracy, RMSE, etc.)
Model Serialization (model.pkl)

Flask Web App Features

Clean HTML form for input
Backend ML inference
POST data handling
Predictive output returned to UI


Technologies Used

Python
pandas, numpy
scikit-learn
matplotlib, seaborn
Flask
HTML, CSS & JavaScript
Pickle (Model Serialization)




📢 Note

This project is for research and educational purposes using publicly available data from the UCI Machine Learning Repository.
