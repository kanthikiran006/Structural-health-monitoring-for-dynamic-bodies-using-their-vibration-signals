import os
import zipfile
import numpy as np

# Create a directory to store the dataset and navigate into it
os.makedirs('/content/MetroDataset', exist_ok=True)
os.chdir('/content/MetroDataset')

# Download the correct dataset file from Google Drive
# This file contains the pre-computed IMFs in .npz format
!gdown --id 1CmqtHQVI4ElKIzMWMnIFewGJ-no1Dh8S --output imfs_all.zip

# Unzip the downloaded file to access the .npz files
with zipfile.ZipFile('imfs_all.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

# Load the extracted .npz file using the correct path and file name
# The file is named 'imfs.npz' after extraction
data = np.load('imfs.npz')

# The data is stored under the key 'imfs' inside the file
imfs_data = data['imfs']

# Print the top 10 rows of the 'imfs' array
print(imfs_data[:10, :])
