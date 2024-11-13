import base64
import pandas as pd
from utils.csv_processor import decode_base64_csv

def test_decode_base64_csv():
    # Create a base64-encoded sample CSV
    csv_content = "Intent,Description\nTestIntent,Test description"
    base64_csv = base64.b64encode(csv_content.encode('utf-8')).decode('utf-8')

    # Decode the base64 string and check the DataFrame output
    df = decode_base64_csv(base64_csv)
    assert isinstance(df, pd.DataFrame)
    assert df.loc[0, 'Intent'] == "TestIntent"
    assert df.loc[0, 'Description'] == "Test description"
