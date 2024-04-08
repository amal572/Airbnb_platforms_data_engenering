from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from pandas import DataFrame
import pandas as pd
from os import path
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level as per your requirement

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_snowflake(input_dir, **kwargs) -> None:
    """
    Template for exporting data to a Snowflake warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#snowflake
    """
    table_name = 'your_table_name'
    database = 'AIRBNB'
    schema = 'AIRBNB'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    if not os.path.isdir(input_dir):
        logging.error(f'{input_dir} does not exist')
        raise FileNotFoundError(f'{input_dir} does not exist')
    
    logging.info(f'Input directory: {input_dir}')

    for folder_path, _, files in os.walk(input_dir):
        parquet_files = [f for f in files if f.endswith('.parquet')]
        for parquet_file in parquet_files:

            table_name = parquet_file[:-8]
            # Read Parquet file into DataFrame
            df = pd.read_parquet(path.join(folder_path, parquet_file))
            logging.info(f'Reading Parquet file: {parquet_file}')

            # Now you can add further processing inside this loop if needed

            # Here you can continue with the rest of your code
            
            with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
                loader.export(
                    df,
                    table_name,
                    database,
                    schema,
                    if_exists='replace',  # Specify resolution policy if table already exists
                )
                logging.info(f'Exported DataFrame to Snowflake table: {table_name}')

