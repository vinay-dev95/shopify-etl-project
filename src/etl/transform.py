#etl/transform.py

def transform_df(df):
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df["variant_sku"] = df["variant_sku"].astype(str).replace("'", "", regex=True)
    df["variant_price"] = df["variant_price"].astype(float)
    df["variant_grams"] = df["variant_grams"].astype(float)
    df["status"] = df["status"].str.upper()
    return df
