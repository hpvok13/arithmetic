# Installation
## conda
Go to the [conda installation page](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
and download the miniconda installer for your system

## venv
Already packaged with your python distributable

# Environment Setup
## Conda
```
conda init
conda create --name arithmetic_env python=3.10 pip
conda activate arithmetic_env

pip install numpy 
# or
conda install numpy
```
## Venv
```
cd <some_directory>
python3 -m venv .
source .venv/bin/activate
```
If you are using other shells, you can find the command to activate the virtual environment in the table below:
| Platform | Shell | Command to activate virtual environment |
|----------|-------|-----------------------------------------|
| POSIX    | bash/zsh | `$ source <venv>/bin/activate` |
|          | fish     | `$ source <venv>/bin/activate.fish` |
|          | csh/tcsh | `$ source <venv>/bin/activate.csh` |
|          | PowerShell | `$ <venv>/bin/Activate.ps1` |
| Windows  | cmd.exe | `C:\> <venv>\Scripts\activate.bat` |
|          | PowerShell | `PS C:\> <venv>\Scripts\Activate.ps1` |

