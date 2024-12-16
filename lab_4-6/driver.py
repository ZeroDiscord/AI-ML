import requests
from helpers.exp4_impexp import exp4_import_export
from helpers.exp5_eda import exp5_eda
from helpers.exp6_preprocess import exp6_preprocessing
    
if __name__ == "__main__":
    DATASET_URL = "https://udacity-dsnd.s3.amazonaws.com/sparkify/mini_sparkify_event_data.json"
    print("Downloading dataset from", DATASET_URL)
    res = requests.get(DATASET_URL)
    with open("data/mini_sparkify_event_data.json", "wb") as f:
        f.write(res.content)
        
    DATASET_PATH = "data/mini_sparkify_event_data.json"
    
    # Import and Export
    exp4_import_export(DATASET_PATH)
    
    # Exploratory Data Analysis
    exp5_eda(DATASET_PATH)
    
    # Preprocessing
    exp6_preprocessing(DATASET_PATH)
    
    
