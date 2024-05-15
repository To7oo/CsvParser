import pandas as pd

class DataManager:
    
    def __init__(self, path, column_keys):
        self.path = path
        self.column_keys = column_keys
        self.dataframe = pd.read_csv(path)
        
        self.rename_columns(column_keys)
        
    def rename_columns(self, column_keys):
        self.dataframe.rename(columns=column_keys, inplace=True)
        return self.dataframe
