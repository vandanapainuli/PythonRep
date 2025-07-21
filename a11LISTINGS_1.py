
import pandas as pd
import os

# Define the folder path
folder_path = 'C:\\Users\\u819970\\Downloads\\TEST\\Datasets'

# Correctly define the list of files
files_to_update = ['DEMO_AE.xlsx', 'DEMO_MH.xlsx', 'DEMO_CM.xlsx', 'DEMO_PE.xlsx', 'DEMO_DM.xlsx']

# Loop through each file, add a new column, and save the updated file
for file in files_to_update:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)

    # Add new column 'SOURCE'
    df['SOURCE'] = 'Created on Python'

    # Save the updated file with a new name
    new_file_name = file.replace('.xlsx', '_MOD.xlsx')
    new_file_path = os.path.join(folder_path, new_file_name)
    df.to_excel(new_file_path, index=False)
