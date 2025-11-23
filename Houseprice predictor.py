
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

def load_data(a):
    try:
        if not os.path.exists(a):
            print("File not found at {a}.")
        df = pd.read_csv(a)
        print("Success: Data loaded.")
        return df
    except Exception as e:
        print("Error loading data: {e}")
        return None

def train_model(df):
    required_columns = ['Area_sqft', 'BHK', 'Age_years', 'Price']
    if not all(col in df.columns for col in required_columns):
        print(f"Error: CSV must contain columns: {required_columns}")
        return None

    x=df[['Area_sqft', 'BHK', 'Age_years']]
    y=df['Price']
    
    model=LinearRegression()
    model.fit(x, y)
    print("Success: Model trained.")
    return model

def predict_price(model):
    if model is None:
        print("Error: Model is not trained. Cannot predict.")
        return
    print("\n--- House Price Predictor ---")
    try:
        area = float(input("Enter Area (in sqft): "))
        bhk = int(input("Enter number of BHK: "))
        age = int(input("Enter Age of house (in years): "))
        if area <= 0 or bhk <= 0 or age < 0:
             print("Error: Area, BHK, and Age must be positive values.")
             return
        i=pd.DataFrame([[area, bhk, age]],columns=['Area_sqft', 'BHK', 'Age_years'])
        prediction = model.predict(i)[0]
        if prediction<0:
            prediction=0
            print("Note: The inputs provided suggest a very low value house.")
        print(f"\nEstimated House Price: {prediction:.2f} Lakhs")
    except ValueError:
        print("Input Error: Please enter valid numbers only.")
while True:
    path = ('/Users/shreesh12/Desktop/dataset.csv')
    dataframe = load_data(path)
    trained_model = train_model(dataframe)
    predict_price(trained_model)
    a=input("Do you wish to continue? (y/n)")
    if a=='n' or a=='N':
        print("You chose to exit")
        break
    else:
        print("Running one more time...")
