#!/bin/bash
chmod +x setup_and_run.sh

# Print current working directory
pwd

# Install Robot Framework and Robot Framework AppiumLibrary
python3 -m pip install robotframework
python3 -m pip install robotframework-appiumlibrary

# Print Python version and installed packages
python3 --version
pip3 list
pip3 install pytest
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
source ~/.bashrc
nvm install node

# Run the Robot Framework test suite specified in the requirements.txt file