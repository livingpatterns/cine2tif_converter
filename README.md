# cine2tif_converter
Python script to convert `.cine` files to `.tif` format.

### Setup
To setup got to your install/code directory, and type:
```sh
git clone https://github.com/livingpatterns/cine2tif_converter.git
```

#### Custom Environment
Create a virtual environment to install Python libraries. We use the python virtual environment [venv](https://docs.python.org/3/library/venv.html) for this.

``` bash
python -m venv venv
```

###### Activate your environment 

`On Windows`
- In cmd.exe
    ``` sh
    .\venv\Scripts\Activate.bat
    ```
- In PowerShell
    ``` sh
    .\venv\Scripts\Activate.ps1
    ```
`On macOS and Linux`
- In the terminal:
    ``` sh
    source .venv/bin/activate
    ```

#### Setup Dependencies
Install all requirements:
``` bash
pip install -r requirements.txt
```

#### Changes in pycine

After the installation of required packages navigate into pycine.color script find the color_pipeline function and comment the following two lines of code:

``` bash
    BayerPatterns = {3: "gbrg", 4: "rggb"}
    pattern = BayerPatterns[setup.CFA]
```

and paste the following instead:

``` bash
    if hasattr(setup, "CFA"):
        BayerPatterns = {3: "gbrg", 4: "rggb"}
        pattern = BayerPatterns[setup.CFA] if setup.CFA == 3 or setup.CFA == 4 else "gbrg"
    else:
        pattern = "gbrg"
```

Again in pycine.color (pycine --version == 0.3.2) script comment any print statement in `color_pipeline` and  `whitebalance_raw` functions, you can use `ctrl+k+c` keys to comment multiple lines of code in VS Code. This is an optional step but the additional print statements in these functions intervene with the progress bar. 

### How to Use

Open a command prompt or terminal.
Navigate to the directory where you have saved the project files using the cd command. For example:

``` bash
cd path/to/cine2tif_converter
```

##### Examples of Usage:

1. Convert a single file in `.\cine_files` and save the output into `.\tif_files`: 
    ``` bash
    python cine2tif.py --file_name file_name.cine
    ```
2. Convert a single file in another location and save the output in the same location:
    ``` bash
    python cine2tif.py --file_name path/to/file/file_name.cine
    ```
3. Convert all the .cine files under `.\` and save the outputs to `.\tif_files`: 
    ``` bash
    python cine2tif.py --folder_name cine_files    
    ``` 
4. Convert akk the .cine files in another location and save the outputs in `path/to/folder/tif_files`
    ``` bash
    python cine2tif.py --folder_name path/to/folder/folder_name
    ```
