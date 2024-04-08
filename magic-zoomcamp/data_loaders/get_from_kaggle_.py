import io
import os
import pandas as pd
import requests
import zipfile
import tempfile
import logging

# Set up logging
logging.basicConfig(filename='data_loader.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    # URL of the zip file
    #url = 'https://drive.google.com/file/d/1-Ibjb4zcowQDu1JcmHoSS3SMmr50qd5m/view?usp=sharing'

    # Directory for saving the downloaded zip file
    project_file = './data-source/'
    project_file_out = './data-source/archive'
    project_dir = os.path.abspath(project_file)
    data_source_dir = os.path.join(project_dir, 'data-source')
    archive_zip = os.path.join(data_source_dir, 'archive.zip')

    # Ensure the directory exists, create if it doesn't
    os.makedirs(data_source_dir, exist_ok=True)
    
    # Extract zip file
    with zipfile.ZipFile(archive_zip) as zip_file:
        for member in zip_file.infolist():
            extracted_file_path = os.path.join(project_file_out, member.filename)
            logging.info(f'Extracting {extracted_file_path}...')  # Log the extraction process
            zip_file.extract(member, path=project_file_out)
    
    return project_file_out


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    logging.info('Test output successful')  # Log successful test output
