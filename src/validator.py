def validate_invalid_geometry(file_name, gdf):
    errors = []

    invalid = gdf[~gdf.is_valid]

    for idx in invalid.index:
        errors.append({
            "file_name": file_name,
            "error_type": "invalid_geometry",
            "feature_index": idx
        })

    return errors