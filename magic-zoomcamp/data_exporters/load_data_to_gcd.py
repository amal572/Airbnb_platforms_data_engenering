from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from pandas import DataFrame
from os import listdir

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_snowflake(input_dir, **kwargs) -> None:
    """
    Template for exporting data to a Snowflake warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#snowflake
    """
    database = 'Airbnb'
    schema = 'Airbnb'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Test connection to Snowflake
    try:

        if not os.path.isdir(input_dir):
           raise FileNotFoundError(f'{input_dir} not exist')

        snowflake_conn = Snowflake.with_config(ConfigFileLoader(config_path, config_profile))
        print(snowflake_conn)
       # snowflake_conn.connect()'
        #config_path = path.join(get_repo_path(), 'io_config.yaml')
        #config_profile = 'default'

        # Iterate over each folder path
        for path, _, files in os.walk(input_dir):
            # Get a list of Parquet files in the folder
            #parquet_files = [f for f in listdir(folder_path) if f.endswith('.parquet')]
            parquet_files = [file for file in files if file.endswith('.parquet')]
            print(parquet_files)
            # Iterate over each Parquet file
            for parquet_file in parquet_files:
                table_name = parquet_file[:-8]  # Remove '.parquet' extension to derive table name
                
                print(table_name)
                # Read Parquet file into DataFrame
                df = pd.read_parquet(path.join(folder_path, parquet_file))
                
                # Export DataFrame to Snowflake
                with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
                    loader.export(
                        df,
                        table_name,
                        database,
                        schema,
                        if_exists='replace'  # Specify resolution policy if table already exists
                    )
        print("Connection to Snowflake successful!")
    except Exception as e:
        print("Connection to Snowflake failed:", e)
        return  # Exit function if connection failed

    #with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
    #    loader.export(
    #        df,
    #        table_name,
    #        database,
    #        schema,
    #        if_exists='replace',  # Specify resolution policy if table already exists
    #    )
