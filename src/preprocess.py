# src/preprocess.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(file_path='data/iris.csv'):
    """
    Load the Iris dataset from a CSV file.
    
    Args:
    file_path (str): Path to the CSV file containing the dataset.
    
    Returns:
    pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """
    Preprocess the Iris dataset by encoding labels and scaling features.
    
    Args:
    data (pd.DataFrame): Raw Iris dataset.
    
    Returns:
    pd.DataFrame: Preprocessed data.
    """
    # Separate features and target variable
    X = data.drop(columns=['species'])  # Features (all columns except species)
    y = data['species']  # Target (species column)

    # Encode target variable (species) into numerical labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Scale features using StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create a new DataFrame with scaled features and encoded target
    preprocessed_data = pd.DataFrame(X_scaled, columns=X.columns)
    preprocessed_data['species'] = y_encoded

    return preprocessed_data

def split_data(data, test_size=0.2, random_state=42):
    """
    Split the dataset into training and test sets.
    
    Args:
    data (pd.DataFrame): The preprocessed dataset.
    test_size (float): Proportion of the dataset to include in the test split.
    random_state (int): Random seed to ensure reproducibility.
    
    Returns:
    tuple: Four sets - X_train, X_test, y_train, y_test.
    """
    X = data.drop(columns=['species'])
    y = data['species']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def save_data(data, path='data/processed_data.csv'):
    """
    Save the preprocessed data to a CSV file.
    
    Args:
    data (pd.DataFrame): The preprocessed dataset.
    path (str): Path to save the processed data CSV file.
    """
    data.to_csv(path, index=False)
    print(f"Preprocessed data saved to {path}")

if __name__ == "__main__":
    # Load the data
    raw_data = load_data()

    # Preprocess the data
    preprocessed_data = preprocess_data(raw_data)

    # Save the preprocessed data
    save_data(preprocessed_data)
    
    # Optionally, split the data for model training and evaluation
    X_train, X_test, y_train, y_test = split_data(preprocessed_data)
    print("Data split into training and test sets.")
