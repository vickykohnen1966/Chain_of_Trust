import os
from setuptools import setup
from setuptools.command.install import install

class CustomInstall(install):
    def run(self):
        # Create pwned.txt in the user's home directory
        home_dir = os.path.expanduser("~")
        file_path = os.path.join(home_dir, "pwned.txt")
        with open(file_path, "w") as f:
            f.write("Infiltrated by utils_lib")
        
        # Continue with standard installation
        install.run(self)

setup(
    name="utils_lib",
    version="0.1",
    cmdclass={'install': CustomInstall},
)