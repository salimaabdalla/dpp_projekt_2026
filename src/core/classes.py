import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from math import nan

from sklearn.base import BaseEstimator, TransformerMixin
from imblearn.pipeline import Pipeline 

class DataImputation(TransformerMixin, BaseEstimator):
    """Imputs missing values. """
    
    def __init__(self):
        """Initalizes the attributes."""
        self.features = []
        self.num_cols = []
        self.dict_num = {}

    def fit(self, X, y=None):
  
        self.num_cols = list(X.select_dtypes(exclude='object').columns)
        self.dict_num = {col: X[col].median() for col in self.num_cols}
        return self
    
    def transform(self, X, y=None):
        """Fill the missing values and drop some columns.
        
        
        """
        df = X.copy()
        for col in self.num_cols:
            if df[col].isna().sum() > 0:
                df.loc[df[col].isna(), col] = self.dict_num[col]

        self.features = df.columns.values
        return df
    
    def get_feature_names_out(self, input_features=None):
        """Returns the names of the features."""
        return self.features
    

class FeatureEngineer(TransformerMixin, BaseEstimator):  
    """Generates new features."""
    
    def __init__(self, dict_lag):
        """Initalizes the attributes."""
        self.features = []
        self.dict_lag = dict_lag
    
    def fit(self, X, y=None):
        """DocString  """
        df = X.copy()
        return self
    
    def transform(self, X, y=None):
        """Generate new columns. """        
        
        df = pd.DataFrame.from_dict({'date':X.index})
        df = df.set_index('date')
        for col in self.dict_lag.keys(): 
            lags = self.dict_lag[col]
            for lag in lags:
                if lag > 0:
                    df[col + '_lag_by_' + str(lag)] = X.loc[:, col ].shift(lag)
                else:
                    df[col ] = X.loc[:, col ]

        self.features = df.columns.values
        return df
    
    def get_feature_names_out(self, input_features=None):
        """Returns the names of the features."""
        return self.features
