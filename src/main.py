import os, pandas as pd

base_path = './data/'
list_of_files = os.listdir(base_path)

list_path = []

for file in list_of_files:
    
    is_valid_file = os.path.isfile(base_path + file) & file.endswith('.csv')
    
    if is_valid_file:
        list_path.append(base_path + file)
    else: 
        print(f'{base_path + file} is not a valid file')

newColumns = {
    'Dirección de correo electrónico': 'email',
    '¿Cuál es el nombre de tu emprendimiento?': 'Name',
    '¿Cuáles son las redes sociales de tu emprendimiento? Adjunta el link.': 'socialMedia'
}
filtered_keys =list(newColumns.values())

list_data = []

for path in list_path:
    df = pd.read_csv(path)
    df.rename(columns=newColumns, inplace=True)
    subset = df[filtered_keys]
    list_data.append(subset)

pd.concat(list_data).to_csv(f"{base_path}output.csv", index=False)