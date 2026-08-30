# Define the input file names and the output file path
number1 = 12
input_files = [f"C:/Users/USER/Desktop/درس مرس/ارشد/ترم 2/PROJECT/VGS/vgs_0/{i}.dat" for i in range(0, number1+1)]  # Replace with your file names if different
output_file_path = 'C:/Users/USER/Desktop/درس مرس/ارشد/ترم 2/PROJECT/VGS/vgs_0/transformed.dat'

# Initialize a list to store all the extracted data
all_values = []

# Process each input file
for file_name in input_files:
    try:
        # Read the file line by line
        with open(file_name, 'r') as file:
            data_lines = []
            for line in file:
                # Check if the line contains two valid numeric values
                parts = line.split()
                if len(parts) == 2:
                    try:
                        # Attempt to convert both parts to floats (valid data line)
                        float(parts[0])
                        float(parts[1])
                        data_lines.append(line)  # Add the valid data line
                    except ValueError:
                        continue  # Ignore non-numeric lines
            
            # Parse the second column values from the valid data lines
            second_column = [float(line.split()[1]) for line in data_lines]

            # Extract the last 121 values from the second column
            last_121_values = second_column[-121:]
            all_values.extend(last_121_values)  # Add to the master list

    except FileNotFoundError:
        print(f"File {file_name} not found. Skipping...")
    except Exception as e:
        print(f"An error occurred while processing {file_name}: {e}")

# Write all the extracted values to the output file
with open(output_file_path, 'w') as output_file:
    for value in all_values:
        output_file.write(f"{value}\n")

print(f"All data saved to {output_file_path}")
