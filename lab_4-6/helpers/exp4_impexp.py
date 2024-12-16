import pandas as pd

def exp4_import_export(dataset_path):
    """
    Experiment 4: Import and Export Data with Dataset Details
    """
    # Import dataset
    data = pd.read_json(dataset_path, lines=True)
    
    # Export to CSV
    exported_path = "data/exported_dataset.csv"
    data.to_csv(exported_path, index=False)
    print(f"Dataset exported to {exported_path}\n")
    
    # Dataset details
    print("Dataset Details:")
    print(f"Number of Rows: {data.shape[0]}")
    print(f"Number of Columns: {data.shape[1]}")
    print("First 5 Rows:")
    print(data.head())
    print(f"Size of Dataset: {data.size}")
    print("\nMissing Values Per Column:")
    print(data.isnull().sum())
    print("\nSummary Statistics for Numerical Columns:")
    print(data.describe())
    # sum mean min max for numerical columns
    sum = data.sum()
    mean = data.mean()
    minimum = data.min()
    maximum = data.max()
    print(f"Sum:\n{sum}")
    print(f"Mean:\n{mean}")
    print(f"Minimum:\n{minimum}")
    print(f"Maximum:\n{maximum}")
    
    return data  # Return the dataset for further experiments