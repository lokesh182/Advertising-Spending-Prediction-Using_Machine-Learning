import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class DataPreprocessing:
    def __init__(self,df):
        self.df = df
        
    def identify_outliers(self,data:pd.DataFrame):
        """
        Identify outliers in the data
        Args:
            data (pd.DataFrame):    the data to be analyzed
        
        Returns:
            pd.DataFrame:    a dataframe containing the outliers
        """
        
        fig,ax = plt.subplots() 
        ax.boxplot(data)
        ax.set_title("Box plot the data")
        ax.set_ylabel("Value")
        plt.show()
    
    def identify_outliers_zscore(self,data:pd.Series,threshold:float = 3):
        """
        Identify outliers in the data using the z-score method
        Args:
            data (pd.Series):    the data to be analyzed
            threshold (float):    the threshold for the z-score
        
        Returns:
            pd.Series:    a series containing the outliers
        """
        
        mean = np.mean(data)
        std = np.std(data)
        z_scores = (data-mean)/std
        outliers = data[np.abs(z_scores)>threshold]
        return outliers