# Data Loader
import io
import pandas as pd
import requests
from datetime import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Loading data from floods API.
    """
    url = 'http://environment.data.gov.uk/flood-monitoring/id/floods.json'
    response = requests.get(url)
    data = response.json()
    items = data['items']

    # Create a DataFrame from the API response
    df = pd.DataFrame(items)

    # Convert timestamp columns to datetime
    timestamp_columns = ['timeRaised', 'timeMessageChanged', 'timeSeverityChanged']
    for col in timestamp_columns:
        df[col] = pd.to_datetime(df[col])
    df['dateRaised']= df['timeRaised'].dt.date
    df =df.drop(columns='message')

    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert isinstance(output, pd.DataFrame), 'Output should be a pandas DataFrame'
    assert len(output) > 0, 'The DataFrame should have at least one row'

# import io
# import pandas as pd
# import requests
# if 'data_loader' not in globals():
#     from mage_ai.data_preparation.decorators import data_loader
# if 'test' not in globals():
#     from mage_ai.data_preparation.decorators import test


# @data_loader
# def load_data_from_api(*args, **kwargs):
#     """
#     loading data from floods API
#     """
#     url = 'http://environment.data.gov.uk/flood-monitoring/id/floods.json'
    
#     response = requests.get(url)
#     data = response.json()
#     items = data['items']
#     df = pd.DataFrame(items)

#     return df

# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
