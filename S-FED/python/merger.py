import os

# Define the range of files to merge
input_files = [f"C:/Users/USER/Desktop/vgs_0/transformed{i}.dat" for i in range(0, 12+1)]  # 0.dat to 12.dat
output_file = "C:/Users/USER/Desktop/vgs_0/merged.dat"

# Initialize a list to store all data
all_data = []

# Read each file and append its content to all_data
for file_name in input_files:
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            all_data.extend(lines)
        print(f"Added data from {file_name}")
    else:
        print(f"File {file_name} not found. Skipping...")

# Write all the data to the output file
with open(output_file, 'w') as file:
    file.writelines(all_data)

print(f"All data merged into {output_file}")
