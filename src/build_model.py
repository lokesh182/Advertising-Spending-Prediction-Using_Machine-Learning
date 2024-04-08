import statsmodels.api as sm
class SimpleLinearRegression:
    
    
    def __init__(self,x,y):
        """
        Initialize the class with the data

        Args:
            x (pd.series):   the independent variable
            y (_type_):  the dependent variable
        """
        self.x = x
        self.y = y
        self.x = sm.add_constant(self.x)
        
    def fit(self):
        """
        Fit the model to the data
        
        returns:
            model: the fitted model
            
        """
        model = sm.OLS(self.y,self.x).fit()
        return model
    
    def summary(self):
        """
        Get the summary of the model
        
        """

        return self.fit().summary()
    