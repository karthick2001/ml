import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(file_path='C:/Users/Windows/Desktop/ml1/ml/data/iris.csv'):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    X = data.drop(columns=['species'])
    y = data['species']

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    preprocessed_data = pd.DataFrame(X_scaled, columns=X.columns)
    preprocessed_data['species'] = y_encoded

    return preprocessed_data

def split_data(data, test_size=0.2, random_state=42):
    X = data.drop(columns=['species'])
    y = data['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def save_data(data, path='C:/Users/Windows/Desktop/ml1/ml/data/processed_data.csv'):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    data.to_csv(path, index=False)
    print(f"Preprocessed data saved to {path}")

if __name__ == "__main__":
    raw_data = load_data()
    preprocessed_data = preprocess_data(raw_data)
    save_data(preprocessed_data)
    X_train, X_test, y_train, y_test = split_data(preprocessed_data)
    print("Data split into training and test sets.")
