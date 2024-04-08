import io
import pandas as pd
import requests
import zipfile
import os
import pyarrow.parquet as pq
import time
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


# Function to download file from URL with retries
def download_file_with_retry(url, output_path, max_retries=3):
    for i in range(max_retries):
        try:
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(output_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            return True
        except Exception as e:
            print(f"Download failed (attempt {i+1}/{max_retries}): {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying
    print("Download failed after multiple attempts.")
    return False

# Function to check if file download is complete
def is_file_complete(file_path, expected_size):
    if os.path.exists(file_path):
        return os.path.getsize(file_path) == expected_size
    return False

# Function to check if the downloaded file is a valid zip file
def is_zip_file_valid(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.testzip()
        return True
    except zipfile.BadZipFile:
        return False

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    
    # Define the directory containing the Parquet files
    #url = 'https://drive.usercontent.google.com/download?id=1laSM-xQCnJtb1_-_MxMceG02kzo6taPx&export=download&authuser=0'

    # Output directory where the Parquet files will be downloaded
    output_directory = './data/'
    #expected_size = 121

    # Download the single file containing multiple Parquet files
    #downloaded_successfully = download_file_with_retry(url, output_directory)

    #if downloaded_successfully and is_file_complete(output_path, expected_size) and is_zip_file_valid(output_path):
        # Unzip the downloaded file
      #  with zipfile.ZipFile(output_path, 'r') as zip_ref:
       #     zip_ref.extractall(output_directory)

    # Read all Parquet files from the output directory into a list of DataFrames
    parquet_files = []
    for file_name in os.listdir(output_directory):
        if file_name.endswith('.parquet'):
            print(pd.read_parquet(os.path.join(output_directory, file_name)))
            parquet_files.append(pd.read_parquet(os.path.join(output_directory, file_name)))

    print(parquet_files)
    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(parquet_files, ignore_index=True)

    # Save the combined DataFrame to a CSV file
    combined_df.to_csv('combined_data.csv', index=False)

        
    return combined_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
