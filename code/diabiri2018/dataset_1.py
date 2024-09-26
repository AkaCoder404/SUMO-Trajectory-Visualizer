"""
Code to convert the raw geolife dataset to the starting combined dataset.

Geolife Dataset Originally

geolife/Data
    000/
        2008XX1.plt
        2008XX2.plt
        ...
    ...
    010/
        2008XX1.plt
        2008XX2.plt
        labels.txt
        ...

Want it to transform into
geolife/CombinedData
    combined_000.plt
    combined_001.plt
    ...
    label_010.plt
    ...

"""

import os
import glob
import pandas as pd

# Function to read .plt file and return the DataFrame
def read_plt(plt_file):
    points = pd.read_csv(plt_file, skiprows=6, header=None)
    points.columns = ['lat', 'lon', 'none', 'alt', 'days_past', 'date', 'time']
    points['timestamp'] = pd.to_datetime(points['date'] + ' ' + points['time'], format='%Y-%m-%d %H:%M:%S')
    points.drop(columns=['none'], inplace=True)
    return points

# Function to read label file
def read_label_file(driver, file):
    labels = pd.read_csv(file, skiprows=1, header=None, sep='\t')
    labels.columns = ['start_time', 'end_time', 'transport_mode']
    labels['start_time'] = pd.to_datetime(labels['start_time'])
    labels['end_time'] = pd.to_datetime(labels['end_time'])
    return labels

# Function to combine all plt files for a driver
def combine_plt_files(driver):
    plt_files = glob.glob(f'data/geolife/Data/{driver}/Trajectory/*.plt')
    combined_df = pd.concat([read_plt(plt_file) for plt_file in plt_files], ignore_index=True)
    return combined_df

# Function to save combined plt data and labels
def save_combined_data(driver, combined_df, labels_df=None):
    output_dir = 'data/geolife/CombinedData'
    os.makedirs(output_dir, exist_ok=True)
    
    # Save combined .plt file for the driver
    combined_file = os.path.join(output_dir, f'combined_{driver}.plt')
    combined_df.to_csv(combined_file, index=False, sep=',')
    
    if labels_df is not None:
        # Save labels file for the driver
        label_file = os.path.join(output_dir, f'label_{driver}.plt')
        labels_df.to_csv(label_file, index=False, sep=',')

# Main function to process all drivers
def process_geolife_data():
    drivers = os.listdir('data/geolife/Data/')
    drivers = [driver for driver in drivers if os.path.isdir(f'data/geolife/Data/{driver}')]
    drivers.sort()

    for driver in drivers:
        print(f'Processing driver {driver}...')
        
        # Combine all plt files for the current driver
        combined_df = combine_plt_files(driver)

        # Check if labels.txt exists and process it
        label_file = f'data/geolife/Data/{driver}/labels.txt'
        if os.path.exists(label_file):
            labels_df = read_label_file(driver, label_file)
            save_combined_data(driver, combined_df, labels_df)
        else:
            save_combined_data(driver, combined_df)

# Run the processing
if __name__ == "__main__":
    process_geolife_data()