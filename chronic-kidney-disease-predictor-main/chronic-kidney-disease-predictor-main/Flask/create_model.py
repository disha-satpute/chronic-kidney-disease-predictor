import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

def create_model():
    # Load the dataset
    # The dataset path is relative to the location of this script
    df = pd.read_csv('..\dataset\kidney_disease.csv')

    # --- Data Preprocessing ---

    # Drop the 'id' column as it's not a feature
    df.drop('id', axis=1, inplace=True)

    # Clean column names (remove tabs and spaces)
    df.columns = [col.strip() for col in df.columns]

    # Define categorical and numerical columns
    categorical_cols = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane', 'classification']
    numerical_cols = ['age', 'bp', 'sg', 'al', 'su', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc']

    # Replace '?' with NaN and clean up whitespace issues
    for col in df.columns:
        df[col] = df[col].replace('?', np.nan)
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()

    # Convert numerical columns to numeric type, coercing errors
    for col in numerical_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Impute missing values
    # For numerical columns, use the mean
    for col in numerical_cols:
        df[col].fillna(df[col].mean(), inplace=True)
    # For categorical columns, use the mode
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Encode categorical features
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])

    # --- Model Training ---

    # Separate features (X) and target (y)
    X = df.drop('classification', axis=1)
    y = df['classification']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # --- Save the Model ---

    # Save the trained model to a file
    with open('CKD.pkl', 'wb') as file:
        pickle.dump(model, file)

    print("Model 'CKD.pkl' created successfully!")

if __name__ == '__main__':
    create_model()
