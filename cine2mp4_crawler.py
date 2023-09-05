"""
Description:

This script is designed to automate the process of converting .cine files to .mp4 format within specified parent folders. The steps of operation are:

1. Accepts the name of a parent folder as input.
2. Recursively navigates through each subdirectory of the provided parent folder.
3. Identifies any .cine files present within these subdirectories.
4. For each found .cine file:
    - A corresponding -mp4 directory is created within the parent folder (if it doesn't already exist).
    - The .cine file's contents are converted into .mp4 format.
    - The newly created .mp4 file is saved in the -mp4 directory, retaining the original file's name but with a .csv extension.
"""

import os

from utils import save_as_mp4, nd2_to_mp4


def main(folder_name):
    # Iterate over subdirectories of the main folder
    for root, dirs, files in os.walk(folder_name):
        dirs[:] = [d for d in dirs if not d.startswith(('.', '$'))]
        for file in files:
            if file.endswith('.cine'):
                # Create the converted directory if it doesn't exist
                converted_dir = os.path.join(folder_name, "cine2mp4conversions", os.path.basename(root) + '-mp4')
                if not os.path.exists(converted_dir):
                    os.makedirs(converted_dir)

                # Convert the .txt file to .csv and save in the converted directory
                input_file = os.path.join(root, file)
                output_file = os.path.join(converted_dir, os.path.splitext(file)[0] + '.mp4')
                if os.path.exists(output_file):
                    print(f"{output_file} already exists.")
                else:
                    try:
                        save_as_mp4(input_file=input_file, output_file=output_file, fps=30)
                        print(f"Conversion {input_file} to {output_file} complete.")
                    except Exception as e:
                        print(f"Error encountered: {e} in converting {input_file} to {output_file}.")
            
            elif file.endswith('.nd2'):
                # Create the converted directory if it doesn't exist
                converted_dir = os.path.join(folder_name, "nd2mp4conversions", os.path.basename(root) + '-mp4')
                if not os.path.exists(converted_dir):
                    os.makedirs(converted_dir)

                # Convert the .txt file to .csv and save in the converted directory
                input_file = os.path.join(root, file)
                output_file = os.path.join(converted_dir, os.path.splitext(file)[0] + '.mp4')
                if os.path.exists(output_file):
                    print(f"{output_file} already exists.")
                else:
                    try:
                        nd2_to_mp4(input_file=input_file, output_file=output_file, fps=30)
                        print(f"Conversion {input_file} to {output_file} complete.")
                    except Exception as e:
                        print(f"Error encountered: {e} in converting {input_file} to {output_file}.")

if __name__ == "__main__":
    parent_folder = input("Enter the parent folder name: ")
    main(parent_folder)
