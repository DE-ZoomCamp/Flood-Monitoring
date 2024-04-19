# Data Exporter
import pandas as pd
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Export the entire DataFrame to Google Cloud Storage, keeping previous versions.
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    bucket_name = 'flood-bucket24'
    object_key = 'floods.csv'

    # Load the existing data from GCS
    gcs = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile))
    try:
        existing_df = gcs.load(bucket_name, object_key)
    except FileNotFoundError:
        existing_df = pd.DataFrame()

    # Combine the new and existing data, keeping the latest measurements
    combined_df = pd.concat([existing_df, df], ignore_index=True)
    combined_df.drop_duplicates(subset=['@id'], keep='last', inplace=True)

    # Export the combined DataFrame to GCS
    gcs.export(combined_df, bucket_name, object_key)

