import pandas as pd

file_path = '.xlsx'
df = pd.read_excel(file_path)

#Function for priority

def assign_priority(value):
    if value == "Must have":
        return "P1"
    elif value == "Must not have":
        return "P3"
    else:
        return "P4"

# Apply the function to the relevant column
# Replace 'Requirement' with the actual column name in your Excel file
df['Priority'] = df['Requirement'].apply(assign_priority)

# Save the updated DataFrame to a new Excel file
output_file_path = 'Vishal_Demo.xlsx'  #desired output file path
df.to_excel(output_file_path, index=False)

print(f"Updated Excel file saved to {output_file_path}")