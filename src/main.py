import os, pandas as pd
from plugins.data_manager import DataManager
from plugins.config_manager import ConfigManager
from utilities.ui import print_title
from utilities.validate_files import validate_files

print_title()
print("Reading config...")

config = ConfigManager("config/config.json").get_config()

filename_list = os.listdir(config.base_path)

files_list = [os.path.join(config.base_path, file) for file in filename_list]

print(f"Files found: { len(files_list) }\n")

valid_files, invalid_files = validate_files(files_list)

print(f"Valid files: {len(valid_files)}")
print(f"Invalid files: {len(invalid_files)}\n")

for invalid_file in invalid_files:
    print(f"Invalid file: {invalid_file}")

print("")

dataManager = DataManager(config.column_keys)

dataManager.process_files(valid_files)

print("Generate output...")

root_dir = os.path.curdir
out_route = os.path.join(root_dir, config.output_folder_name)

if not os.path.exists(out_route):
    os.mkdir(out_route)

file_amount = len(os.listdir(out_route)) + 1
filename = f"output-{file_amount}.csv"
path = os.path.join(out_route, filename)

dataManager.render(path)
print(f"{filename} generated successfully!")
