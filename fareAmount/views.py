from django.shortcuts import render
from joblib import load
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

model = load('./savedModel/model1.joblib')
scaler = load('./savedModel/scaler1.joblib')

car_mapping = { 'Bad': 0,
    'Excellent': 1,
    'Good': 2,
    'Very Good': 3}
weather_mapping = {'cloudy': 0, 'rainy': 1, 'stormy': 2, 'sunny': 3, 'windy': 4}
traffic_mapping = {'Congested Traffic': 0, 'Dense Traffic': 1, 'Flow Traffic': 2}

def predictor(request):
    if request.method == 'POST':
        
        data = request.POST.dict()  
        input_data = pd.DataFrame([data])

        
        int_features = ['passenger_count', 'hour', 'day', 'month', 'weekday', 'year']
        float_features = ['jfk_dist', 'ewr_dist', 'lga_dist', 'sol_dist', 'nyc_dist', 'distance', 'bearing']

        for col in int_features:
            input_data[col] = input_data[col].astype(int)

        for col in float_features:
            input_data[col] = input_data[col].astype(float)

       
        input_data['Car Condition'] = input_data['car_condition'].map(car_mapping)
        input_data['Weather'] = input_data['weather'].map(weather_mapping)
        input_data['Traffic Condition'] = input_data['traffic_condition'].map(traffic_mapping)

        
        feature_order = ['Car Condition', 'Weather', 'Traffic Condition', 'passenger_count', 
                         'hour', 'day', 'month', 'weekday', 'year', 
                         'jfk_dist', 'ewr_dist', 'lga_dist', 'sol_dist', 'nyc_dist', 
                         'distance', 'bearing']
        input_data = input_data[feature_order]

        print(input_data)

        scaled_features = scaler.transform(input_data)
        fare_amount = model.predict(scaled_features)[0]

        return render(request, 'main.html', {'result': round(fare_amount, 2)})

    return render(request, 'main.html')