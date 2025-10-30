"""
This file is to extract Cartesian coordinates in the xml file from kuka prc and save in csv form

"""
import os
import xml.etree.ElementTree as ET
import csv

# Folder containing XML files
xml_folder = r'dataset generation\motion'
# Output folder for CSV files
csv_folder = r'dataset generation\csv_outputs'
os.makedirs(csv_folder, exist_ok=True)

# Loop through all XML files in the folder
for filename in os.listdir(xml_folder):
    if filename.lower().endswith('.xml'):
        xml_file = os.path.join(xml_folder, filename)
        csv_file = os.path.join(csv_folder, filename.replace('.xml', '.csv'))

        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Open CSV
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(['A1','A2','A3','A4','A5','A6','A7',
                             'X_mm','Y_mm','Z_mm','alpha_rad','beta_rad','gamma_rad'])

            # Loop through all PRC_CMD elements
            for cmd in root.findall('.//PRC_CMD'):
                # Initialize empty values
                a_vals = ['']*7
                xyz_vals = ['']*6

                # Extract joint angles if AXIS exists
                axis = cmd.find('AXIS')
                if axis is not None:
                    a_vals[0] = axis.findtext('A01','')
                    a_vals[1] = axis.findtext('A02','')
                    a_vals[2] = axis.findtext('A03','')
                    a_vals[3] = axis.findtext('A04','')
                    a_vals[4] = axis.findtext('A05','')
                    a_vals[5] = axis.findtext('A06','')
                    a_vals[6] = axis.findtext('A07','')

                # Extract frame positions if FRAME exists
                frame = cmd.find('FRAME')
                if frame is not None:
                    inner_frame = frame.find('FRAME')
                    if inner_frame is not None:
                        frame = inner_frame
                    xyz_vals[0] = frame.findtext('X','')
                    xyz_vals[1] = frame.findtext('Y','')
                    xyz_vals[2] = frame.findtext('Z','')
                    xyz_vals[3] = frame.findtext('A','')
                    xyz_vals[4] = frame.findtext('B','')
                    xyz_vals[5] = frame.findtext('C','')

                # Write row
                writer.writerow(a_vals + xyz_vals)

        print(f"✅ CSV generated: {csv_file}")
