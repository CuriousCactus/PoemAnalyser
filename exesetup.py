
a=input("umm")
from cx_Freeze import setup, Executable

includefiles = []
includes = []
excludes = []
packages = []

setup(
    name = 'yourgame',
    version = '1.0.0',
    description = '',
    author = 'John Doe',
    author_email = 'johndoe@gmail.com',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('tk_colouring.py')]
)

a=input("umm")
