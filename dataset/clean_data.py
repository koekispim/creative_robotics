"""
This file is to clean the data generated from kuka prc
What it does:
1. Delete extreme value of start and end points
2. Shrink the data sequence from kuka prc

"""

import pandas as pd
import os
import pandas as pd

input_folder = "dataset generation\data_motion_5000(parametric)"
output_folder = "dataset generation\data_motion_5000(parametric)_cleaned"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        df = pd.read_csv(input_path)

        cols_to_keep = ["X_mm", "Y_mm", "Z_mm", "alpha_rad", "beta_rad", "gamma_rad"]
        df = df[cols_to_keep]

        # clean the first and last three rows (delete extreme value)
        if len(df) > 6:
            df = df.iloc[3:-3].reset_index(drop=True)

        # collect every 4 rows (shrink the data from kuka prc)
        df = df.iloc[::4, :].reset_index(drop=True)


        df.to_csv(output_path, index=False)
        print(f"{filename} finished, output file: {output_path}")

print("🎉 finished")