import matplotlib.pyplot as plt
import seaborn as sns
def exp5_eda(data):
    """
    Experiment 5: Perform Exploratory Data Analysis
    """
    # Count plot of user levels
    plt.figure(figsize=(8, 5))
    sns.countplot(data=data, x='level')
    plt.title("User Level Distribution")
    plt.show()
    
    # Distribution of song lengths
    plt.figure(figsize=(8, 5))
    sns.histplot(data=data, x='length', kde=True, bins=30)
    plt.title("Distribution of Song Lengths")
    plt.show()
    
    # # Churn analysis by user level ( can be done only if 'churn' column is present after preprocessing )
    # if 'churn' in data.columns:
    #     plt.figure(figsize=(8, 5))
    #     sns.barplot(data=data, x='level', y='churn', estimator='mean')
    #     plt.title("Average Churn Rate by User Level")
    #     plt.show()
    # else:
    #     print("'churn' column not found in the dataset.")
    
    # Pairplot for numerical features
    numeric_cols = data.select_dtypes(include='number').columns
    if len(numeric_cols) > 1:
        sns.pairplot(data[numeric_cols].sample(min(500, len(data)) if len(data) > 500 else len(data)))
        plt.show()
    
    print("EDA completed. Visualizations generated.")
