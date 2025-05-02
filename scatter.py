import numpy as np # For numerical computations
import pandas as pd # For handling tabular data
# Set a random seed for reproducibility
np . random . seed (42)
true_values = np . random . normal ( loc =50 , scale =10 , size =1000)
# Add noise to generate predicted values based on true values
predicted_values = true_values + np . random . normal ( loc =0 ,
scale =5 , size =1000)

true_values [::50] += np . random . normal ( loc =20 , scale =10 , size
=20)
predicted_values [::50] += np . random . normal ( loc =20 , scale =10 ,
size =20)
# Combine the data into a DataFrame
data = pd . DataFrame ({
'True ': true_values ,
'Predicted ': predicted_values
})

import matplotlib . pyplot as plt # For plotting
from scipy . stats import zscore # For calculating Z- Score
def scatter_plot_with_outliers ( data ) :
    plt . figure ( figsize =(10 , 6) ) # Set figure size
# Scatter plot for all data points
    plt . scatter ( data ['True '] , data ['Predicted '] , alpha =0.7 ,
    label ='Data ␣ Points ')
# Calculate Z- Scores for outlier detection
    z_scores = zscore ( data [[ 'True ', 'Predicted ']])
    outliers = np .abs( z_scores ) > 3 # Identify outliers with
# Highlight outliers in red
    plt . scatter ( data ['True '][ outliers .any( axis =1) ] ,
    data ['Predicted '][ outliers .any ( axis =1) ] ,
    color ='red', label ='Outliers ')

    # Add labels , legend , and grid
    plt . title (" Scatter Plot with Outliers Marked ")
    plt . xlabel (" True Values ")
    plt . ylabel (" Predicted Values ")
    plt . legend ()
    plt . grid ()
    plt . show ()
    # Call the function to plot
scatter_plot_with_outliers ( data )