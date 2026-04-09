# Heart Disease Diagnostic System 🩺
A Python-based clinical decision support tool that utilizes the **Gaussian Naïve Bayes** algorithm to predict the probability of heart disease based on patient vitals.

## ystem Overview
This project demonstrates the application of Bayesian inference in healthcare. By analyzing features like Age, Blood Pressure, and Cholesterol, the model calculates a posterior probability to assist medical professionals in identifying highrisk patients.

## User Interface & Experience
The application features a custom GUI built with **Tkinter**, designed for ease of use in a clinical setting. Users can input patient data and receive an instant diagnostic recommendation backed by a probability score.

![Diagnostic Interface](screenshots/Diagnostic%20interface.png)

*The interface allows for rapid data entry and provides immediate visual feedback on the diagnostic result.*

## Diagnostic Output
When the "Results" button is triggered, the system calculates the posterior probability using the Naïve Bayes engine and provides a clear decision support message.

![Diagnostic Result](screenshots/Results.png) 

*Example of the system identifying a high-risk case with a high posterior probability score.*

## Performance & Evaluation
To ensure reliability, the system includes a built-in performance reporting module. The model is evaluated on a test split to measure its accuracy and sensitivity.
**Note on Dataset Scale:** Since this is a curated demonstration dataset of 18 records, the 20% test split consists of 4 total samples. The **2 and 0 results** indicate that the model perfectly classified all 4 test cases. While the results are nearly equal to 1 (100% accuracy), this is a "Proof of Concept" showing that the Gaussian Naïve Bayes logic correctly identified the distinct patterns in our clinical data without error.

### Confusion Matrix Analysis
The matrix below shows the count of True Positives and True Negatives. In our testing phase, the model achieved **100% Accuracy** with **Zero False Negatives**, which is a critical safety metric for medical software.

![Confusion Matrix](screenshots/Confusion%20matrix.png)

### Summary of Results
The following metrics represent the model's predictive power:
* **Accuracy:** 100%
* **Precision:** 1.0
* **Recall:** 1.0 (Ensuring all sick patients are identified)
* **F1-Score:** 1.0

![Performance Graph](screenshots/Performance%20graph.png)

*Visual summary of the model's accuracy, precision, and recall scores.*
