import pandas as pd 

# Use raw string to avoid unicode escape errors
file_path = r"C:\Users\u819970\Downloads\blankSepTextFile.xlsx"

# Read the Excel file
df = pd.read_excel(file_path, engine='openpyxl')

# Add a new column 'Grade' with value 'A'
df['Grade'] = 'A'

# Concatenate 'Gender' and 'Grade' into a new column 'TOOT'
df['TOOT'] = df['Gender'] + df['Grade']

# Print the updated DataFrame
print("\n✅ Updated DataFrame:")
print(df) 

# Save the updated DataFrame to a new Excel file
new_file_path = r"C:\Users\u819970\Downloads\FILENEW.xlsx"
df.to_excel(new_file_path, index=False, engine='openpyxl')

# Print confirmation
print(f"\n✅ Updated DataFrame has been saved to: {new_file_path}")
