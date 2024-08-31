# src/train.py

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from preprocess import load_data, preprocess_data, split_data

def train_model(X_train, y_train):
    """
    Train a RandomForestClassifier on the training data.
    
    Args:
    X_train (pd.DataFrame): Training features.
    y_train (pd.Series): Training labels.
    
    Returns:
    RandomForestClassifier: Trained model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the test set.
    
    Args:
    model (RandomForestClassifier): The trained model.
    X_test (pd.DataFrame): Test features.
    y_test (pd.Series): Test labels.
    
    Returns:
    dict: A dictionary containing the accuracy and classification report.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=['setosa', 'versicolor', 'virginica'])
    
    evaluation = {
        "accuracy": accuracy,
        "classification_report": report
    }
    
    return evaluation

def save_model(model, path='model.pkl'):
    """
    Save the trained model to a file.
    
    Args:
    model (RandomForestClassifier): The trained model.
    path (str): The path where the model should be saved.
    """
    joblib.dump(model, path)
    print(f"Model saved to {path}")

if __name__ == "__main__":
    # Load and preprocess data
    raw_data = load_data()
    preprocessed_data = preprocess_data(raw_data)
    
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = split_data(preprocessed_data)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluation = evaluate_model(model, X_test, y_test)
    print(f"Model accuracy: {evaluation['accuracy']}")
    print("Classification Report:")
    print(evaluation['classification_report'])
    
    # Save the trained model
    save_model(model)
