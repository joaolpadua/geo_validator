import os
import geopandas as gpd


def read_files(input_path):
    """
    Lê arquivos .shp e .geojson de uma pasta (incluindo subpastas)
    e retorna uma lista de tuplas (nome_do_arquivo, GeoDataFrame).
    """
    files_data = []

    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith((".shp", ".geojson")):
                full_path = os.path.join(root, file)
                gdf = gpd.read_file(full_path)
                files_data.append((file, gdf))

    return files_data