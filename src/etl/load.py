# etl/load.py
def load_to_db(df, db):
    from database.models import Product, InactiveProduct

    active_rows = df[df["status"] == "ACTIVE"]
    inactive_rows = df[df["status"] == "INACTIVE"]

    # Insert ACTIVE rows into product table
    active_objects = [
        Product(
            device_name=row.device_name,
            variant_grams=row.variant_grams,
            vendor=row.vendor,
            variant_sku=row.variant_sku,
            variant_inventory_tracker=row.variant_inventory_tracker,
            status=row.status,
            variant_type=row.variant_type,
            variant_price=row.variant_price
        )
        for row in active_rows.itertuples()
    ]

    # Insert INACTIVE rows into inactive_products table
    inactive_objects = [
        InactiveProduct(
            device_name=row.device_name,
            variant_grams=row.variant_grams,
            vendor=row.vendor,
            variant_sku=row.variant_sku,
            variant_inventory_tracker=row.variant_inventory_tracker,
            status=row.status,
            variant_type=row.variant_type,
            variant_price=row.variant_price
        )
        for row in inactive_rows.itertuples()
    ]

    # Save both
    db.bulk_save_objects(active_objects)
    db.bulk_save_objects(inactive_objects)
    db.commit()
