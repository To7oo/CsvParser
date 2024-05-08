import os, pandas as pd

print("""

=======================================
             CSV Parser
=======================================

""")



base_path = './data/'
list_of_files = os.listdir(base_path)

files_count = len(list_of_files)

print(f'Files found: {files_count}')

valid_files = []
invalid_files = []

for file in list_of_files:
    
    is_valid_file = os.path.isfile(base_path + file) & file.endswith('.csv')
    
    if is_valid_file:
        valid_files.append(base_path + file)
    else:
        invalid_files.append(base_path + file) 

valid_files_count = len(valid_files)
invalid_files_count = len(invalid_files)

print(f'Valid files: {valid_files_count}')
print(f'Invalid files: {invalid_files_count}\n')
print('Processing...')

newColumns = {
    'Dirección de correo electrónico': 'email',
    '¿Cuál es el nombre de tu emprendimiento?': 'Name',
    '¿Cuáles son las redes sociales de tu emprendimiento? Adjunta el link.': 'socialMedia'
}

filtered_keys =list(newColumns.values())

list_data = []

for path in valid_files:
    df = pd.read_csv(path)
    df.rename(columns=newColumns, inplace=True)
    subset = df[filtered_keys]
    list_data.append(subset)

pd.concat(list_data).to_csv(f"{base_path}output.csv", index=False)

print('Done!')