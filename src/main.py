import os, pandas as pd

print("""

=======================================
             CSV Parser
=======================================

""")

base_path = "./data/"
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

new_columns = {
    "Dirección de correo electrónico": "email",
    "¿Cuál es el nombre de tu emprendimiento?": "name",
    "¿Cuáles son las redes sociales de tu emprendimiento? Adjunta el link.": "socialMedia"
}

filtered_keys =list(new_columns.values())

list_data = []

for path in valid_files:
    
    df = pd.read_csv(path)
    
    df.rename(columns=new_columns, inplace=True)
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
pd.concat(list_data).to_csv(f"{base_path}output.csv", index=False)

print("Done!")