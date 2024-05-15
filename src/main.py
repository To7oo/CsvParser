import os, json, pandas as pd
from plugins.data_manager import DataManager

print("""

=======================================
             CSV Parser
=======================================

""")

with open("config/config.json") as json_file:
    config = json.load(json_file)
    
print("Reading config...")

base_path = config.get("base_path")
foldername = config.get("output_folder_name")

list_of_files = os.listdir(base_path)

files_count = len(list_of_files)

print(f"Files found: {files_count}\n")

valid_files = []
invalid_files = []

for file in list_of_files:
    
    is_valid_file = os.path.isfile(base_path + file) & file.endswith(".csv")
    print(f"Reading {base_path + file}")
    
    if is_valid_file:
        valid_files.append(base_path + file)
    else:
        invalid_files.append(base_path + file)

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
    
    df = dataManager.dataframe

    columns = df.columns.values.tolist()
    
    elements_missing = list(set(filtered_keys) - set(columns))
    
    if len(elements_missing) == 0:
        subset = df[filtered_keys]
    else:
        sub_filtered_keys = filtered_keys.copy()
        for element in elements_missing:
            sub_filtered_keys.remove(element)
        subset = df[sub_filtered_keys]
        
    list_data.append(subset)

print("Generate output...")

root_dir = os.path.curdir

out_route = os.path.join(root_dir, foldername)

if not os.path.exists(out_route):
    os.mkdir(out_route)

file_amount = len(os.listdir(out_route))
filename = f"output-{file_amount + 1}.csv"

pd.concat(list_data).to_csv(f"{out_route}\\{filename}", index=False)
print("Done!")
