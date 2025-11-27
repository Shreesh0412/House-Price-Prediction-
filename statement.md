# House Price Prediction System

## 1. Problem Statement
Determining the fair market value of a residential property is a complex challenge for buyers and sellers alike. Property prices are influenced by multiple factors such as the total area, the number of bedrooms (BHK), and the age of the building. Without a data-driven approach, stakeholders often rely on intuition or incomplete information, leading to overpricing or undervaluation. This project aims to solve this by providing an automated tool that uses historical data to estimate accurate property prices.

## 2. Scope of the Project
The scope of this project is to develop a machine learning-based application that:
* Ingests and processes historical housing datasets (CSV format).
* Trains a **Linear Regression** model to understand the relationship between property features and price.
* Provides a user-friendly Command Line Interface (CLI) for real-time predictions.
* Validates user inputs to ensure realistic predictions.

**Limitations:** The current scope is limited to using Linear Regression on a static dataset. It does not currently account for location-specific data (e.g., city or neighborhood) or real-time market fluctuations.

## 3. Target Users
* **Home Buyers:** Individuals looking to verify if a quoted price for a house is reasonable based on its features.
* **Property Sellers:** Owners who want to set a competitive and fair asking price for their property.
* **Real Estate Agents:** Professionals needing a quick estimation tool to assist clients during initial consultations.

## 4. High-Level Features
* **Data Ingestion:** Automated loading and validation of CSV datasets to ensure data integrity.
* **Model Training:** On-demand training of a Linear Regression model using Scikit-Learn.
* **Price Prediction:** Real-time estimation of house prices based on user inputs (Area, BHK, Age).
* **Input Validation:** Robust error handling to reject invalid inputs (e.g., negative values or text).
* **System Logging:** A centralized logging mechanism to track runtime errors and system events for debugging.
