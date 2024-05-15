import os, pandas as pd
from plugins.data_manager import DataManager
from plugins.config_manager import ConfigManager

print("""

=======================================
             CSV Parser
=======================================

""")
    
print("Reading config...")
config = ConfigManager("config/config.json").get_config()

list_of_files = os.listdir(config.base_path)

files_amount = len(list_of_files)

print(f"Files found: {files_amount}\n")

valid_files = []
invalid_files = []

for file in list_of_files:
    
    is_valid_file = os.path.isfile(config.base_path + file) & file.endswith(".csv")
    print(f"Reading {config.base_path + file}")
    
    if is_valid_file:
        valid_files.append(config.base_path + file)
    else:
        invalid_files.append(config.base_path + file)

print("")

valid_files_count = len(valid_files)
invalid_files_count = len(invalid_files)

print(f"Valid files: {valid_files_count}")
print(f"Invalid files: {invalid_files_count}\n")

for invalid_file in invalid_files:
    print(f"Invalid file: {invalid_file}")

print("")

filtered_keys = list(config.get("column_keys").values())

list_data = []

for path in valid_files:
    
    dataManager = DataManager(path, config.get("column_keys"))
    
    columns = dataManager.dataframe.columns.values.tolist()
    
    elements_missing = list(set(filtered_keys) - set(columns))
    
    if len(elements_missing) == 0:
        subset = dataManager.dataframe[filtered_keys]
    else:
        sub_filtered_keys = filtered_keys.copy()
        for element in elements_missing:
            sub_filtered_keys.remove(element)
        subset = dataManager.dataframe[sub_filtered_keys]
        
    list_data.append(subset)

print("Generate output...")

root_dir = os.path.curdir

out_route = os.path.join(root_dir, config.output_folder_name)

if not os.path.exists(out_route):
    os.mkdir(out_route)

file_amount = len(os.listdir(out_route)) + 1
filename = f"output-{file_amount}.csv"

pd.concat(list_data).to_csv(f"{out_route}\\{filename}", index=False)
print(f"{filename} generated successfully!")
