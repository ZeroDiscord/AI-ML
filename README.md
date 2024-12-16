# [Lab Experiments](https://github.com/ZeroDiscord/AI-ML/tree/master/lab_4-6)

## Lab 4-6: Data Import, EDA, and Preprocessing

### Overview  
This repository covers three experiments:  
1. **Experiment 4**: Import/export data and display basic statistics.  
2. **Experiment 5**: Perform Exploratory Data Analysis (EDA).  
3. **Experiment 6**: Handle missing values, outliers, and preprocess data.  

### File Structure 
```
lab_4-6/
│
├── data/            # Directory for input datasets
│   └── sample.csv   # Placeholder for the dataset used in experiments
│
├── helpers/         # Contains scripts for individual experiments
│   ├── exp4_impexp.py   # Code for Experiment 4
│   ├── exp5_eda.py      # Code for Experiment 5
│   └── exp6_preprocess.py   # Code for Experiment 6
│
├── output/          # Stores exported results, plots, and preprocessed data
│   └── ...
│
└── driver.py        # Main driver script to run experiments
```

### Requirements  
- Python 3.x  
- Libraries: `pandas`, `matplotlib`, `seaborn`, `scipy`  

### How to Run  
1. Place the dataset in the `data/` directory OR simply run the driver script to import the sample dataset. 
2. Execute the main script:  
   ```bash
   python driver.py
   ```
3. Outputs for evaluation are present in the `output/` directory.


<br><br><br>

# [Project](https://github.com/ZeroDiscord/AI-ML/tree/master/project)

### Machine Learning Pipeline
This Demonstrates the creation and training of a machine learning pipeline using `scikit-learn`. The pipeline consists of two main components:

1. **StandardScaler**: Standardizes the features by removing the mean and scaling to unit variance.
2. **RandomForestClassifier**: A classifier that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

#### Code Overview


#### Steps:

1. **Import Libraries**: Import the necessary libraries from `scikit-learn`.
2. **Define Pipeline**: Create a pipeline that first scales the data using `StandardScaler` and then applies the `RandomForestClassifier`.
3. **Train the Model**: Fit the pipeline to the training data (`X_train`, `y_train`).

This setup ensures that the data is properly scaled before being fed into the classifier, which can improve the performance of the model.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Create a pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier())
])

# Fit the pipeline
pipe.fit(X_train, y_train)
```

### References
- [scikit-learn: Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
- [Dataset: Sparkify](https://udacity-dsnd.s3.amazonaws.com/sparkify/mini_sparkify_event_data.json)

