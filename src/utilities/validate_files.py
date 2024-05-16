import os

def validate_files(files_list: list) -> tuple:
    
    valid_files = []
    invalid_files = []
    
    for file in files_list:
        print(f"Reading: {file}")
        
        if os.path.isfile(file) & file.endswith(".csv"):
            valid_files.append(file)
        else:
            invalid_files.append(file)
            
    print("")
    
    return (valid_files, invalid_files)