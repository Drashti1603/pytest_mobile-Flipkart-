#!/bin/bash
chmod +x setup_and_run.sh

# Print current working directory
pwd

# Install Robot Framework and Robot Framework AppiumLibrary
python3 -m pip install robotframework
python3 -m pip install robotframework-appiumlibrary
npm cache clean --force

# Print Python version and installed packages
python3 --version
pip3 list
pip3 install pytest
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
# Set NVM directory and source NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm

# Check if NVM is sourced correctly
if command -v nvm >/dev/null 2>&1; then
    echo "NVM sourced successfully."
else
    echo "Error: NVM not sourced properly."
    exit 1
fi
nvm install node
npm install -g appium

# Run the Robot Framework test suite specified in the requirements.txt file