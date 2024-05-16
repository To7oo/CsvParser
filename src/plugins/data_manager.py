import pandas as pd

class DataManager:
    
    dataframe: pd.DataFrame
    
    def __init__(self, column_keys):
        self.column_keys = column_keys
        
    def read_file(self, filename):
        self.dataframe = pd.read_csv(filename)
        
    def rename_columns(self, column_keys):
        self.dataframe.rename(columns=column_keys, inplace=True)
        return self.dataframe
    
    def get_missing_columns(self, column_list: list) -> list:
        current_columns = set(self.dataframe.columns.values.tolist())
        given_columns = set(column_list)
        
        return list(given_columns.difference(current_columns))

    def create_subset(self, column_list: list) -> pd.DataFrame:
        return self.dataframe[column_list]
    
    def process_files(self, files: list):
        
        list_data = []
        filtered_keys = list(self.column_keys.values())
        
        for file in files:
            self.read_file(file)
            missing_columns = self.get_missing_columns(filtered_keys)
            
            if len(missing_columns) == 0:
                subset = self.create_subset(filtered_keys)
            else:
                sub_filtered_keys = filtered_keys.copy()
                for column in missing_columns:
                    sub_filtered_keys.remove(column)
                subset = self.create_subset(sub_filtered_keys)
        
            list_data.append(subset)
        
        self.dataframe = pd.concat(list_data)
    
    def render(self, path: str):
        self.dataframe.to_csv(path, index=False)