# Define the input file names and the output file path
number1 = 22   #(range of vgs or vgd) + 1  ---> exp : -0.4 to 1.6 --> 21+1 = 22
input_files = []

for j in range(0, number1-1):
    if j < 10:
        a1 = 0
        a0 = j
    elif (j < 20) and (j >= 10 ):
        a1 = 1
        a0 = j - 10
    else:
        a1 = 2
        a0 = j - 20

    for i in range(0, number1-1):
        if i < 10:
            b1 = 0
            b0 = i
        elif (i < 20) and (i >= 10 ):
            b1 = 1
            b0 = i - 10
        else:
            b1 = 2
            b0 = i - 20

        # Create the file path string and append it to the list
        input_files.append(f"C:/Users/USER/Desktop/درس مرس/ارشد/ترم 2/PROJECT/S-FED DR_capG/sfedMode{a1}{a0}_{b1}{b0}.log")

output_file_path = 'C:/Users/USER/Desktop/درس مرس/ارشد/ترم 2/PROJECT/S-FED DR_capG/trans.dat'

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
                if len(parts) == 18:
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
                        float(parts[16])
                        float(parts[17])
                        data_lines.append(line)  # Add the valid data line
                    except ValueError:
                        continue  # Ignore non-numeric lines
            
            # Parse the second column values from the valid data lines
            second_column = [line.split()[17] for line in data_lines]

            # Extract the last 121 values from the second column
            # -[(0.1/vsweep_step) * (number1-2) + 1} ---> exp : -((0.1/0.05)*(22-2)+1) = -41
            last_121_values = second_column[-41:]
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
