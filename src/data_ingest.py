import pandas as pd

class DataIngestion:
    """
    A class to load data from a file
    """
    def __init__(self,file_path):
        """
        initialize the class with the file path

        Args:
        
            file_path (_type__:str): the path to the file to be loaded
        """
        self.file_path = file_path
        
    def load_data(self):
        """
        Load data from a file

        Returns:
        
            _type__:pd.DataFrame: the data loaded from the file
        """
        return pd.read_csv(self.file_path)
    
    def getx_y(self):
        """
        Get the features and target columns from the data

        Returns:
        
            _type__:pd.DataFrame: the features and target columns
        """
        data = self.load_data()
        X = data["TV"]
        y = data["Sales"]
        df = pd.concat([X,y],axis = 1)
        return X,y,df