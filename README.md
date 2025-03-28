
# 🚖 Fare Amount Prediction Web App (ML + Django)

This web application allows users to **predict the fare amount for a taxi ride** based on specific ride details.  
It combines **machine learning (Random Forest Regression)** with a **Django-based web interface** for end-to-end interaction.

---

## 📚 Table of Contents

- [🎥 Demo](#-demo)
- [✅ What the App Does](#-what-the-app-does)
- [📊 Features Used in the Model](#-features-used-in-the-model)
- [📁 Project Structure](#-project-structure)
- [🧼 Data Exploration & Preprocessing](#-data-exploration--preprocessing)
- [📈 Model Training](#-model-training)
- [🌐 Web App with Django](#-web-app-with-django)
- [📥 Downloads](#-downloads)

---

## 🎥 Demo

[Click to Watch Demo](https://github.com/sarakhataam/Uber_Fare_Amount_Prediction/issues/1#issuecomment-2758060736))


---

## ✅ What the App Does

1. 🎯 **Predicts Fare Amount**  
   Based on input features like:
   - Pickup & dropoff location
   - Date & time of ride
   - Passenger count
   - Weather, traffic, and car condition

2. 📈 **Processes User Input**  
   - Extracts time-based features
   - Calculates Haversine distance to NYC landmarks
   - Handles missing or unexpected inputs

3. 🧠 **Uses a Trained ML Model**  
   A `RandomForestRegressor` trained on historical taxi data with enriched features.

4. 🌐 **Interactive Web Interface**  
   Users can input ride details and get instant fare prediction via a user-friendly Django app.

---

## 📊 Features Used in the Model

The model uses the following features:

- `Car Condition`
- `Weather`
- `Traffic Condition`
- `passenger_count`
- `hour`, `day`, `month`, `weekday`, `year`
- `jfk_dist`, `ewr_dist`, `lga_dist`, `sol_dist`, `nyc_dist`
- `distance` (Haversine distance)
- `bearing` (direction angle between pickup and dropoff)
- `fare_amount` (target)

---

## 📁 Project Structure

![Image](https://github.com/user-attachments/assets/e79889dc-7345-4ef8-8b54-92028a7eeee3)

---

## 🧼 Data Exploration & Preprocessing

- **Exploratory Data Analysis (EDA)** done using `pandas`, `matplotlib`, and `seaborn`
- Outlier removal for extreme distances and fare values
- Feature engineering:
  - Time-based features from `pickup_datetime`
  - Haversine distance and bearing calculation
  - Distance to NYC landmarks like JFK, LGA, Times Square, etc.
- One-hot encoding for categorical variables (e.g., Weather)

---

## 📈 Model Training

- Algorithm: `RandomForestRegressor`
- Framework: `scikit-learn`
- Steps:
  - Train/test split (80/20)
  - GridSearch for tuning hyperparameters (optional)
  - Model evaluation using RMSE, MAE, and R² score
- Final model serialized using `joblib` (`model1.joblib`)

---

## 🌐 Web App with Django

- Django form takes user inputs for ride parameters
- Backend loads the trained model and processes features
- Prediction returned and displayed in results page
- Templates styled with basic Bootstrap for clarity

---
### 📥 Downloads

- 📁 **Dataset** (for training & testing):  
  [Download from Google Drive](https://drive.google.com/drive/folders/1dAYekToXZ28mrvj9GaKLH3Bx-ExDEMfp?usp=drive_link)

- 🎯 **Trained Model & Scaler** (for predictions):  
  [Download from Google Drive](https://drive.google.com/drive/folders/1AnfA6LM4SolZ8pFkcnDmypWc_RS6dVJ9?usp=drive_link)










