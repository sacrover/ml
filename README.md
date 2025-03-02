# Machine Learning Projects

This repository contains a collection of my machine learning projects. Each project contains a well documented Jupyter Notebook (`.ipynb`) and its corresponding HTML export. These projects were accomplished during Data Analysis and Machine Learning graduate course at University of Toronto.


### 1️⃣ [Project 1: Anomaly Detection in Forest Cover Data](Gaussian%20Mixture%20Models/forest_cover_analysis.ipynb)

### Overview

This project focuses on detecting anomalies in forest cover data using statistical modeling techniques. The dataset contains 10 features with a small percentage of anomalies (0.96%).

### Key Components

- Dataset: Forest Cover Anomaly Dataset

- Analysis Methods:

    - Single & Multi-feature Gaussian models

    - One & Two-Gaussian approaches

    - Mixture of Gaussians for improved modeling

- Evaluation Metrics: F1-score, AUC


### 2️⃣ [Project 2: Diabetes Severity Classification and Feature Selection](KNN%20and%20Decision%20Trees/diabetes_severity.ipynb)

### Overview
This project focuses on predicting diabetes severity using a dataset containing various health features. The dataset includes 10 features and the target is based on whether diabetes severity is above or below the median value.

### Key Components

- **Dataset:** Diabetes Health Indicators Dataset

- **Analysis Methods:**
    - KNN Classification
    - Feature selection using decision trees
    - Cross-validation for hyperparameter tuning

### 3️⃣ [Project 3: Vaccination Data Analysis](PCA%20and%20SVD/covid_analysis.ipynb)


### Overview
This project focuses on analyzing COVID-19 vaccination data for multiple countries and performing dimensionality reduction techniques to explore trends and reconstruct time-series data. The dataset contains vaccination data for different countries across various dates.

### Key Components

- **Dataset:** COVID-19 Vaccination Data

- **Analysis Methods:**
    - **Time-Series Plotting:** Plot time-series for specified countries and standardize the data.
    - **Principal Component Analysis (PCA):** Compute covariance matrix, eigenvalues, eigenvectors, and visualize the contribution of principal components to explain the dataset's variance.
    - **Singular Value Decomposition (SVD):** Perform data decomposition using SVD and compare it with PCA results.


### 4️⃣ [Project 4: Superconductor Critical Temperature Prediction](Gradient%20Descent/critical_temp_superconductor.ipynb)

### Overview
This project focuses on predicting the critical temperature of a superconductors using a dataset that contains over 20,000 instances, with wide set of features. The goal is to predict the critical temperature (`critical_temp`) based on these features. The prediction model is implemented using linear regression with different techniques for optimization, including direct solution, full batch gradient descent, and mini-batch gradient descent.

### Key Components

- **Dataset:** Superconductor Dataset containing 21,263 instances and 81 features.

- **Analysis Methods:**
    - **Linear Regression:** Direct solution using matrix inversion.
    - **Full Batch Gradient Descent:** Implement gradient descent and track training time and RMSE evolution over epochs.
    - **Mini-Batch Gradient Descent:** Implement mini-batch gradient descent for various batch sizes and investigate convergence.
    - **Learning Rate Sensitivity:** Investigate the effect of learning rate on convergence for various batch sizes.





