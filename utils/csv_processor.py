import base64
import pandas as pd
from io import BytesIO

def decode_base64_csv(base64_string):
    """Decodes a base64-encoded CSV file and returns a DataFrame."""
    try:
        # Decode base64 and read as CSV
        csv_bytes = base64.b64decode(base64_string + '==')
        csv_df = pd.read_csv(BytesIO(csv_bytes))
    except Exception as e:
        raise ValueError("Error decoding or reading CSV file") from e

    return csv_df
