# Define the input file names and the output file path
number1 = 16
input_files = []

for j in range(0, number1-1):
    if j < 10:
        a1 = 0
        a0 = j
    else:
        a1 = 1
        a0 = j - 10

    for i in range(0, number1-1):
        if i < 10:
            b1 = 0
            b0 = i
        else:
            b1 = 1
            b0 = i - 10

        # Create the file path string and append it to the list
        input_files.append(f"C:/Users/USER/Desktop/درس مرس/ارشد/ترم 2/PROJECT/S-FED DR_2/sfedMode{a1}{a0}_{b1}{b0}.log")

output_file_path = 'C:/Users/USER/Desktop/درس مرس/ارشد/ترم 2/PROJECT/S-FED DR_2/trans.dat'

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
                if len(parts) == 16:
                    try:
                        # Attempt to convert both parts to floats (valid data line)
                        # float(parts[0])
                        float(parts[1])
                        float(parts[2])
                        float(parts[3])
                        float(parts[4])
                        float(parts[5])
                        float(parts[6])
                        float(parts[7])
                        float(parts[8])
                        float(parts[9])
                        float(parts[10])
                        float(parts[11])
                        float(parts[12])
                        float(parts[13])
                        float(parts[14])
                        float(parts[15])
                        data_lines.append(line)  # Add the valid data line
                    except ValueError:
                        continue  # Ignore non-numeric lines
            
            # Parse the second column values from the valid data lines
            second_column = [line.split()[9] for line in data_lines]

            # Extract the last 121 values from the second column
            last_121_values = second_column[-141:]
            last_121_values_fl = [float(line) for line in last_121_values]
            #all_values.extend(last_121_values_fl)  # Add to the master list
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
