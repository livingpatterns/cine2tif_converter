import os
import argparse

from utils import save_as_tif

def main():

    parser = argparse.ArgumentParser(description="cine2tif converter")

    parser.add_argument('--file_name', default=None, help='.cine file to be converted to .tif')
    parser.add_argument('--folder_name', default=None, help='all .cine files in folder are converted to .tif')

    args = parser.parse_args()

    file_name = args.file_name
    folder_name = args.folder_name


    if file_name is not None:
        working_dir, file = os.path.split(file_name)
        file = file[:-5] if file.lower().endswith(".cine") else file

        if working_dir == '':
            input_file = os.path.join(os.getcwd(), "cine_files", file + ".cine")
            output_file = os.path.join(os.getcwd(), "tif_files", file + ".cine")
            if not os.path.exists(os.path.join(os.getcwd(), "tif_files")):
                os.makedirs(os.path.join(os.getcwd(), "tif_files"))
        else:
            input_file = os.path.join(os.getcwd(), file + ".cine")
            output_file = os.path.join(os.getcwd(), file + ".tif")

        if os.path.exists(input_file):
            save_as_tif(input_file=input_file, output_file=output_file)
        else:
            print("Input file does not exist!")

        print(f"input_file: {input_file}")
        print(f"output_file: {output_file}")

    if folder_name is not None: 
        working_dir, folder = os.path.split(folder_name)
        print(working_dir)
        SRC_DIR = os.path.join(os.getcwd(), folder) if working_dir == '' else os.path.join(working_dir, folder)
        DST_DIR = os.path.join(os.getcwd(), "tif_files") if working_dir == '' else os.path.join(working_dir, folder, "tif_files")

        print(f"SRC_DIR: {SRC_DIR}")
        print(f"DST_DIR: {DST_DIR}")

        if os.path.exists(SRC_DIR):

            if not os.path.exists(DST_DIR):
                os.makedirs(DST_DIR)

            # Iterate through .txt files
            for filename in os.listdir(SRC_DIR):
                if filename.endswith(".cine"):
                    input_file = os.path.join(SRC_DIR, filename)
                    output_file = os.path.join(DST_DIR, filename.replace('.cine', '.tif'))
                    save_as_tif(input_file=input_file, output_file=output_file)
        else:
            print("Input folder does not exist!")


if __name__ == "__main__":
    main()