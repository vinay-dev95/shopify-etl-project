# etl/process_csv.py

from .extract import extract_csv_data
from .transform import transform_df
from .load import load_to_db
from database.config import get_db_session

def process_csv(path):
    df = extract_csv_data(path)
    df = transform_df(df)
    db = get_db_session()
    load_to_db(df, db)
