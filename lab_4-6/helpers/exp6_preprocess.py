import pandas as pd
import numpy as np

def exp6_preprocessing(data):
    """
    Experiment 6: Handle Missing Values and Outliers
    """
    # Missing Value Handling
    print("Handling Missing Values:")
    missing_before = data.isnull().sum()
    print(f"Missing Values Before:\n{missing_before}")
    
    # Fill missing numerical values with the mean
    numeric_cols = data.select_dtypes(include='number').columns
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
    
    # Fill missing categorical values with mode
    categorical_cols = data.select_dtypes(include='object').columns
    for col in categorical_cols:
        data[col] = data[col].fillna(data[col].mode()[0])
    
    missing_after = data.isnull().sum()
    print(f"Missing Values After:\n{missing_after}")
    
    # Outlier Handling: Replace outliers with boundaries using IQR
    print("\nHandling Outliers:")
    for col in numeric_cols:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = ((data[col] < lower_bound) | (data[col] > upper_bound)).sum()
        print(f"{col}: {outliers} outliers")
        
        # Capping outliers
        data[col] = np.where(data[col] < lower_bound, lower_bound, data[col])
        data[col] = np.where(data[col] > upper_bound, upper_bound, data[col])
    
    print("\nData preprocessing complete.")
    return data  # Return preprocessed data
