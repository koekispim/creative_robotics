"""
This file check is there are empty csv file
What it does:
print the empty file name

"""

import os
import glob
import pandas as pd

csv_folder = "dataset generation/data_motion_5000(parametric)/"  # change to your directory
csv_files = sorted(glob.glob(os.path.join(csv_folder, "*.csv")))

short_files = []

# check all the files, print empty csv file
for f in csv_files:

    df = pd.read_csv(f)
    motion = df[['X_mm','Y_mm','Z_mm']].dropna()
    if len(motion) < 3:
        short_files.append(os.path.basename(f))
        print(f"Found {f} empty")
