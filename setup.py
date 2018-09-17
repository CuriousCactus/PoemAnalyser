import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": [], "include_files": ["data"]}

company_name, product_name="LoisApps", "PoemAnalyser"

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "ProgramMenuFolder",          # Directory_
     "PoemAnalyser",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]tk_colouring.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

#bdist_msi_options = {'data': msi_data}

bdist_msi_options = {
    'upgrade_code': '{66620F3A-DC3A-11E2-B341-002219E9B01E}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    'data': msi_data
    
    }

# GUI applications require a different base on Windows (the default is for a
# console application).

# GUI applications require a different base on Windows
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(script='tk_colouring.py',
                 base=base,
                 #icon='MyGui.ico',
                #shortcutName="PoemAnalyser",
                #shortcutDir="DesktopFolder",
                )

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name=product_name,
      version='1.0.0',
      description='blah',
        options = {'bdist_msi': bdist_msi_options,"build_exe": build_exe_options},
        executables = [exe])








