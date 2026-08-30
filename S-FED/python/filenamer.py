import os

# Define a function to rename the files
def rename_files_in_pattern(folder_path):
    # Get a list of all .dat files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.dat')]

    for file_name in files:
        try:
            # Extract the numeric part of the file name
            numeric_part = int(file_name.split('.')[0])
            
            # Calculate the new number for the file name
            new_number = numeric_part // 10  # Integer division by 10
            
            # Create the new file name
            new_file_name = f"{new_number}.dat"
            
            # Rename the file
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_file_name)
            os.rename(old_path, new_path)
            
            print(f"Renamed {file_name} to {new_file_name}")
        except ValueError:
            print(f"Skipping {file_name}: not a valid numeric file name")
        except Exception as e:
            print(f"Error renaming {file_name}: {e}")

# Specify the folder containing the .dat files
folder_path = "C:/Users/USER/Desktop/درس مرس/ارشد/ترم 2/PROJECT/VGS/vgs_0"  # Replace with your folder path
rename_files_in_pattern(folder_path)
