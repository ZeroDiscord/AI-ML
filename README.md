
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

