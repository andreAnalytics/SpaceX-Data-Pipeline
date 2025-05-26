import singer
import pandas as pd
import math

LOGGER = singer.get_logger()

def sanitize_floats(obj):
    if isinstance(obj, float):
        if math.isinf(obj) or math.isnan(obj):
            return None
        return obj
    elif isinstance(obj, dict):
        return {k: sanitize_floats(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize_floats(v) for v in obj]
    else:
        return obj

# Define schema (partial, add fields as needed)
schema = {
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'rocket':{'type': 'string'},
        'success':{'type':['number','null']},
        'date_utc': {'type': 'string', 'format': 'date-time'},
        # Add more fields here if required
    }
}

def main():
    url = 'https://api.spacexdata.com/v4/launches'
    
    # Load data into DataFrame
    df = pd.read_json(url)

    # Clean the DataFrame: replace inf, -inf, NaN with None
    df = df.replace([float('inf'), float('-inf')], pd.NA)
    df = df.where(pd.notnull(df), None)

    # Convert to records (list of dicts)
    raw_records = df.to_dict(orient='records')

    # Sanitize each record
    clean_records = [sanitize_floats(record) for record in raw_records]

    # Emit schema and records
    singer.write_schema('launches', schema, ['id'])
    singer.write_records('launches', clean_records)

if __name__ == '__main__':
    main()