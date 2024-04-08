import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(filename='transformer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def clean_airbnb_csv_data(csv_file_path: str) -> pd.DataFrame:
    """
    Cleans Airbnb CSV data.

    Args:
        csv_file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    schema = {
       'realSum': float,
       'room_type': str,
       'room_shared': bool,
       'room_private': bool,
       'person_capacity': int,
       'host_is_superhost': bool,
       'multi': bool,
       'biz': bool,
       'cleanliness_rating': int,
       'guest_satisfaction_overall': int,
       'bedrooms': int,
       'dist': float,
       'metro_dist': float,
       'lng': float,
       'lat': float
    }

    df = pd.read_csv(csv_file_path).astype(schema)

    df = df[schema.keys()]

    # Check if any columns has value null 
    for column in df.columns:
        assert not df[column].isnull().any()

    # Check for zero values in float columns
    float_columns = df.select_dtypes(include=['float']).columns

    for column in float_columns:
        assert (df[column] != 0).all()

    return df

@transformer
def transform(input_dir):
    """
    Template code for a transformer block.

    Args:
        input_dir (str): The directory containing CSV files to transform.

    Returns:
        str: The directory containing transformed Parquet files.
    """
    if not os.path.isdir(input_dir):
        raise FileNotFoundError(f'{input_dir} not exist')

    for path, _, files in os.walk(input_dir):
        csv_files = [file for file in files if file.endswith('.csv')]
        for csv_file in csv_files:
            csv_file_path = os.path.join(path, csv_file)
            parquet_file_path = csv_file_path.replace('.csv', '.parquet')
            df = clean_airbnb_csv_data(csv_file_path)
            df.to_parquet(parquet_file_path)
            logging.info(f'Transformed {csv_file_path} to {parquet_file_path}')  # Log transformation

    return input_dir


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

    
